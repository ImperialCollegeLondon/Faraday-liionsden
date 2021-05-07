from django.test import TestCase


class TestHashFile(TestCase):
    def test_hash_file(self):
        import hashlib
        from pathlib import Path

        from common.utils import hash_file

        f = open(Path(__file__), "rb")
        expected = hashlib.md5(f.read()).hexdigest()
        self.assertEqual(expected, hash_file(f))
