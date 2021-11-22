from pathlib import Path
from unittest import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile


class TestValidators(TestCase):
    def test_validate_data_file(self):
        from django.core.exceptions import ValidationError

        from common.validators import validate_data_file

        with Path(__file__).open("r") as f:
            f.path = Path(__file__)
            with self.assertRaises(ValidationError):
                validate_data_file(f)

        some_data = SimpleUploadedFile(
            "best_file_eva.csv", b"these are the contents of the txt file"
        )

        with some_data.open("r") as f:
            f.path = "best_file_eva.csv"
            validate_data_file(f)
