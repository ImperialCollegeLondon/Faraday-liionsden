from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase


class TestBiologicCSVnTSVParser(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from parsing_engines import BiologicCSVnTSVParser as BP

        self.parser = SimpleNamespace(file_path=self.file_path, encoding=BP.encoding)

    def test__get_header_size(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        actual = BP._get_header_size(self.parser)

        with open(self.file_path, encoding="iso-8859-1") as f:
            for line in f:
                if "Nb header lines" in line:
                    expected = int(line.strip().split(" ")[-1]) - 1

        self.assertEqual(actual, expected)

    def test__load_data(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        self.parser.skip_rows = BP._get_header_size(self.parser)

        actual = BP._load_data(self.parser)
        self.assertGreater(len(actual.columns), 1)
        self.assertGreater(len(actual), 100)

    def test__create_rec_no(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        self.parser.skip_rows = BP._get_header_size(self.parser)
        self.parser.data = BP._load_data(self.parser)

        self.assertNotIn("Rec#", self.parser.data.columns)
        BP._create_rec_no(self.parser)
        self.assertIn("Rec#", self.parser.data.columns)

    def test__drop_unnamed_columns(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        self.parser.skip_rows = BP._get_header_size(self.parser)
        self.parser.data = BP._load_data(self.parser)

        self.assertGreater(sum(self.parser.data.columns.str.contains("^Unnamed")), 0)
        BP._drop_unnamed_columns(self.parser)
        self.assertEqual(sum(self.parser.data.columns.str.contains("^Unnamed")), 0)

    def test__standardise_columns(self):
        from parsing_engines import BiologicCSVnTSVParser as BP
        from parsing_engines.mappings import COLUMN_NAME_MAPPING

        self.parser.skip_rows = BP._get_header_size(self.parser)
        self.parser.data = BP._load_data(self.parser)
        BP._drop_unnamed_columns(self.parser)

        def all_cols(data):
            return sum(
                [COLUMN_NAME_MAPPING.get(c, c) == c for c in data.columns]
            ) == len(data.columns)

        self.assertFalse(all_cols(self.parser.data))
        BP._standardise_columns(self.parser)
        self.assertTrue(all_cols(self.parser.data))

    def test_get_column_info(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        parser = BP(self.file_path)
        cols = parser.get_column_info()
        for c in parser.data.columns:
            self.assertEqual(list(cols[c].keys()), ["is_numeric", "has_data"])

    def test__get_file_header(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        parser = BP(self.file_path)
        header = parser._get_file_header()
        self.assertGreater(len(header), 2)
        self.assertLess(len(header), parser.skip_rows)

    def test_get_metadata(self):
        from parsing_engines import BiologicCSVnTSVParser as BP
        from parsing_engines.biologic_engine import header_to_yaml

        parser = BP(self.file_path)
        meta = parser.get_metadata()
        cols = parser.get_column_info()

        self.assertEqual(cols, parser.get_column_info())
        self.assertEqual(meta["Dataset_Name"], self.file_path.stem)
        self.assertEqual(meta["dataset_size"], self.file_path.stat().st_size)
        self.assertEqual(meta["num_rows"], len(parser.data))
        self.assertEqual(meta["data_start"], parser.skip_rows)
        self.assertEqual(meta["first_sample_no"], parser.skip_rows + 1)
        self.assertEqual(
            meta["file_metadata"], header_to_yaml(parser._get_file_header())
        )
        self.assertGreater(len(meta["warnings"]), 0)

    def test_get_data_generator_for_columns(self):
        from parsing_engines import BiologicCSVnTSVParser as BP

        parser = BP(self.file_path)

        ncols = 5
        first = 20
        cols = parser.data.columns[:ncols]
        actual = list(parser.get_data_generator_for_columns(cols, first))
        expected = [list(row) for row in parser.data[cols].values[first:]]
        self.assertEqual(actual, expected)


class TestHeaderToYaml(TestCase):
    file_path = Path(__file__).parent / "biologic_example.csv"

    def setUp(self) -> None:
        from parsing_engines import BiologicCSVnTSVParser as BP

        self.parser = BP(self.file_path)

    def test_header_to_yaml(self):
        from parsing_engines.biologic_engine import header_to_yaml, yaml_replacements

        header = self.parser._get_file_header()
        meta = header_to_yaml(header)

        self.assertLess(len(meta), len(header))
        yaml_replacements.pop("\t")
        for v in yaml_replacements.values():
            self.assertIn(v.split(":")[0].strip(), meta)
