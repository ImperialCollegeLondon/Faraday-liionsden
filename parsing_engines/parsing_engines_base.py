from __future__ import annotations

import abc
import functools
from pathlib import Path
from typing import Dict, Generator, List, Optional, Tuple, Type, Union
from warnings import warn

import pandas.errors
from django.core.exceptions import ValidationError

KNOWN_PARSING_ENGINES: Dict[str, Type[ParsingEngineBase]] = {}
"""Registry of the known parsing engines."""


class ParsingEngineBase(abc.ABC):

    name: str = ""
    description: str = ""
    valid: List[Tuple[str, str]] = []

    def __init_subclass__(cls: Type[ParsingEngineBase]):
        if len(cls.name) == 0:
            msg = "A ParsingEngineBase subclass cannot have an empty attribute 'name'."
            raise ValueError(msg)
        elif cls.name in KNOWN_PARSING_ENGINES:
            raise ValueError(f"A parsing engine named '{cls.name}' already exists.")
        KNOWN_PARSING_ENGINES[cls.name] = cls

    def __init__(self, file_path: Union[Path, str]):
        self.file_path = Path(file_path)

    @abc.abstractmethod
    def get_metadata(self) -> Dict:
        pass

    @abc.abstractmethod
    def get_column_info(self) -> Dict:
        pass

    @abc.abstractmethod
    def get_data_generator_for_columns(
        self, columns: List, first_data_row: int = 0, col_mapping: Optional[Dict] = None
    ) -> Generator[list, None, None]:
        pass


class DummyParsingEngine(ParsingEngineBase):

    name = "Dummy"
    description = "Dummy parsing engine that does nothing"
    valid: List[Tuple[str, str]] = []

    def get_metadata(self) -> Dict:
        return {"num_rows": 0}

    def get_column_info(self) -> Dict:
        return {}

    def get_data_generator_for_columns(
        self, columns: List, first_data_row: int = 0, col_mapping: Optional[Dict] = None
    ) -> Generator[list, None, None]:
        return iter([])  # noqa


def get_parsing_engine(file_format: str) -> Type[ParsingEngineBase]:
    """Provides the chosen parsing engine or the Dummy one if none found.

    Args:
        file_format: String indicating the format of the file. Should match one of the
            known parsing engines.

    Warnings:
        RuntimeWarning if the chosen parsing engine is not found and the Dummy one is
        provided instead.

    Returns:
        The chosen parser for the given file
    """
    parser = KNOWN_PARSING_ENGINES.get(file_format, None)
    if parser is None:
        warn(f"No parser available for file format {file_format}!", RuntimeWarning)
        parser = DummyParsingEngine
    return parser


def available_parsing_engines() -> List[Tuple[str, str]]:
    """Generates a list of available parsing engines names and descriptions.

    Returns:
        A list of tuples with the parser name and its description.
    """
    return [(k, v.description) for k, v in KNOWN_PARSING_ENGINES.items()]


def mime_and_extension() -> List[Tuple[str, str]]:
    """Generates a list of valid mime types and extensions.

    Returns:
        A list of tuples with the mime type and the extension.
    """

    def aggregate(store: List, new: Type[ParsingEngineBase]) -> List:
        return store + new.valid

    return list(
        set(
            functools.reduce(
                aggregate,
                KNOWN_PARSING_ENGINES.values(),
                [],
            )
        )
    )


def parse_data_file(
    file_path: str,
    file_format: str,
    first_data_row: int = 0,
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
    engine = get_parsing_engine(file_format)(file_path)

    try:
        metadata = engine.get_metadata()
        cols = engine.get_column_info()
    except (pandas.errors.ParserError, ValueError) as e:
        raise ValidationError(
            message={"raw_data_file": "File parsing failed: " + str(e)}
        )

    file_columns = list(cols.keys())
    parsed_columns = [c for c in columns if c in file_columns]
    missing_columns = [c for c in columns if c not in file_columns]
    total_rows = metadata.get("num_rows", 0)
    range_config = {"all": {"start": 1, "end": total_rows, "action": "all"}}
    data = engine.get_data_generator_for_columns(
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
