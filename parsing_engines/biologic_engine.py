import re
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple, Union

import pandas as pd
import yaml
from pandas.core.dtypes.common import is_numeric_dtype

from .battery_exceptions import UnsupportedFileTypeError
from .mappings import COLUMN_NAME_MAPPING
from .parsing_engines_base import ParsingEngineBase


class BiologicCSVnTSVParser(ParsingEngineBase):
    """ParserBase for the csv and tsv output of the BioLogic cycler."""

    name = "biologic"
    description = "Biologic CSV/TSV/MPT"
    valid: List[Tuple[str, str]] = [
        ("text/plain", ".csv"),
        ("text/plain", ".mpt"),
        ("text/plain", ".tsv"),
        ("text/plain", ".txt"),
    ]
    MANDATORY_COLUMNS = {"Time", "Rec#", "Ns"}

    # Assumed to be this encoding, but iot might be different...
    encoding = "iso-8859-1"

    def __init__(self, file_path: Union[Path, str]) -> None:
        """Initialise the parser and load the data into the Pandas dataframe."""
        super(BiologicCSVnTSVParser, self).__init__(file_path)

        self.skip_rows = self._get_header_size()
        self.data = self._load_data()

        # Some preprocessing that can be done straight away
        self._drop_unnamed_columns()
        self._standardise_columns()
        self._create_rec_no()

    def _get_header_size(self) -> int:
        """Reads the file and determines the size of the header.

        Returns:
            Header size as an int
        """
        with open(self.file_path, encoding=self.encoding) as datafile:
            if next(datafile) == "BT-Lab ASCII FILE\n":
                return int(re.findall(r"[0-9]+", next(datafile))[0]) - 1
            return 0

    def _load_data(self) -> pd.DataFrame:
        """Loads the data as a Pandas data frame.

        Can work with files that have a header or that do not have one. It is assumed
        that the separator is a comma (,). If there is only 1 column, it is reloaded
        using tabs. If there is still only 1 column, an erro is raised.

        Raises:
            UnsupportedFileTypeError: If only one column is found after trying comma and
            tabs as separators.

        Returns:
            A pandas dataframe with all the data.
        """
        kwargs = dict(engine="python", skiprows=self.skip_rows, encoding=self.encoding)

        try:
            data = pd.read_csv(self.file_path, delimiter=",", **kwargs)
        except pd.errors.ParserError:
            try:
                data = pd.read_csv(self.file_path, delimiter="\t", **kwargs)
            except pd.errors.ParserError:
                raise UnsupportedFileTypeError()

        if len(data.columns) == 1:
            data = pd.read_csv(self.file_path, delimiter="\t", **kwargs)

        if len(data.columns) == 1:
            raise UnsupportedFileTypeError()

        return data

    def _create_rec_no(self) -> None:
        """Adds Rec# to the dataset if it was not already present."""
        if "Rec#" not in self.data.columns:
            self.data["Rec#"] = range(len(self.data))

    def _drop_unnamed_columns(self) -> None:
        """Drops columns of the internal parser dataframe that have no name."""
        self.data = self.data.loc[:, ~self.data.columns.str.contains("^Unnamed")]

    def _standardise_columns(self) -> None:
        """Standardise column names using a mapping of standard names."""
        self.data.rename(columns=COLUMN_NAME_MAPPING, inplace=True)

    def get_column_info(self) -> Dict:
        """Gathers some metadata for each column.

        In particular, it gathers if it is a numeric column and if it has data.

        Returns:
            A nested dictionary with the above information for each column, proved as
            keys 'is_numeric' and 'has_data.
        """ ""
        return {
            k: {
                "is_numeric": is_numeric_dtype(self.data[k].dtype),
                "has_data": True,
            }
            for k in self.data.columns
        }

    def _get_file_header(self) -> List[str]:
        """Extracts the header from the Biologic file.

        Returns:
            A list of rows for the header, without the termination characters and
            empty lines.
        """
        with open(self.file_path, encoding=self.encoding) as f:
            header = list(
                filter(len, (f.readline().strip("\n") for _ in range(self.skip_rows)))
            )
        return header  # noqa

    def get_metadata(self) -> Dict:
        """Obtain all the metadata from the header of the file and related to the cycler
        and experimental conditions.

        Returns:
            A dictionary with the metadata
        """
        metadata: Dict[str, Any] = {
            "Dataset_Name": self.file_path.stem,
            "dataset_size": self.file_path.stat().st_size,
            "num_rows": len(self.data),
            "data_start": self.skip_rows,
            "first_sample_no": self.skip_rows + 1,
            "file_metadata": header_to_yaml(self._get_file_header()),
            "warnings": [],
        }

        if not self.MANDATORY_COLUMNS.issubset(self.data.columns):
            metadata["warnings"].append(
                "Not all mandatory columns are present in the raw datafile"
            )

        return metadata

    def get_data_generator_for_columns(
        self, columns: list, first_data_row: int = 0, col_mapping: Optional[Dict] = None
    ) -> Generator[list, None, None]:
        """Provides the data filtered by the requested columns and a column mapping.

        Args:
            columns (List): Columns of data to provide
            first_data_row (int): First row of data to parse (NOT USED)
            col_mapping (Optional[Dict], optional): Dictionary to map the required
            column names to the Maccor file column names. Defaults to None.

        Raises:
            KeyError if the required columns, after applying the mapping, do not exist
                in the data.

        Returns:
            Union[Generator[Dict, None, None], NDArray]: [description]
        """
        cols = (
            [col_mapping.get(c, c) for c in columns]
            if col_mapping is not None
            else columns
        )

        for row in self.data[cols].itertuples():
            yield list(row)[1:]


yaml_replacements = {
    "\t": "    ",  # tabs form lists. in YAML, tab indents are not valid
    "BT-Lab ASCII FILE": "FileType : BT-Lab ASCII FILE",
    "Modulo Bat": "Mode: Modulo Bat",
    "BT-Lab for windows": "BT-Lab for windows : ",
    "Internet server": "Internet server : ",
    "Command interpretor": "Command interpretor : ",
    "for DX =": "DX/DQ : for DX =",
    "Record": "Record : ",
}


def header_to_yaml(header: List[str]) -> Dict:
    """Adapt BioLog file header to YAML format.

    The format of the BioLogix header is "almost" parsable directly as YAML We can hack
    in a few string replacements to make it valid. Table containg per-column metadata
    is not parseable as YAML. We skip this for now - find line where it starts,
    and end there.

    TODO: The table-like part of the header contains useful information related to the
    cycler protocol. This should be extracted somehow and making it available.

    Args:
        header: The header as a list fo strings.

    Returns:
        A dictionary parsed by YAML
    """

    # 1) Apply replacements
    regex = re.compile("(%s)" % "|".join(map(re.escape, yaml_replacements.keys())))
    rep_header = [
        regex.sub(lambda mo: yaml_replacements[mo.group()], h) for h in header
    ]

    # 2) Find parseable data before the table-like region
    parseable_lines = []
    for line in rep_header:
        if line.startswith("Ns"):
            break
        parseable_lines.append(line)

    # 3) Parse the header using YAML
    return yaml.safe_load("\n".join(parseable_lines))
