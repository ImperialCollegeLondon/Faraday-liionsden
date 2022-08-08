from django.test import TestCase
from model_bakery import baker


class TestSasToken(TestCase):
    def setUp(self):
        from django.core.files.uploadedfile import SimpleUploadedFile

        self.data = SimpleUploadedFile(
            "test_file_for_sas_token.txt", b"file_content", content_type="text/plain"
        )
        self.uploaded_file = baker.make_recipe(
            "tests.battDB.uploaded_file", file=self.data
        )

    def test_generate_sas_token(self):
        from azure.core.exceptions import ResourceNotFoundError

        from management.custom_azure import generate_sas_token

        sas_token = generate_sas_token(self.uploaded_file.file.name)
        self.assertIn("sv=20", sas_token)
        self.assertIn("sig=", sas_token)
        self.assertIn("se=", sas_token)
        self.assertIn("sp=", sas_token)
        self.assertIn("sr=b", sas_token)

        # Need to actually try and access blob properties for this error to be raised
        # Need to rethink how this is implemented in the generate_sa_token function
        # with self.assertRaises(ResourceNotFoundError):
        # sas_token = generate_sas_token("A_non_existent_file.extension")
        # print(sas_token)
