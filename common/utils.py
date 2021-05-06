import hashlib
from functools import partial


def hash_file(file, block_size=65536):
    """Get the hash of a file using MD5.

    Apparently, there is some vulnerability with this, but it is unclear if it is
    relevant for the case of checking a file for corruption.

    https://stackoverflow.com/a/3431835/3778792
    """
    hasher = hashlib.md5()

    file.seek(0)
    for buf in iter(partial(file.read, block_size), b""):
        hasher.update(buf)

    return hasher.hexdigest()
