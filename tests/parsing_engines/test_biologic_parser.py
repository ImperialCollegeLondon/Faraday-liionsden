from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch


class TestBiologicParsingEngine(TestCase):
    @patch("parsing_engines.BiologicParsingEngine._drop_unnamed_columns")
    @patch("parsing_engines.BiologicParsingEngine._create_rec_no")
    @patch("parsing_engines.biologic_engine.get_header_size")
    @patch("parsing_engines.biologic_engine.load_biologic_data")
    @patch("parsing_engines.biologic_engine.get_file_header")
    def test_factory(
        self, mock_head, mock_data, mock_size, mock_create, mock_standard, mock_drop
    ):
        import pandas as pd

        from parsing_engines import BiologicParsingEngine as BP

        mock_data.return_value = pd.DataFrame()
        mock_size.return_value = 0
        mock_head.return_value = {"answer": 42}

        file_path = Path("biologic_example.csv")

        parser = BP.factory(file_path=file_path)
        mock_drop.assert_called_once()
        mock_standard.assert_called_once()
        mock_create.assert_called_once()
        mock_size.assert_called_once_with(file_path, BP.encoding)
        mock_data.assert_called_once_with(file_path, 0, BP.encoding)
        mock_head.assert_called_once_with(file_path, 0, BP.encoding)
        self.assertEqual(len(parser.data), 0)
        self.assertEqual(parser.name, "biologic")
        self.assertEqual(parser.skip_rows, 0)
        self.assertEqual(parser.file_path, file_path)
        self.assertEqual(parser.file_metadata, {"answer": 42})


class TestBiologicFunctions(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from parsing_engines import BiologicParsingEngine as BP

        self.parser = SimpleNamespace(file_path=self.file_path, encoding=BP.encoding)

    def test_get_header_size(self):
        from parsing_engines.biologic_engine import get_header_size

        actual = get_header_size(self.parser.file_path, encoding="iso-8859-1")

        with open(self.file_path, encoding="iso-8859-1") as f:
            for line in f:
                if "Nb header lines" in line:
                    expected = int(line.strip().split(" ")[-1]) - 1
                    break

        self.assertEqual(actual, expected)

    def test_load_data(self):
        from parsing_engines.biologic_engine import get_header_size, load_biologic_data

        skip_rows = get_header_size(self.parser.file_path, encoding="iso-8859-1")

        actual = load_biologic_data(
            self.parser.file_path, skip_rows, encoding="iso-8859-1"
        )
        self.assertGreater(len(actual.columns), 1)
        self.assertGreater(len(actual), 100)

    def test_get_file_header(self):
        from parsing_engines.biologic_engine import get_file_header, get_header_size

        skip_rows = get_header_size(self.parser.file_path, encoding="iso-8859-1")

        header = get_file_header(
            self.parser.file_path, skip_rows, encoding="iso-8859-1"
        )
        self.assertGreaterEqual(len(header), 1)


class TestHeaderToYaml(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from parsing_engines import BiologicParsingEngine as BP

        self.parser = BP.factory(self.file_path)

    def test_header_to_yaml(self):
        from parsing_engines.biologic_engine import header_to_yaml, yaml_replacements

        with open(self.parser.file_path, encoding=self.parser.encoding) as f:
            header = list(
                filter(
                    len,
                    (f.readline().strip("\n") for _ in range(self.parser.skip_rows)),
                )
            )
        meta = header_to_yaml(header)

        self.assertLess(len(meta), len(header))
        yaml_replacements.pop("\t")
        for v in yaml_replacements.values():
            self.assertIn(v.split(":")[0].strip(), meta)
