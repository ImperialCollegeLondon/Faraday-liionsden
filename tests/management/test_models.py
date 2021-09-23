from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUser(TestCase):

    def test_user_str(self):
        self.assertEqual(str(User), "<class 'management.models.User'>")