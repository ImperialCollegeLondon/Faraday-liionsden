from types import SimpleNamespace as SName
from unittest import TestCase, skip
from unittest.mock import patch


class TestParsingEngineBase(TestCase):
    def test_abstract_methods(self):
        from parsing_engines.parsing_engines_base import ParsingEngineBase

        expected = {"factory"}
        self.assertEqual(ParsingEngineBase.__abstractmethods__, expected)

    def test_register_subclass(self):
        from parsing_engines.parsing_engines_base import (
            KNOWN_PARSING_ENGINES,
            ParsingEngineBase,
        )

        class WeirdParser(ParsingEngineBase):
            name = "Weird Parser"
            description = "Dummy parser that does nothing"

        self.assertEqual(KNOWN_PARSING_ENGINES["Weird Parser"], WeirdParser)

        # Assert existing parser with same name
        with self.assertRaises(ValueError) as info:

            class SameName(ParsingEngineBase):
                name = "Weird Parser"

        self.assertEqual(
            str(info.exception), "A parsing engine named 'Weird Parser' already exists."
        )

        # Assert no name parser
        with self.assertRaises(ValueError) as info:

            class NoName(ParsingEngineBase):
                name = ""

        self.assertEqual(
            str(info.exception),
            "A ParsingEngineBase subclass cannot have an empty attribute 'name'.",
        )

    def test_create_rec_no(self):
        import pandas as pd

        from parsing_engines.parsing_engines_base import ParsingEngineBase

        engine = SName(data=pd.DataFrame())
        self.assertNotIn("Rec#", engine.data.columns)
        ParsingEngineBase._create_rec_no(engine)
        self.assertIn("Rec#", engine.data.columns)

    def test_drop_unnamed_columns(self):
        import pandas as pd

        from parsing_engines.parsing_engines_base import ParsingEngineBase

        engine = SName(data=pd.DataFrame({"^Unnamed": [1, 2, 3], "Voltage": [4, 5, 6]}))
        self.assertIn("^Unnamed", engine.data.columns)
        ParsingEngineBase._drop_unnamed_columns(engine)
        self.assertNotIn("^Unnamed", engine.data.columns)

    def test_get_column_info(self):
        import pandas as pd

        from parsing_engines.parsing_engines_base import ParsingEngineBase

        engine = SName(
            data=pd.DataFrame({"Voltage": [4, 5, 6], "Trash": [None, None, None]}),
            column_name_mapping={"Voltage": "Volts / V"},
        )
        expected = {
            "Voltage": {
                "is_numeric": True,
                "has_data": True,
            },
            "Trash": {
                "is_numeric": False,
                "has_data": False,
            },
        }
        actual = ParsingEngineBase.get_column_info(engine)
        self.assertEqual(actual, expected)

    def test_get_metadata(self):
        from pathlib import Path

        import pandas as pd
        from django.core.files.base import File

        from parsing_engines.parsing_engines_base import ParsingEngineBase

        filename = Path(__file__)
        with open(filename, "rb") as f:
            file_obj = File(f)
        engine = SName(
            data=pd.DataFrame({"Voltage": [4, 5, 6], "Trash": [None, None, None]}),
            skip_rows=0,
            file_obj=file_obj,
            file_metadata={"temperature": 42},
            name="test",
            mandatory_columns={"Voltage": "V", "Current": "I"},
        )
        expected = {
            "dataset_name": str(filename),
            "dataset_size": filename.stat().st_size,
            "num_rows": 3,
            "data_start": 0,
            "first_sample_no": 1,
            "file_metadata": {"temperature": 42},
            "machine_type": "test",
        }
        actual = ParsingEngineBase.get_metadata(engine)
        for i in expected:
            self.assertEqual(actual[i], expected[i])

        self.assertTrue(len(actual["warnings"]) > 0)
        self.assertIn("mandatory columns", actual["warnings"][0])

    def test_get_data_generator_for_columns(self):
        import pandas as pd

        from parsing_engines.parsing_engines_base import ParsingEngineBase

        engine = SName(
            data=pd.DataFrame(
                {
                    "Voltage": [4, 5, 6],
                    "I / A": [1, 2, 3],
                    "Trash": [None, None, None],
                }
            ),
        )
        actual = ParsingEngineBase.get_data_generator_for_columns(
            engine,
            columns=["Voltage", "I / A"],
        )
        for i, row in enumerate(actual):
            self.assertEqual(row, list(engine.data.loc[i, ["Voltage", "I / A"]].values))

    def test_get_parsed_columns(self):
        from parsing_engines.parsing_engines_base import get_parsed_columns

        parser_columns = ["Volts / V", "I / A"]
        file_columns = ["Voltage", "I / A"]
        col_mapping = {"Voltage": "Volts / V"}
        actual = get_parsed_columns(file_columns, parser_columns, col_mapping)
        expected = (["Volts / V", "I / A"], ["Voltage", "I / A"])
        self.assertEqual(actual, expected)


