from pathlib import Path
from types import SimpleNamespace
from typing import Text
from unittest import TestCase
from unittest.mock import MagicMock, patch

from django.core.files.base import File


class TestMaccorXLSParser(TestCase):
    @patch("parsing_engines.MaccorParsingEngine._drop_unnamed_columns")
    @patch("parsing_engines.MaccorParsingEngine._create_rec_no")
    @patch("parsing_engines.maccor_engine.get_header_size")
    @patch("parsing_engines.maccor_engine.load_maccor_data")
    @patch("parsing_engines.maccor_engine.get_file_header")
    @patch("parsing_engines.maccor_engine.factory_xlsx")
    @patch("parsing_engines.maccor_engine.factory_xls")
    def test_factory(
        self,
        mock_xls,
        mock_xlsx,
        mock_head,
        mock_data,
        mock_size,
        mock_create,
        mock_drop,
    ):
        import pandas as pd

        from parsing_engines import MaccorParsingEngine as MP
        from parsing_engines.battery_exceptions import (
            EmptyFileError,
            UnsupportedFileTypeError,
        )

        sheet = SimpleNamespace(ncols=4, nrows=2, max_column=4, max_row=2)
        datemode = 1
        skip_rows = 4
        mock_xls.return_value = sheet, datemode
        mock_xlsx.return_value = sheet, datemode
        mock_data.return_value = pd.DataFrame()
        mock_size.return_value = skip_rows
        mock_head.return_value = {"answer": 42}

        # XLS file
        file_path = Path(__file__).parent / "example_files/maccor_example.xls"
        with open(file_path, "rb") as file_obj:
            parser = MP.factory(file_obj=file_obj)

        mock_xls.assert_called_once()
        mock_xlsx.assert_not_called()
        mock_drop.assert_called_once()
        mock_create.assert_called_once()
        mock_size.assert_called_once_with(sheet, set(MP.mandatory_columns.keys()))
        mock_data.assert_called_once_with(file_obj, skip_rows)
        mock_head.assert_called_once_with(sheet, skip_rows, datemode)
        self.assertEqual(len(parser.data), 0)
        self.assertEqual(parser.name, "Maccor")
        self.assertEqual(parser.skip_rows, skip_rows)
        self.assertEqual(parser.file_obj, file_obj)
        self.assertEqual(parser.file_metadata, {"answer": 42})

        # XLSX file
        file_path = Path(__file__).parent / "example_files/maccor_example_new.xlsx"
        mock_xls.reset_mock()
        mock_xlsx.reset_mock()

        with open(file_path, "rb") as file_obj:
            MP.factory(file_obj=file_obj)

        mock_xlsx.assert_called_once()
        mock_xls.assert_not_called()

        # Empty file
        sheet = SimpleNamespace(max_column=0, max_row=1)
        mock_xlsx.return_value = sheet, datemode
        self.assertRaises(EmptyFileError, MP.factory, file_obj)

        # Unsupported file
        file_obj = File(b"", name="unsupported.file")
        self.assertRaises(UnsupportedFileTypeError, MP.factory, file_obj)


class TestMaccorFunctions(TestCase):

    file_path = Path(__file__).parent / "example_files/maccor_example.xls"

    @patch("xlrd.open_workbook")
    def test_factory_xls(self, mock_open):
        from parsing_engines.maccor_engine import factory_xls

        sheet = "a sheet"
        datemode = 1
        book = SimpleNamespace(
            sheet_by_index=MagicMock(return_value=sheet), datemode=datemode
        )
        mock_open.return_value = book

        with open(self.file_path, "rb") as file_obj:
            sheet, datemode = factory_xls(file_obj)
            self.assertEqual(sheet, sheet)
            self.assertEqual(datemode, datemode)

    @patch("openpyxl.load_workbook")
    def test_factory_xlsx(self, mock_open):
        from parsing_engines.maccor_engine import factory_xlsx

        sheet = "a sheet"
        book = SimpleNamespace(active=sheet)
        mock_open.return_value = book

        with open(self.file_path, "rb") as file_obj:
            sheet, datemode = factory_xlsx(file_obj)
            self.assertEqual(sheet, sheet)
            self.assertEqual(datemode, None)

    def test_get_header_size(self):
        import xlrd

        from parsing_engines.maccor_engine import MaccorParsingEngine, get_header_size

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        sheet = workbook.sheet_by_index(0)
        actual = get_header_size(sheet, MaccorParsingEngine.mandatory_columns)

        expected = 0
        for i, row in enumerate(sheet.get_rows()):
            if any(
                [isinstance(cell.value, Text) and "Cyc#" in cell.value for cell in row]
            ):
                expected = i

        self.assertEqual(actual, expected)

    def test_load_data(self):
        import xlrd

        from parsing_engines.maccor_engine import (
            MaccorParsingEngine,
            get_header_size,
            load_maccor_data,
        )

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        sheet = workbook.sheet_by_index(0)
        skip_rows = get_header_size(sheet, MaccorParsingEngine.mandatory_columns)

        with open(self.file_path, "rb") as file_obj:
            actual = load_maccor_data(file_obj, skip_rows)
            self.assertGreater(len(actual.columns), 1)
            self.assertGreater(len(actual), 30)

    def test_get_file_header(self):
        import xlrd

        from parsing_engines.maccor_engine import (
            MaccorParsingEngine,
            get_file_header,
            get_header_size,
        )

        workbook = xlrd.open_workbook(self.file_path, on_demand=True)
        sheet = workbook.sheet_by_index(0)
        datemode = workbook.datemode
        skip_rows = get_header_size(sheet, MaccorParsingEngine.mandatory_columns)

        header = get_file_header(sheet, skip_rows, datemode)
        self.assertGreater(len(header), 2)

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
        expected = "Date", str(xlrd.xldate.xldate_as_datetime(raw_date, 0)), 2
        self.assertEqual(get_metadata_value(0, row, 0), expected)
