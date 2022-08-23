import shutil
import unittest

from django.core.management.base import BaseCommand
from django.test import TestCase, override_settings
from model_bakery import baker

from tests.fixtures import TEST_AZURE_CONTAINER, TEST_MEDIA_URL


class Command(BaseCommand):
    help = """
    Run the tests that rely on / test the Azure storage backend.
    """

    def handle(self, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestDownloadBlob)
        unittest.TextTestRunner().run(suite)


# Note: It is necessary to override DEFAULT_FILE_STORAGE again for the other overrides
# to fully take effect.
@override_settings(
    AZURE_CONTAINER=TEST_AZURE_CONTAINER,
    MEDIA_URL=TEST_MEDIA_URL,
    DEFAULT_FILE_STORAGE="storages.backends.azure_storage.AzureStorage",
)
class TestDownloadBlob(TestCase):
    def setUp(self):
        from django.core.files.uploadedfile import SimpleUploadedFile

        self.data = SimpleUploadedFile(
            "test_file_for_sas_token.txt", b"file_content", content_type="text/plain"
        )

        self.uploaded_file = baker.make_recipe(
            "tests.battDB.uploaded_file", file=self.data
        )

    def test_download_blob(self):
        import os

        from management.custom_azure import download_blob, generate_sas_token

        blob_name = self.uploaded_file.file.name
        sas_token = generate_sas_token(blob_name)
        download_path = download_blob(
            local_path="./tmp",
            blob_name=blob_name,
            sas_token=sas_token,
        )
        self.assertTrue(os.path.exists(download_path))
        self.assertEqual(open(download_path, "r").read(), "file_content")

    def test_download_blob_not_found(self):
        from logging import getLogger

        from management.custom_azure import download_blob, generate_sas_token

        blob_name = "not_found_file.txt"
        sas_token = generate_sas_token(blob_name)

        with self.assertLogs(logger=getLogger(), level="ERROR") as cm:
            download_blob(
                local_path="./tmp",
                blob_name=blob_name,
                sas_token=sas_token,
            )
            self.assertIn("Could not find blob", cm.output[0])


def tearDownModule():
    """
    Remove the temporary directory folder at the end of the tests and
    delete all the blobs in the testmedia container.
    """
    from management.custom_azure import delete_blobs, list_blobs

    shutil.rmtree("./tmp")
    blobs = list_blobs(TEST_AZURE_CONTAINER)
    delete_blobs(blobs, TEST_AZURE_CONTAINER)
