from pathlib import Path
from types import SimpleNamespace
from typing import Text
from unittest import TestCase


class TestMaccorXLSParser(TestCase):
    file_path = Path(__file__).parent / "maccor_example.xls"

    def setUp(self) -> None:
        self.parser = SimpleNamespace(file_path=self.file_path)
        self.parser.MANDATORY_COLUMNS = {"Cyc#", "Step"}

    def test_get_header_size(self):
        import xlrd

        from parsing_engines import MaccorXLSParser as MP

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        self.parser.sheet = workbook.sheet_by_index(0)
        self.parser.datemode = workbook.datemode
        actual = MP._get_header_size(self.parser)

        expected = 0
        for i, row in enumerate(self.parser.sheet.get_rows()):
            if any(
                [isinstance(cell.value, Text) and "Cyc#" in cell.value for cell in row]
            ):
                expected = i

        self.assertEqual(actual, expected)

    def test_load_data(self):
        import xlrd

        from parsing_engines import MaccorXLSParser as MP

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        self.parser.sheet = workbook.sheet_by_index(0)
        self.parser.datemode = workbook.datemode
        self.parser.skip_rows = MP._get_header_size(self.parser)

        actual = MP._load_data(self.parser)
        self.assertGreater(len(actual.columns), 1)
        self.assertGreater(len(actual), 30)

    def test_create_rec_no(self):
        import xlrd

        from parsing_engines import MaccorXLSParser as MP

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        self.parser.sheet = workbook.sheet_by_index(0)
        self.parser.datemode = workbook.datemode
        self.parser.skip_rows = MP._get_header_size(self.parser)
        self.parser.data = MP._load_data(self.parser)

        self.assertNotIn("Rec#", self.parser.data.columns)
        MP._create_rec_no(self.parser)
        self.assertIn("Rec#", self.parser.data.columns)

    def test_drop_unnamed_columns(self):
        import xlrd

        from parsing_engines import MaccorXLSParser as MP

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        self.parser.sheet = workbook.sheet_by_index(0)
        self.parser.datemode = workbook.datemode
        self.parser.skip_rows = MP._get_header_size(self.parser)
        self.parser.data = MP._load_data(self.parser)

        if sum(self.parser.data.columns.str.contains("^Unnamed")) > 0:
            MP._drop_unnamed_columns(self.parser)
        self.assertEqual(sum(self.parser.data.columns.str.contains("^Unnamed")), 0)

    def test_standardise_columns(self):
        import xlrd

        from parsing_engines import MaccorXLSParser as MP
        from parsing_engines.mappings import COLUMN_NAME_MAPPING

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        self.parser.sheet = workbook.sheet_by_index(0)
        self.parser.datemode = workbook.datemode
        self.parser.skip_rows = MP._get_header_size(self.parser)
        self.parser.data = MP._load_data(self.parser)
        MP._drop_unnamed_columns(self.parser)

        def all_cols(data):
            return sum(
                [COLUMN_NAME_MAPPING.get(c, c) == c for c in data.columns]
            ) == len(data.columns)

        if not all_cols(self.parser.data):
            MP._standardise_columns(self.parser)
        self.assertTrue(all_cols(self.parser.data))

    def test_get_column_info(self):
        from parsing_engines import MaccorXLSParser as MP

        parser = MP(self.file_path)
        cols = parser.get_column_info()
        for c in parser.data.columns:
            self.assertEqual(list(cols[c].keys()), ["is_numeric", "has_data"])

    def test_get_file_header(self):
        from parsing_engines import MaccorXLSParser as MP

        parser = MP(self.file_path)
        header = parser._get_file_header()
        self.assertGreater(len(header), 2)

    def test_get_metadata(self):
        from parsing_engines import MaccorXLSParser as MP

        parser = MP(self.file_path)
        meta = parser.get_metadata()
        cols = parser.get_column_info()

        self.assertEqual(cols, parser.get_column_info())
        self.assertEqual(meta["dataset_name"], self.file_path.stem)
        self.assertEqual(meta["dataset_size"], self.file_path.stat().st_size)
        self.assertEqual(meta["num_rows"], len(parser.data))
        self.assertEqual(meta["data_start"], parser.skip_rows)
        self.assertEqual(meta["first_sample_no"], parser.skip_rows + 1)
        self.assertEqual(meta["file_metadata"], parser._get_file_header())
        self.assertEqual(len(meta["warnings"]), 0)

    def test_get_data_generator_for_columns(self):
        from parsing_engines import MaccorXLSParser as MP

        parser = MP(self.file_path)

        ncols = 5
        cols = parser.data.columns[:ncols]
        actual = list(parser.get_data_generator_for_columns(cols))
        expected = [list(row) for row in parser.data[cols].values]
        self.assertEqual(actual, expected)


class TestMaccorFunctions(TestCase):
    def test_clean_value(self):
        from parsing_engines.maccor_engine import clean_value

        value = " Someone''s dirty string\n\0\n"
        expected = "Someone's dirty string"
        self.assertEqual(clean_value(value), expected)

    def test_is_metadata_row(self):
        from parsing_engines.maccor_engine import is_metadata_row

        row = ["A", "B", "C", "D"]
        withnesses = [1, 2]
        self.assertTrue(is_metadata_row(row, withnesses))

        withnesses = [1, "A"]
        self.assertFalse(is_metadata_row(row, withnesses))

    def test_get_metadata_value(self):
        import xlrd

        from parsing_engines.maccor_engine import get_metadata_value

        row = [None, SimpleNamespace(value=42)]
        expected = "", 42, 2
        self.assertEqual(get_metadata_value(0, row, 0), expected)

        row = [
            SimpleNamespace(value="Question"),
        ]
        expected = "Question", "", 2
        self.assertEqual(get_metadata_value(0, row, 0), expected)

        row = [
            SimpleNamespace(value="Procedure"),
            SimpleNamespace(value="42"),
            SimpleNamespace(value="84"),
        ]
        expected = "Procedure", "42, 84", 3
        self.assertEqual(get_metadata_value(0, row, 0), expected)

        raw_date = 43237
        row = [
            SimpleNamespace(value="Date:"),
            SimpleNamespace(value=raw_date),
        ]
        expected = "Date", xlrd.xldate.xldate_as_datetime(raw_date, 0), 2
        self.assertEqual(get_metadata_value(0, row, 0), expected)
