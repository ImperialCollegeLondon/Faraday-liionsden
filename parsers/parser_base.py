from __future__ import annotations

import abc
from typing import Dict, Generator, List, Optional, Tuple, Type
from warnings import warn

import pandas.errors
from django.core.exceptions import ValidationError

KNOWN_PARSERS: Dict[str, Type[ParserBase]] = {}


class ParserBase(abc.ABC):

    name: str = ""
    description: str = ""

    def __init_subclass__(cls: Type[ParserBase]):
        if len(cls.name) == 0:
            msg = "A ParserBase subclass cannot have an empty attribute 'name'."
            raise ValueError(msg)
        elif cls.name in KNOWN_PARSERS:
            raise ValueError(f"A parser named '{cls.name}' already exists.")
        KNOWN_PARSERS[cls.name] = cls

    @abc.abstractmethod
    def __init__(self, file_path: str) -> None:  # noqa
        pass

    @abc.abstractmethod
    def get_metadata(self) -> (Dict, Dict):
        pass

    @abc.abstractmethod
    def get_data_generator_for_columns(
        self, columns: List, first_data_row: int, col_mapping: Optional[Dict] = None
    ) -> Generator[Dict, None, None]:
        pass


class DummyParser(ParserBase):

    name = "Dummy"
    description = "Dummy parser that does nothing"

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_metadata(self) -> (Dict, Dict):
        return {"num_rows": 0}, {}

    def get_data_generator_for_columns(
        self, columns: List, first_data_row: int, col_mapping: Optional[Dict] = None
    ) -> Generator[Dict, None, None]:
        return iter([])  # noqa


def get_parser(file_format: str) -> Type[ParserBase]:
    """Provides the chosen parser or the Dummy one if none found.

    Args:
        file_format: String indicating the format of the file. Should match one of the
            known parsers.

    Warnings:
        RuntimeWarning if the chosen parser is not found and the Dummy one is provided
            instead.

    Returns:
        The chosen parser for the given file
    """
    parser = KNOWN_PARSERS.get(file_format, None)
    if parser is None:
        warn(f"No parser available for file format {file_format}!", RuntimeWarning)
        parser = DummyParser
    return parser


def available_parsers() -> List[Tuple[str, str]]:
    """Generates a list of available parser names and descriptions.

    Returns:
        A list of tuples with the parser name and its description.
    """
    return [(k, v.description) for k, v in KNOWN_PARSERS.items()]


def parse_data_file(
    file_path: str,
    file_format: str,
    first_data_row: int,
    columns=("time/s", "Ecell/V", "I/mA"),
    col_mapping: Optional[Dict[str, str]] = None,
) -> Dict:
    """Parse a file according to the chosen format

    Args:
        file_path: Path to the file to parse.
        file_format: String indicating the format of the file. Should match one of the
            known parsers.
        first_data_row: First row that contains data.
        columns: Columns that will be retrieved, if possible.
        col_mapping: Mapping of column names to match the standard 'columns' above.

    Raises:
        ValidationError: If the file could not be parsed for some reason.

    Returns:
        A dictionary containing the following keys: 'metadata', 'file_columns',
        'parsed_columns', 'missing_columns', 'total_rows', 'range_config' and 'data'.
    """
    parser = get_parser(file_format)(file_path)

    try:
        metadata, cols = parser.get_metadata()
    except (pandas.errors.ParserError, ValueError) as e:
        raise ValidationError(
            message={"raw_data_file": "File parsing failed: " + str(e)}
        )

    file_columns = list(cols.keys())
    parsed_columns = [c for c in columns if c in file_columns]
    missing_columns = [c for c in columns if c not in file_columns]
    total_rows = metadata.get("num_rows", 0)
    range_config = {"all": {"start": 1, "end": total_rows, "action": "all"}}
    data = parser.get_data_generator_for_columns(
        parsed_columns, first_data_row, col_mapping
    )

    return {
        "metadata": metadata,
        "file_columns": file_columns,
        "parsed_columns": parsed_columns,
        "missing_columns": missing_columns,
        "total_rows": total_rows,
        "range_config": range_config,
        "data": list(data),
    }
