from typing import (
    Any,
    Dict,
    Generator,
    Iterable,
    List,
    Optional,
    Sequence,
    Text,
    Tuple,
    Union,
)

import pandas as pd
import xlrd
from numpy.typing import NDArray
from pandas.core.dtypes.common import is_numeric_dtype
from xlrd.sheet import Cell

from .battery_exceptions import EmptyFileError
from .mappings import COLUMN_NAME_MAPPING
from .parsing_engines_base import ParsingEngineBase


class MaccorXLSParser(ParsingEngineBase):
    """
    ParserBase for Maccor excel raw data
    Based on maccor_functions by Luke Pitt
    """

    name = "maccor"
    description = "Maccor XLS/XLSX"
    valid: List[Tuple[str, str]] = [
        ("application/vnd.ms-excel", ".xls"),
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".xlsx"),
    ]
    MANDATORY_COLUMNS = {"Cyc#", "Step"}

    def __init__(self, file_path: str) -> None:
        """Initialises the XLS parser for Maccor"""
        super().__init__(file_path)
        workbook = xlrd.open_workbook(file_path, on_demand=True)
        self.sheet = workbook.sheet_by_index(0)
        self.datemode = workbook.datemode

        self.skip_rows = self._get_header_size()
        self.data = self._load_data()

        # Some preprocessing that can be done straight away
        self._drop_unnamed_columns()
        self._standardise_columns()
        self._create_rec_no()

    def _get_metadata_value(
        self, idx: int, row: Sequence[Cell]
    ) -> Tuple[str, str, int]:
        """A wrapper for metadata value parsing, handling special cases.

        Args:
            idx (int): Index of the cell with the next key to check
            row (Sequence[Cell]): Row of cells

        Raises:
            ValueError: If the index of the next cell is not bigger than the current
                one.

        Returns:
            Tuple[str, str, int]: A tuple with the processed key, value and the next
            index to check.
        """
        key = row[idx]
        if not key:
            key = ""
        elif isinstance(key.value, Text):
            key = key.value.replace("''", "'").strip().rstrip(":")
        else:
            key = key.value

        if "Date" in key:
            value = xlrd.xldate.xldate_as_datetime(row[idx + 1].value, self.datemode)
            new_idx = idx + 2
        elif "Procedure" in key:
            value = (
                clean_value(row[idx + 1].value) + ", " + clean_value(row[idx + 2].value)
            )
            new_idx = idx + 3
        else:
            value = row[idx + 1].value if idx + 1 < len(row) else ""
            new_idx = idx + 2

        if new_idx <= idx:
            raise ValueError(
                "Non-increasing index number when processing metadata cells."
            )
        return key, value, new_idx

    def _get_header_size(self) -> int:
        """Reads the file and determines the size of the header.

        Returns:
            Header size as an int
        """
        for i, row in enumerate(self.sheet.get_rows()):
            if not is_metadata_row(row, self.MANDATORY_COLUMNS):
                return i
        return 0

    def _load_data(self) -> pd.DataFrame:
        """Loads the data as a Pandas data frame.

        Returns:
            A pandas dataframe with all the data.
        """
        data = pd.read_excel(
            self.file_path, sheet_name=None, header=self.skip_rows, index_col=None
        )

        if isinstance(data, dict):
            data = pd.concat(data.values(), ignore_index=True)

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

    def _get_file_header(self) -> Dict[str, Any]:
        """Extracts the header from the Maccor file.

        The header is spread across columns, so these need to be scan for the key/value
        pairs to extract.

        Returns:
            A dictionary with the header information.
        """
        if self.sheet.ncols < 1 or self.sheet.nrows < 2:
            raise EmptyFileError()

        header: Dict[str, Any] = {}
        for i, row in enumerate(self.sheet.get_rows()):
            if i == self.skip_rows:
                break

            current = 0
            while current < len(row):
                key, value, current = self._get_metadata_value(current, row)
                if key == "":
                    continue
                header[key] = value

        return header

    def get_metadata(self) -> Dict[str, Any]:
        """Puts together the metadata for the file

        Raises:
            EmptyFileError: If the file is found to be empty.

        Returns:
            Dict[str, Any]: A dictionary with the metadata
        """
        if self.sheet.ncols < 1 or self.sheet.nrows < 2:
            raise EmptyFileError()

        metadata: Dict[str, Any] = {
            "Dataset_Name": self.file_path.stem,
            "dataset_size": self.file_path.stat().st_size,
            "num_rows": len(self.data),
            "data_start": self.skip_rows,
            "first_sample_no": self.skip_rows + 1,
            "file_metadata": self._get_file_header(),
            "Machine Type": "Maccor",
            "warnings": [],
        }

        if not self.MANDATORY_COLUMNS.issubset(self.data.columns):
            metadata["warnings"].append(
                "Not all mandatory columns are present in the raw datafile"
            )

        return metadata

    def get_data_generator_for_columns(
        self, columns: List, first_data_row: int = 0, col_mapping: Optional[Dict] = None
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

    @staticmethod
    def _sanitise_rec_val(value) -> float:
        if isinstance(value, str):
            return float(value.replace(",", ""))
        else:
            return value


def clean_value(value: str) -> str:
    """Cleans up the string and trims special characters.

    Args:
        value (str): The string to clean

    Returns:
        str: The string cleaned.
    """
    return value.replace("''", "'").strip().rstrip("\0").strip()


def is_metadata_row(row: Iterable, withnesses: Iterable) -> bool:
    """Checks if a row is a metadata row.

    Args:
        row (Iterable): Iterable with the row data to check
        withnesses (Iterable): Iterable with the elements to check that would identify
            this as NOT a metadata row.

    Returns:
        bool: True if it is identified as a metadata row
    """
    row_values = [y.value if hasattr(y, "value") else y for y in row]
    return not any(x in withnesses for x in row_values)
