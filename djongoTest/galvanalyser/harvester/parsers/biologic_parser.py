import os
import re

import pandas as pd

from abc import ABC
from typing import Set, Dict, Generator

from pandas.core.dtypes.common import is_numeric_dtype

from galvanalyser.harvester.battery_exceptions import UnsupportedFileTypeError
from galvanalyser.harvester.parsers.parser import Parser
from galvanalyser.harvester.parsers.parser_util.biologic import COLUMN_NAME_MAPPING


class BiologicCSVnTSVParser(Parser, ABC):
    """
        Parser for the csv and tsv output of the BioLogic cycler
    """

    MANDATORY_COLUMNS = {'Time', 'Rec#', 'Ns'}

    def __init__(self, file_path: str) -> None:
        """ Initialise the parser and load the data into the Pandas dataframe """
        super().__init__(file_path)
        self.encoding = "iso-8859-1"  # Assumed to be this, but we may need to do something about it
        self.skip_rows = BiologicCSVnTSVParser._get_header_size(file_path, self.encoding)
        self._load_data(file_path)
        # Some preprocessing that could be done straight away
        self._drop_unnamed_columns()
        self._standardise_columns()
        self._create_rec_no()

    def _load_data(self, file_path) -> None:
        """
        Loads the data as a Pandas data frame
        Can work with files that have a header or do not have one
        """
        self.data = pd.read_csv(file_path, ',', engine="python", skiprows=self.skip_rows)
        # If we only have one column, it is likely that data is in tsv
        if len(self.data.keys()) == 1:
            # Read the data as tsv
            self.data = pd.read_csv(file_path, '\t', engine="python", skiprows=self.skip_rows)
        if len(self.data.keys()) == 1:
            # If the data still has only one column, then this is an unsupported filetype
            raise UnsupportedFileTypeError()

    @staticmethod
    def _get_header_size(file_path: str, encoding: str) -> int:
        """
            Reads the file and determines the size of the header
            :return:
                header size --> int
        """
        with open(file_path, encoding=encoding) as datafile:
            if next(datafile) == "BT-Lab ASCII FILE\n":
                return int(re.findall(r"[0-9]+", next(datafile))[0]) - 1
            return 0

    def _create_rec_no(self) -> None:
        """Adds Rec# to the dataset if it was not already present"""
        if "Rec#" not in self.data.keys():
            self.data["Rec#"] = range(len(self.data))

    def _drop_unnamed_columns(self) -> None:
        """Drops columns of the internal parser dataframe that have no name """
        for header in list(self.data):
            if 'Unnam' in header:
                self.data.drop(header, axis=1, inplace=True)

    def _standardise_columns(self) -> None:
        """Standardise column names using the mapping of all known names to the standard name"""
        columns = list(self.data.keys())
        for i, col in enumerate(columns):
            for std_name, all_names in COLUMN_NAME_MAPPING.items():
                if col in all_names:
                    columns[i] = std_name
        self.data.rename(columns=dict(zip(self.data.keys(), columns)), inplace=True)

    def _get_column_info(self) -> Dict:
        """
            Gathers the metadata for each column
            :return:
            column_name: {is_numeric: bool}
        """
        col_metadata = {}
        for k in self.data.keys():
            col_metadata[k] = {
                'is_numeric': is_numeric_dtype(self.data[k]),
                'has_data': True
            }
        return col_metadata

    def get_metadata(self) -> (Dict, Dict):
        """
            :return:
            Dict: Metadata for the dataset (produced by the cycler)
            Dict: Column names, whether they have data and if the data is numeric
        """
        metadata = {
            "Dataset_Name": os.path.splitext(os.path.basename(self.file_path))[0],
            "dataset_size": os.path.getsize(self.file_path),
            "num_rows": len(self.data.index),
            "data_start": self.skip_rows,
            "first_sample_no": self.skip_rows + 1,
            "misc_file_data": {},  # Header for BioLogic, empty dict of naked file
            "warnings": [],
            # Additional metadata could be extracted from the header if needed
        }
        with open(self.file_path, encoding=self.encoding) as f:
            metadata["misc_file_data"] = [f.readline() for _ in range(0, self.skip_rows)]

        column_info = self._get_column_info()

        if not self.MANDATORY_COLUMNS.issubset(self.data.keys()):
            metadata["warnings"].append("Not all mandatory columns are present in the raw datafile")

        return metadata, column_info

    def get_data_generator_for_columns(self, columns: Set, first_data_row: int,
                                       col_mapping: Dict = {}) -> Generator[Dict, None, None]:
        """
        Creates a Generator for accessing all data in a biologic file row by row for the
        specified set of columns. Columns can be renamed if the mapping is passed
        """
        wanted = self.data[list(columns)]  # Get the columns we want
        renamed = wanted.rename(columns=col_mapping, inplace=False)  # Apply renaming
        for row in renamed.to_dict(orient="row"):
            yield row
