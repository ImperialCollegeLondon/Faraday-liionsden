from unittest import TestCase
from unittest.mock import patch


class TestParserBase(TestCase):
    def test_abstract_methods(self):
        from parsing_engines.parsing_engines_base import ParsingEngineBase

        expected = {"factory", "_get_file_header"}
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


class TestDummyParser(TestCase):
    def setUp(self) -> None:
        from parsing_engines.parsing_engines_base import DummyParsingEngine

        self.parser = DummyParsingEngine.factory("")

    def test_get_metadata(self):
        metadata = self.parser.get_metadata()
        self.assertEqual(metadata["file_metadata"], {"num_rows": 0})

    def test_get_column_info(self):
        cols = self.parser.get_column_info()
        self.assertEqual(cols, {"Rec#": {"is_numeric": True, "has_data": True}})

    def test_get_data_generator_for_columns(self):
        self.assertEqual(list(self.parser.get_data_generator_for_columns([])), [])


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
