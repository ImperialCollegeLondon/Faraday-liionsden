import os
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

    def test_validate_pdf(self):
        from django.core.exceptions import ValidationError

        from common.validators import validate_pdf_file

        with Path(__file__).open("rb") as f:
            f.path = Path(__file__)
            with self.assertRaises(ValidationError):
                validate_pdf_file(f)

        print(os.path.dirname(Path(__file__)))
        with open(
            os.path.join(os.path.dirname(Path(__file__)), "faraday.pdf"), "rb"
        ) as f:
            f.path = "faraday.pdf"
            validate_pdf_file(f)
