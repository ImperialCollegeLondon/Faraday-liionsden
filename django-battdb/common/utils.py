import hashlib
from functools import partial
from django.db.models import FileField

def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)
    return hasher.hexdigest()


def file_cleanup(sender, **kwargs):
    field = sender.file
    if field and isinstance(field, FileField):
        field.storage.delete()
