import logging
import os
from abc import ABC
from typing import Dict, Generator, Iterable, Set

import xlrd
from xlrd.sheet import Cell

from galvanalyser.harvester import battery_exceptions
from galvanalyser.harvester.parsers.parser import Parser


class MaccorXLSParser(Parser, ABC):
    """
    Parser for Maccor excel raw data
    Based on maccor_functions by Luke Pitt
    """

    def __init__(self, file_path: str) -> None:
        """Initialises the XLS parser for Maccor"""
        super().__init__(file_path)
        self.workbook = xlrd.open_workbook(file_path, on_demand=True)
        # Rec# columns in a typical Maccor file, set in get_metadata, used in get_data
        self.rec_col = -1

    @staticmethod
    def clean_value(value: str) -> str:
        """ Trims values """
        return value.replace("''", "'").strip().rstrip("\0").strip()

    def _get_metadata_value(self, key: str, value: Cell) -> str:
        """ A wrapper for metadata value parsing. Handles special cases. """
        if "Date" in key:
            return xlrd.xldate.xldate_as_datetime(value.value, self.workbook.datemode)
        elif "Procedure" in key:
            return self.clean_value(value.value) + "\t" + self.clean_value(value.value)
        else:
            return value.value

    def _identify_columns(self, header_row: int) -> (Dict, Dict):
        """ Parses the file to determine column headers as well as which columns have data """
        sheet = self.workbook.sheet_by_index(0)
        headers = [x.value for x in sheet.row_slice(header_row)]
        column_has_data = [False for _ in range(sheet.ncols)]

        column_is_numeric, numeric_columns = [], []
        val_row = sheet.row_slice(header_row + 1)
        for i in range(sheet.ncols):
            column_is_numeric.insert(i, isinstance(val_row[i].value, float))
            if column_is_numeric[i]:
                numeric_columns.append(i)
            else:
                column_has_data.insert(i, True)

        first_rec = 1
        try:
            self.rec_col = headers.index("Rec#")
            first_rec = sheet.cell_value(header_row + 1, self.rec_col)
        except ValueError:
            pass

        last_rec, total_rows = self._check_columns_for_data(
            column_has_data, headers, numeric_columns, header_row + 1
        )

        return (
            {
                "num_rows": total_rows,
                "first_sample_no": first_rec,
                "last_sample_no": last_rec,
            },
            {
                headers[i]: {
                    "has_data": column_has_data[i],
                    "is_numeric": column_is_numeric[i],
                }
                for i in range(len(headers))
            },
        )

    def _check_columns_for_data(
        self, column_has_data, headers, numeric_columns, data_start
    ):
        """ Scans the entire file for datapoints in each column """
        total_rows, last_rec = 0, 0
        for sheet_id in range(self.workbook.nsheets):
            logging.info("Loading sheet for metadata parsing %d", sheet_id)
            sheet = self.workbook.sheet_by_index(sheet_id)
            total_rows += sheet.nrows - 2
            for col in numeric_columns[:]:
                try:
                    unique_vals = set(
                        [float(x) for x in sheet.col_values(col, data_start)]
                    )
                except (ValueError, IndexError) as e:
                    unique_vals = set()

                unique_vals.discard(0)
                if len(unique_vals) > 0:
                    column_has_data[col] = True
                    numeric_columns.remove(col)
                    logging.info("Found data in col %d", col)

            if sheet.nrows > 2:
                try:
                    last_rec = sheet.cell_value(2, headers.index("Rec#"))
                except ValueError:
                    last_rec = total_rows

            logging.info("Unloading sheet %d", sheet_id)
            self.workbook.unload_sheet(sheet_id)
        return last_rec, total_rows

    @staticmethod
    def _is_metadata_row(row: Iterable) -> bool:
        return not any(x in ["Rec#", "Cyc#", "Step"] for x in [y.value for y in row])

    def get_metadata(self) -> (Dict, Dict):
        sheet = self.workbook.sheet_by_index(0)
        if sheet.ncols < 1 or sheet.nrows < 2:
            raise battery_exceptions.EmptyFileError()

        metadata = {}

        metadata_end = 0
        for row in sheet.get_rows():
            metadata_end += 1
            if self._is_metadata_row(row):
                for key, value in zip(row[::2], row[1::2]):  # Pairwise iteration
                    if not key:
                        continue
                    key = key.value.replace("''", "'").strip().rstrip(":")
                    metadata[key] = self._get_metadata_value(key, value)
            else:
                break

        metadata["Dataset_Name"] = os.path.basename(self.file_path)
        metadata["data_start"] = metadata_end
        metadata["misc_file_data"] = {"excel format metadata": (dict(metadata), None)}
        metadata["Machine Type"] = "Maccor"
        metadata["dataset_size"] = os.path.getsize(self.file_path)
        aggregates, column_info = self._identify_columns(metadata_end - 1)
        metadata.update(aggregates)

        return metadata, column_info

    def get_data_generator_for_columns(
        self, columns: Set, first_data_row: int, col_mapping: Dict = None
    ) -> Generator[Dict, None, None]:
        """
        Creates a generator for accessing all data in a maccor file row by row for the desired
         columns. Can rename columns if a custom mapping is passed.
        """
        sheet = self.workbook.sheet_by_index(0)
        col_names = sheet.row_slice(first_data_row - 1)
        columns_of_interest = [
            i for i in range(sheet.ncols) if col_names[i].value in columns
        ]
        if col_mapping is not None:
            col_names = [col_mapping[x] if x in col_mapping else x for x in col_names]

        for sheet_id in range(self.workbook.nsheets):
            logging.info("Loading sheet for data parsing %d", sheet_id)
            sheet = self.workbook.sheet_by_index(sheet_id)
            for i in range(first_data_row, sheet.nrows):
                row = sheet.row(i)
                yield {
                    col_names[col].value: (
                        row[col].value
                        if self.rec_col != col
                        else self._sanitise_rec_val(row[col].value)
                    )
                    for col in columns_of_interest
                }
            logging.info("Unloading sheet %d", sheet_id)
            self.workbook.unload_sheet(sheet_id)

    @staticmethod
    def _sanitise_rec_val(value) -> float:
        if isinstance(value, str):
            return float(value.replace(",", ""))
        else:
            return value


class MaccorTSVParser(Parser, ABC):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def get_metadata(self) -> None:
        pass


class MaccorCSVParser(Parser, ABC):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def get_metadata(self) -> None:
        pass
