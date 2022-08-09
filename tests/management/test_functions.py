import shutil
from unittest import skipIf

from django.conf import settings
from django.test import TestCase, override_settings
from model_bakery import baker
from storages.backends import azure_storage

TEST_AZURE_CONTAINER = "testmedia"
TEST_MEDIA_URL = f"https://{settings.AZURE_CUSTOM_DOMAIN}/{TEST_AZURE_CONTAINER}/"


class TestSasToken(TestCase):
    def test_generate_sas_token(self):
        from management.custom_azure import generate_sas_token

        sas_token = generate_sas_token("test_file_for_sas_token.txt")
        self.assertIn("sv=20", sas_token)
        self.assertIn("sig=", sas_token)
        self.assertIn("se=", sas_token)
        self.assertIn("sp=", sas_token)
        self.assertIn("sr=b", sas_token)


@skipIf(
    settings.DEFAULT_FILE_STORAGE != "storages.backends.azure_storage.AzureStorage",
    "Only run if Azure is used",
)
@override_settings(
    AZURE_CONTAINER=TEST_AZURE_CONTAINER,
    MEDIA_URL=TEST_MEDIA_URL,
    DEFAULT_FILE_STORAGE="storages.backends.azure_storage.AzureStorage",
)
# Note: It is necessary to override DEFAULT_FILE_STORAGE again for the other overrides
# to fully take effect.
class TestDownloadBlob(TestCase):
    @override_settings(AZURE_CONTAINER=TEST_AZURE_CONTAINER)
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
            download_path = download_blob(
                local_path="./tmp",
                blob_name=blob_name,
                sas_token=sas_token,
            )
            self.assertIn("Could not find blob", cm.output[0])


def tearDownModule():
    """
    Remove the temporary directory folder at teh end of the tests and
    delete all the blobs in the testmedia container.
    """
    from management.custom_azure import delete_blobs, list_blobs

    shutil.rmtree("./tmp")
    blobs = list_blobs(TEST_AZURE_CONTAINER)
    delete_blobs(blobs, TEST_AZURE_CONTAINER)