class TestDummyParsingEngine(TestCase):
    @patch(
        "parsing_engines.parsing_engines_base.DummyParsingEngine._drop_unnamed_columns"
    )
    @patch("parsing_engines.parsing_engines_base.DummyParsingEngine._create_rec_no")
    def test_factory(self, mock_create, mock_drop):
        from django.core.files.base import File

        from parsing_engines.parsing_engines_base import DummyParsingEngine

        parser = DummyParsingEngine.factory(File(b""))
        mock_drop.assert_called_once()
        mock_create.assert_called_once()
        self.assertEqual(len(parser.data), 0)
        self.assertEqual(parser.name, "Dummy")
        self.assertEqual(parser.skip_rows, 0)
        self.assertEqual(type(parser.file_obj), File)
        self.assertEqual(parser.file_metadata, {"num_rows": 0})


class TestFunctions(TestCase):
    def test_get_parser(self):
        from parsing_engines.parsing_engines_base import (
            KNOWN_PARSING_ENGINES,
            DummyParsingEngine,
            get_parsing_engine,
        )

        for file_format, parser in KNOWN_PARSING_ENGINES.items():
            actual = get_parsing_engine(file_format)
            self.assertEqual(actual.name, file_format)
            self.assertEqual(actual, parser)

        with self.assertWarns(RuntimeWarning):
            actual = get_parsing_engine("weird parser")
            self.assertEqual(actual.name, "Dummy")
            self.assertEqual(actual, DummyParsingEngine)

    def test_available_parsers(self):
        from parsing_engines.parsing_engines_base import (
            KNOWN_PARSING_ENGINES,
            available_parsing_engines,
        )

        names = list(KNOWN_PARSING_ENGINES.keys())
        descriptions = [p.description for p in KNOWN_PARSING_ENGINES.values()]
        expected = list(zip(names, descriptions))
        self.assertEqual(expected, available_parsing_engines())

    def test_mime_and_extension(self):
        from itertools import chain

        from parsing_engines.parsing_engines_base import (
            KNOWN_PARSING_ENGINES,
            mime_and_extension,
        )

        descriptions = [p.valid for p in KNOWN_PARSING_ENGINES.values()]
        actual = mime_and_extension()
        for item in chain.from_iterable(descriptions):
            assert item in actual


class TestParseDataFile(TestCase):
    def setUp(self) -> None:
        class MockParser:
            cols = {"time/s": 1, "V": 2}
            metadata = {"num_rows": 150}
            data = [(1, 1), (1, 2)]

            @classmethod
            def factory(cls, file_path):
                return cls(file_path)

            def __init__(self, file_path):
                self.file_path = file_path

            def get_metadata(self):
                return self.metadata

            def get_column_info(self):
                return self.cols

            def get_data_generator_for_columns(self, *args, **kwargs):
                return self.data

        self.mock_parser = MockParser

    @skip("Fix after updating parsers to use file objects not paths")
    @patch("parsing_engines.parsing_engines_base.get_parsing_engine")
    def test_parse_data_file(self, mock_parser):
        mock_parser.return_value = self.mock_parser

        from parsing_engines.parsing_engines_base import parse_data_file

        actual = parse_data_file("some_file.txt", "some format")
        rows = self.mock_parser.metadata["num_rows"]
        self.assertEqual(actual["metadata"], self.mock_parser.metadata)
        self.assertEqual(actual["data"], self.mock_parser.data)
        self.assertEqual(actual["file_columns"], list(self.mock_parser.cols.keys()))
        self.assertEqual(actual["parsed_columns"], ["time/s"])
        self.assertEqual(actual["missing_columns"], ["Ecell/V", "I/mA"])
        self.assertEqual(actual["total_rows"], rows)
        self.assertEqual(
            actual["range_config"], {"all": {"start": 1, "end": rows, "action": "all"}}
        )
