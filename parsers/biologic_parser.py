import os
import re
from typing import Dict, Generator

import pandas as pd
import yaml
from pandas.core.dtypes.common import is_numeric_dtype

from .battery_exceptions import UnsupportedFileTypeError
from .parser import Parser

"""
Based on the test_resources/parser_data/BioLogic_full.txt file
Maps all possible column namings to their standard names
"""
COLUMN_NAME_MAPPING = {
    "time/s": ["time", "Time", "time/s"],
    "mode": ["mode"],
    "ox/red": ["ox/red"],
    "error": ["error"],
    "control changes": ["control changes"],
    "Ns changes": ["Ns changes"],
    "counter inc": ["counter inc."],
    "Ns": ["Ns"],
    "I Range": ["I Range"],
    "control/V/mA": ["control/V/mA"],
    "Ecell/V": ["Ecell/V"],
    "I/mA": ["I/mA"],
    "dq/mA_h": ["dq/mA.h"],
    "(Q-Qo)/mA_h": ["(Q-Qo)/mA.h"],
    "Energy/W_h": ["Energy/W.h"],
    "Analog IN 1/V": ["Analog IN 1/V"],  # TODO: Does 1/V change in this context?
    "Analog OUT/V": ["Analog OUT/V"],
    "Energy charge/W_h": ["Energy charge/W.h"],
    "Energy discharge/W_h": ["Energy discharge/W.h"],
    "Capacitance charge/�F": ["Capacitance charge/�F"],
    "Capacitance discharge/�F": ["Capacitance discharge/�F"],
    "x": ["x"],  # TODO: Is this right? What does it mean and can it change?
    "Q discharge/mA_h": ["Q discharge/mA.h"],
    "Q charge/mA_h": ["Q charge/mA.h"],
    "Capacity/mA_h": ["Capacity/mA.h"],
    "Efficiency/%": ["Efficiency/%"],
    "control/V": ["control/V"],
    "control/mA": ["control/mA"],
    "cycle number": ["cycle number"],
    "P/W": ["P/W"],
    "R/Ohm": ["R/Ohm"],
    "Rec#": ["Rec#", "RecNo"],
}


class BiologicCSVnTSVParser(Parser):
    """
    Parser for the csv and tsv output of the BioLogic cycler
    """

    name = "biologic"
    description = "Biologic CSV/TSV/MPT"
    MANDATORY_COLUMNS = {"Time", "Rec#", "Ns"}

    def __init__(self, file_path: str) -> None:
        """ Initialise the parser and load the data into the Pandas dataframe """
        super().__init__(file_path)
        self.encoding = (
            "iso-8859-1"  # Assumed to be this, but we may need to do something about it
        )
        self.skip_rows = BiologicCSVnTSVParser._get_header_size(
            file_path, self.encoding
        )
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
        self.data = pd.read_csv(
            file_path, ",", engine="python", skiprows=self.skip_rows
        )
        # If we only have one column, it is likely that data is in tsv
        if len(self.data.keys()) == 1:
            # Read the data as tsv
            self.data = pd.read_csv(
                file_path, "\t", engine="python", skiprows=self.skip_rows
            )
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
            if "Unnam" in header:
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
                "is_numeric": is_numeric_dtype(self.data[k]),
                "has_data": True,
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
            "file_header": {},  # Header for BioLogic, empty dict of naked file
            "warnings": [],
            # Additional metadata could be extracted from the header if needed
        }
        with open(self.file_path, encoding=self.encoding) as f:
            metadata["file_header"] = [f.readline() for _ in range(0, self.skip_rows)]
        metadata["Device Metadata"] = self.header_to_yaml(
            "".join(metadata["file_header"])
        )

        column_info = self._get_column_info()

        if not self.MANDATORY_COLUMNS.issubset(self.data.keys()):
            metadata["warnings"].append(
                "Not all mandatory columns are present in the raw datafile"
            )

        return metadata, column_info

    def get_data_generator_for_columns(
        self, columns: list, first_data_row: int, col_mapping: Dict = {}
    ) -> Generator[list, None, None]:
        """
        Creates a Generator for accessing all data in a biologic file row by row for the
        specified set of columns. Columns can be renamed if the mapping is passed
        """
        wanted = self.data[columns]  # Get the columns we want
        # renamed = wanted.rename(columns=col_mapping, inplace=False)  # Apply renaming
        # for row in renamed.to_dict(orient="row"):
        for row in wanted.values:
            yield list(row)

    # The format of the BioLogix header is /almost/ parsable directly as YAML
    # We can hack in a few string replacements to make it valid

    yaml_replacements = {
        "\t": "    ",  # tabs form lists. in YAML, tab indents are not valid
        # simple text lines with no colon are not valid - add a colon for some assumed meaning
        "BT-Lab ASCII FILE": "FileType : BT-Lab ASCII FILE",
        "Modulo Bat": "Mode: Modulo Bat",
        "BT-Lab for windows": "BT-Lab for windows : ",
        "Internet server": "Internet server : ",
        "Command interpretor": "Command interpretor : ",
        "for DX =": "DX/DQ : for DX =",
        "Record": "Record : "
        # lines ending in \ are not valid
        # "(.+)\\$" : "\1$"
    }

    # https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python
    def header_to_yaml(self, header):
        regex = re.compile(
            "(%s)" % "|".join(map(re.escape, self.yaml_replacements.keys()))
        )
        rep_header = regex.sub(
            lambda mo: self.yaml_replacements[mo.string[mo.start() : mo.end()]], header
        )
        # quote all values for safety:
        # clean_header = re.sub(r'^([^:]+):\s*(.*)', r'\1:"\2"', rep_header, flags=re.MULTILINE)
        # print(rep_header)
        # Table containg per-column metadata is not parseable as YAML. Skip this for now - find line where it starts, and end there.
        regex = re.compile("^Ns.+")
        # last_parseable_line = [m.start() for m in regex.finditer(rep_header)]

        parseable_lines = []
        for num, line in enumerate(rep_header.split("\n"), 1):
            #    print('%d\t"%s"' % (num,line))
            if regex.match(line) is not None:
                #         print("Stop at line %d" % num)
                break
            parseable_lines.append(line)

        parseable_header = "\n".join(parseable_lines)
        header_data = yaml.safe_load(parseable_header)
        return header_data
