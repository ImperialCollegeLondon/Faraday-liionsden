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
    def test_factory(self, mock_head, mock_data, mock_size, mock_create, mock_drop):
        import pandas as pd

        from parsing_engines import BiologicParsingEngine as BP

        mock_data.return_value = pd.DataFrame()
        mock_size.return_value = 0
        mock_head.return_value = {"answer": 42}

        file_path = Path("biologic_example.csv")

        parser = BP.factory(file_path=file_path)
        mock_drop.assert_called_once()
        mock_create.assert_called_once()
        mock_size.assert_called_once_with(file_path, BP.encoding)
        mock_data.assert_called_once_with(file_path, 0, BP.encoding)
        mock_head.assert_called_once_with(file_path, 0, BP.encoding)
        self.assertEqual(len(parser.data), 0)
        self.assertEqual(parser.name, "Biologic")
        self.assertEqual(parser.skip_rows, 0)
        self.assertEqual(parser.file_path, file_path)
        self.assertEqual(parser.file_metadata, {"answer": 42})


class TestBiologicFunctions(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from django.core.files.base import File
        from model_bakery import baker

        from parsing_engines import BiologicParsingEngine as BP

        uploaded_file = baker.make_recipe("tests.battDB.uploaded_file")
        with open(self.file_path, "rb") as f:
            uploaded_file.file.save("biologic_example.csv", File(f))

        self.parser = SimpleNamespace(file_obj=uploaded_file.file, encoding=BP.encoding)

    def test_get_header_size(self):
        from parsing_engines.biologic_engine import get_header_size

        actual = get_header_size(self.parser.file_obj, encoding="iso-8859-1")

        with self.parser.file_obj.open("rb") as f:
            lines = iter([i.decode("iso-8859-1") for i in f.readlines()])
            for line in lines:
                if "Nb header lines" in line:
                    expected = int(line.strip().split(" ")[-1]) - 1
                    break

        self.assertEqual(actual, expected)

    def test_load_data(self):
        from parsing_engines.biologic_engine import get_header_size, load_biologic_data

        skip_rows = get_header_size(self.parser.file_obj, encoding="iso-8859-1")

        actual = load_biologic_data(
            self.parser.file_obj, skip_rows, encoding="iso-8859-1"
        )
        self.assertGreater(len(actual.columns), 1)
        self.assertGreater(len(actual), 100)

    def test_get_file_header(self):
        from parsing_engines.biologic_engine import get_file_header, get_header_size

        skip_rows = get_header_size(self.parser.file_obj, encoding="iso-8859-1")

        header = get_file_header(self.parser.file_obj, skip_rows, encoding="iso-8859-1")
        self.assertGreaterEqual(len(header), 1)


class TestHeaderToYaml(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from django.core.files.base import File
        from model_bakery import baker

        from parsing_engines import BiologicParsingEngine as BP

        self.uploaded_file = baker.make_recipe("tests.battDB.uploaded_file")
        with open(self.file_path, "rb") as f:
            self.uploaded_file.file.save("biologic_example.csv", File(f))

        self.parser = BP.factory(self.uploaded_file.file)

    def test_header_to_yaml(self):
        from parsing_engines.biologic_engine import header_to_yaml

        with self.uploaded_file.file.open("r") as f:
            header = list(
                filter(
                    len,
                    (f.readline().rstrip() for _ in range(self.parser.skip_rows)),
                )
            )
            header = [i.decode("iso-8859-1") for i in header]
        meta = header_to_yaml(header)
        self.assertLess(len(meta), len(header))
