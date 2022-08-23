from django.test import TestCase


class TestSasToken(TestCase):
    def test_generate_sas_token(self):
        from management.custom_azure import generate_sas_token

        sas_token = generate_sas_token("test_file_for_sas_token.txt")
        self.assertIn("sv=20", sas_token)
        self.assertIn("sig=", sas_token)
        self.assertIn("se=", sas_token)
        self.assertIn("sp=", sas_token)
        self.assertIn("sr=b", sas_token)
