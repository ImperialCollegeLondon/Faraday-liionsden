from functools import partial
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Sequence,
    Set,
    Text,
    Tuple,
    Union,
)

import pandas as pd
import xlrd
from openpyxl import workbook
from xlrd.sheet import Cell, Sheet

from .battery_exceptions import EmptyFileError, UnsupportedFileTypeError
from .parsing_engines_base import ParsingEngineBase


class MaccorParsingEngine(ParsingEngineBase):

    name = "maccor"
    description = "Maccor XLS/XLSX"
    valid: List[Tuple[str, str]] = [
        ("application/vnd.ms-excel", ".xls"),
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".xlsx"),
    ]
    MANDATORY_COLUMNS: Set[str] = {"Cyc#", "Step"}

    @classmethod
    def factory(cls, file_path: Union[Path, str]) -> ParsingEngineBase:
        """Factory method for creating a parsing engine.

        Args:
            file_path (Union[Path, str]): Path to the file to load.
        """
        ext = Path(file_path).suffix.lower()
        if ext == "xls":
            return cls._factory_xls(file_path)
        elif ext == "xlsx":
            return cls._factory_xlsx(file_path)
        else:
            raise UnsupportedFileTypeError(
                "Unknown file extension for Maccor parsing engine '{ext}'."
            )

    @classmethod
    def _factory_xls(cls, file_path: Union[Path, str]) -> ParsingEngineBase:
        """Factory method for creating a parsing engine specific for Maccor XLS files.

        Args:
            file_path (Union[Path, str]): Path to the file to load.
        """
        workbook = xlrd.open_workbook(file_path, on_demand=True)
        sheet = workbook.sheet_by_index(0)

        if sheet.ncols < 1 or sheet.nrows < 2:
            raise EmptyFileError()

        skip_rows = get_header_size_xls(sheet, cls.MANDATORY_COLUMNS)
        data = load_maccor_data(file_path, skip_rows)
        parser = cls(file_path, skip_rows, data)

        parser._get_file_header_internal = partial(
            get_file_header_xls, sheet, workbook.datemode, skip_rows
        )
        return parser

    @classmethod
    def _factory_xlsx(cls, file_path: Union[Path, str]) -> ParsingEngineBase:
        """Factory method for creating a parsing engine specific for Maccor XLSX files.

        Args:
            file_path (Union[Path, str]): Path to the file to load.
        """

    def __init__(self, file_path: Union[Path, str], skip_rows: int, data: pd.DataFrame):
        """Initialises the XLS parser for Maccor"""
        super(MaccorParsingEngine, self).__init__(file_path, skip_rows, data)
        self._get_file_header_internal: Callable[[], Dict[str, Any]]

    def _get_file_header(self) -> Dict[str, Any]:
        """Extracts the header from the Maccor file.

        The header is spread across columns, so these need to be scan for the key/value
        pairs to extract.

        Returns:
            A dictionary with the header information.
        """
        return self._get_file_header_internal()


def get_file_header_xls(sheet: Sheet, datemode: int, skip_rows: int) -> Dict[str, Any]:
    """Extracts the header from the Maccor file.

    The header is spread across columns, so these need to be scan for the key/value
    pairs to extract.

    Args:
        sheet (Sheet): The Excel sheet to scan.
        datemode (int): The mode in whch dates are enconded in the excel file.
        skip_rows (int): Number of rows containing the header.

    Returns:
        Dict[str, Any]: A dictionary with the header information.
    """
    header: Dict[str, Any] = {}
    for i, row in enumerate(sheet.get_rows()):
        if i == skip_rows:
            break

        current = 0
        while current < len(row):
            key, value, current = get_metadata_value(current, row, datemode)
            if key == "":
                continue
            header[key] = value

    return header


def get_header_size_xls(sheet: Sheet, columns: Set) -> int:
    """Reads the file and determines the size of the header.

    Returns:
        Header size as an int
    """
    for i, row in enumerate(sheet.get_rows()):
        if not is_metadata_row(row, columns):
            return i
    return 0


def load_maccor_data(file_path: Union[Path, str], skip_rows: int) -> pd.DataFrame:
    """Loads the data as a Pandas data frame.

    Args:
        file_path (Union[Path, str]): File to load the data from.
        skip_rows (int): Location of the header, assumed equal to the number of rows to
            skip.

    Returns:
        pd.DataFrame: A pandas dataframe with all the data.
    """
    data = pd.read_excel(file_path, sheet_name=None, header=skip_rows, index_col=None)

    if isinstance(data, dict):
        data = pd.concat(data.values(), ignore_index=True)

    return data


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


def get_metadata_value(
    idx: int, row: Sequence[Cell], datemode: int
) -> Tuple[str, str, int]:
    """A wrapper for metadata value parsing, handling special cases.

    Args:
        idx (int): Index of the cell with the next key to check
        row (Sequence[Cell]): Row of cells
        datemode (int): The datemode the cell containing dates are using.

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

    if hasattr(key, "__iter__") and "Date" in key:
        value = xlrd.xldate.xldate_as_datetime(row[idx + 1].value, datemode)
        new_idx = idx + 2
    elif hasattr(key, "__iter__") and "Procedure" in key:
        value = clean_value(row[idx + 1].value) + ", " + clean_value(row[idx + 2].value)
        new_idx = idx + 3
    else:
        value = row[idx + 1].value if idx + 1 < len(row) else ""
        new_idx = idx + 2

    if new_idx <= idx:
        raise ValueError("Non-increasing index number when processing metadata cells.")
    return key, value, new_idx
