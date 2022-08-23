from __future__ import annotations

import abc
import functools
from typing import Any, Dict, Generator, List, Optional, TextIO, Tuple, Type, Union
from warnings import warn

import pandas as pd
import pandas.errors
from django.core.exceptions import ValidationError
from pandas.core.dtypes.common import is_numeric_dtype

KNOWN_PARSING_ENGINES: Dict[str, Type[ParsingEngineBase]] = {}
"""Registry of the known parsing engines."""


class ParsingEngineBase(abc.ABC):

    name: str = ""
    description: str = ""
    valid: List[Tuple[str, str]] = []
    mandatory_columns: Dict[str, Dict[str, Union[str, Tuple[str, str]]]] = {}
    column_name_mapping: Dict[str, str] = dict()

    def __init_subclass__(cls: Type[ParsingEngineBase]):
        if len(cls.name) == 0:
            msg = "A ParsingEngineBase subclass cannot have an empty attribute 'name'."
            raise ValueError(msg)
        elif cls.name in KNOWN_PARSING_ENGINES:
            raise ValueError(f"A parsing engine named '{cls.name}' already exists.")
        KNOWN_PARSING_ENGINES[cls.name] = cls

    @classmethod
    @abc.abstractmethod
    def factory(cls, file_obj: TextIO) -> ParsingEngineBase:
        """Factory method for creating a parsing engine.

        Args:
            file_obj (TextIO): File to parse.
        """
        pass

    def __init__(
        self,
        file_obj: TextIO,
        skip_rows: int,
        data: pd.DataFrame,
        file_metadata: Dict[str, Any],
    ):
        self.file_obj = file_obj
        self.skip_rows = skip_rows
        self.data = data
        self.file_metadata = file_metadata

        self._drop_unnamed_columns()
        self._create_rec_no()

    def _create_rec_no(self) -> None:
        """Adds Rec# to the dataset if it was not already present."""
        if "Rec#" not in self.data.columns:
            self.data["Rec#"] = range(len(self.data))

    def _drop_unnamed_columns(self) -> None:
        """Drops columns of the internal parser dataframe that have no name."""
        cols = [c for c in self.data.columns if "Unnamed" not in c]
        self.data = self.data.loc[:, cols]

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
                "has_data": not self.data[k].isnull().values.all(),
            }
            for k in self.data.columns
        }

    def get_metadata(self) -> Dict[str, Any]:
        """Puts together the metadata for the file

        Raises:
            EmptyFileError: If the file is found to be empty.

        Returns:
            Dict[str, Any]: A dictionary with the metadata
        """
        metadata: Dict[str, Any] = {
            "dataset_name": self.file_obj.name,
            "dataset_size": self.file_obj.size,
            "num_rows": len(self.data),
            "data_start": self.skip_rows,
            "first_sample_no": self.skip_rows + 1,
            "file_metadata": self.file_metadata,
            "machine_type": self.name,
            "warnings": [],
        }

        if not set(self.mandatory_columns.keys()).issubset(self.data.columns):
            metadata["warnings"].append(
                "Not all mandatory columns are present in the raw datafile"
            )

        return metadata

    def get_data_generator_for_columns(
        self, columns: List, col_mapping: Optional[Dict] = None
    ) -> Generator[list, None, None]:
        """Provides the data filtered by the requested columns and a column mapping.

        Args:
            columns (List): Columns of data to provide
            col_mapping (Optional[Dict], optional): Dictionary to map the required
                column names to the Maccor file column names. Defaults to None.

        Raises:
            KeyError if the required columns, after applying the mapping, do not exist
                in the data.

        Returns:
            Generator[Dict, None, None]: A generator that produces each row of the data
                as a list.
        """
        col_mapping = (
            col_mapping if col_mapping is not None else self.column_name_mapping
        )

        cols = [col_mapping.get(c, c) for c in columns] if col_mapping else columns

        for row in self.data[cols].itertuples():
            yield list(row)[1:]


class DummyParsingEngine(ParsingEngineBase):

    name = "Dummy"
    description = "Dummy parsing engine that does nothing"

    @classmethod
    def factory(cls, file_obj: TextIO) -> ParsingEngineBase:
        """Factory method for creating a parsing engine.

        Args:
            file_obj (TextIO): File to parse.
        """
        return cls(
            file_obj=file_obj,
            skip_rows=0,
            data=pd.DataFrame([]),
            file_metadata={"num_rows": 0},
        )


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
        available = list(KNOWN_PARSING_ENGINES.keys())
        warn(
            f"No parser available for file format {file_format}!"
            f"Available parsers are: {available}",
            RuntimeWarning,
        )
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
    file_obj: TextIO,
    file_format: str,
    columns=("time/s", "Ecell/V", "I/mA"),
    col_mapping: Optional[Dict[str, str]] = None,
) -> Dict:
    """Parse a file according to the chosen format. The file is first retrieved from
    blob storage and copied to a local temporary file. After parsing, the temporary
    file is deleted.

    Args:
        file_obj: The file to be parsed.
        file_format: String indicating the format of the file. Should match the name of
        one of the parsers.
        columns: Columns that will be retrieved, if possible.
        col_mapping: Mapping of column names to match the standard 'columns' above.

    Raises:
        ValidationError: If the file could not be parsed for some reason.

    Returns:
        A dictionary containing the following keys: 'metadata', 'file_columns',
        'parsed_columns', 'missing_columns', 'total_rows', 'range_config' and 'data'.
    """

    engine = get_parsing_engine(file_format).factory(file_obj)

    try:
        metadata = engine.get_metadata()
        cols = engine.get_column_info()
    except (pandas.errors.ParserError, ValueError, KeyError) as e:
        raise ValidationError(
            message={"raw_data_file": "File parsing failed: " + str(e)}
        )

    file_columns = list(cols.keys())
    parsed_columns = [c for c in columns if c in file_columns]
    missing_columns = [c for c in columns if c not in file_columns]
    total_rows = metadata.get("num_rows", 0)
    range_config = {"all": {"start": 1, "end": total_rows, "action": "all"}}
    data = engine.get_data_generator_for_columns(parsed_columns, col_mapping)

    return {
        "metadata": metadata,
        "file_columns": file_columns,
        "parsed_columns": parsed_columns,
        "missing_columns": missing_columns,
        "total_rows": total_rows,
        "range_config": range_config,
        "data": list(data),
    }
