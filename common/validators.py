from pathlib import Path

import magic
from django.core.exceptions import ValidationError

from parsing_engines import mime_and_extension


def validate_data_file(file) -> None:
    """Validates the file against accepted mime types and extensions.

    The (mime type, extension) tuple is checked against all of the combinations
    accepted by the available parsers. Even if no parser is chosen, only files that
    could be accepted by - at least - one of them are valid.

    Args:
        file (FileField): File to validate.

    Raises:
        ValidationError if validation is not passed.
    """
    extension = Path(file.path).suffix
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if (file_mime_type, extension) not in mime_and_extension():
        raise ValidationError(
            f"Unsupported file type and/or extension: '{(file_mime_type, extension)}'"
        )


def validate_pdf_file(file) -> None:
    """Validates the pdf file against the mime type and extension.

    Args:
        file (FileField): File to validate.

    Raises:
        ValidationError if validation not passed.
    """

    extension = Path(file.path).suffix
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if (file_mime_type != "application/pdf") or (extension != ".pdf"):
        raise ValidationError(
            f"Unsupported file type and/or extension - must be a PDF file."
        )
