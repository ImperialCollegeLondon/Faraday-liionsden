import hashlib
from functools import partial
import os
from django.core.files.storage import default_storage
from django.db.models import FileField
import psutil

def has_handle(fpath):
    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                if fpath == item.path:
                    return True
        except Exception:
            pass

    return False


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)
    return hasher.hexdigest()



def file_cleanup(sender, **kwargs):
    field = sender.file
    if field and isinstance(field, FileField):
        field.storage.delete()
