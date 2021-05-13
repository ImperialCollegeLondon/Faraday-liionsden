from unittest import TestCase
from unittest.mock import patch


class TestParserBase(TestCase):
    def test_abstract_methods(self):
        from parsers.parser_base import ParserBase

        expected = {"__init__", "get_metadata", "get_data_generator_for_columns"}
        self.assertEqual(ParserBase.__abstractmethods__, expected)

    def test_register_subclass(self):
        from parsers.parser_base import KNOWN_PARSERS, ParserBase

        class WeirdParser(ParserBase):
            name = "Weird Parser"
            description = "Dummy parser that does nothing"

        self.assertEqual(KNOWN_PARSERS["Weird Parser"], WeirdParser)

        # Assert existing parser with same name
        with self.assertRaises(ValueError) as info:

            class SameName(ParserBase):
                name = "Weird Parser"

        self.assertEqual(
            str(info.exception), "A parser named 'Weird Parser' already exists."
        )

        # Assert no name parser
        with self.assertRaises(ValueError) as info:

            class NoName(ParserBase):
                name = ""

        self.assertEqual(
            str(info.exception),
            "A ParserBase subclass cannot have an empty attribute 'name'.",
        )


class TestDummyParser(TestCase):
    def setUp(self) -> None:
        from parsers.parser_base import DummyParser

        self.parser = DummyParser("")

    def test_get_metadata(self):
        exp_metadata, exp_cols = {"num_rows": 0}, {}
        metadata, cols = self.parser.get_metadata()
        self.assertEqual(metadata, exp_metadata)
        self.assertEqual(cols, exp_cols)

    def test_get_data_generator_for_columns(self):
        self.assertEqual(list(self.parser.get_data_generator_for_columns([], 10)), [])


class TestFunctions(TestCase):
    def test_get_parser(self):
        from parsers.parser_base import KNOWN_PARSERS, DummyParser, get_parser

        for file_format, parser in KNOWN_PARSERS.items():
            actual = get_parser(file_format)
            self.assertEqual(actual.name, file_format)
            self.assertEqual(actual, parser)

        with self.assertWarns(RuntimeWarning):
            actual = get_parser("weird parser")
            self.assertEqual(actual.name, "Dummy")
            self.assertEqual(actual, DummyParser)

    def test_available_parsers(self):
        from parsers.parser_base import KNOWN_PARSERS, available_parsers

        names = list(KNOWN_PARSERS.keys())
        descriptions = [p.description for p in KNOWN_PARSERS.values()]
        expected = list(zip(names, descriptions))
        self.assertEqual(expected, available_parsers())


class TestParseDataFile(TestCase):
    def setUp(self) -> None:
        class MockParser:
            cols = {"time/s": 1, "V": 2}
            metadata = {"num_rows": 150}
            data = [(1, 1), (1, 2)]

            def __init__(self, file_path):
                self.file_path = file_path

            def get_metadata(self):
                return self.metadata, self.cols

            def get_data_generator_for_columns(self, *args, **kwargs):
                return self.data

        self.mock_parser = MockParser

    @patch("parsers.parser_base.get_parser")
    def test_parse_data_file(self, mock_parser):

        mock_parser.return_value = self.mock_parser

        from parsers.parser_base import parse_data_file

        actual = parse_data_file("some_file.txt", "some format", 0)
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
