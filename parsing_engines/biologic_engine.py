import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import pandas as pd
import yaml

from .battery_exceptions import UnsupportedFileTypeError
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

    # Assumed to be this encoding, but it might be different...
    encoding = "iso-8859-1"

    @classmethod
    def factory(cls, file_path: Union[Path, str]) -> ParsingEngineBase:
        """Factory method for creating a parsing engine.

        Args:
            file_path (Union[Path, str]): Path to the file to load.
        """
        skip_rows = get_header_size(file_path, cls.encoding)
        data = load_biologic_data(file_path, skip_rows, cls.encoding)
        return cls(file_path, skip_rows, data)

    def _get_file_header(self) -> Dict[str, Any]:
        """Extracts the header from the Biologic file.

        Returns:
            A list of rows for the header, without the termination characters and
            empty lines.
        """
        with open(self.file_path, encoding=self.encoding) as f:
            header = list(
                filter(len, (f.readline().strip("\n") for _ in range(self.skip_rows)))
            )
        return header_to_yaml(header)


def get_header_size(file_path: Union[Path, str], encoding: str) -> int:
    """Reads the file and determines the size of the header.

    Returns:
        Header size as an int
    """
    with open(file_path, encoding=encoding) as datafile:
        if next(datafile) == "BT-Lab ASCII FILE\n":
            return int(re.findall(r"[0-9]+", next(datafile))[0]) - 1
        return 0


def load_biologic_data(
    file_path: Union[Path, str], skip_rows: int, encoding: str
) -> pd.DataFrame:
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
    kwargs = dict(engine="python", skiprows=skip_rows, encoding=encoding)

    try:
        data = pd.read_csv(file_path, delimiter=",", **kwargs)
    except pd.errors.ParserError:
        try:
            data = pd.read_csv(file_path, delimiter="\t", **kwargs)
        except pd.errors.ParserError:
            raise UnsupportedFileTypeError()

    if len(data.columns) == 1:
        data = pd.read_csv(file_path, delimiter="\t", **kwargs)

    if len(data.columns) == 1:
        raise UnsupportedFileTypeError()

    return data


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
