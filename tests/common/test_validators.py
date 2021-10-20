import sys
from pathlib import Path
from unittest import TestCase, skipIf


@skipIf(sys.platform != "linux", "Issue with decoding files in non-linux systems")
class TestValidators(TestCase):
    def test_validate_data_file(self):
        from django.core.exceptions import ValidationError

        from common.validators import validate_data_file

        with Path(__file__).open("r") as f:
            f.path = Path(__file__)
            with self.assertRaises(ValidationError):
                validate_data_file(f)

        with (Path(__file__).parent.parent / "parsers" / "biologic_example.csv").open(
            "r"
        ) as f:
            f.path = Path(__file__)
            validate_data_file(f)
