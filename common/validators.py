from pathlib import Path

import magic
from django.core.exceptions import ValidationError

from parsers import mime_and_extension


def validate_data_file(file):
    extension = Path(file.path).suffix
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if (file_mime_type, extension) not in mime_and_extension():
        raise ValidationError(
            f"Unsupported file type and/or extension: '{(file_mime_type, extension)}'"
        )
