from django.test import TestCase
from django.contrib.admin.sites import AdminSite


class MockRequest:
    pass


request = MockRequest()


class TestCustomUserAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_user_str(self):
        from management.admin import CustomUserAdmin
        from management.models import User

        ma = CustomUserAdmin(User, self.site)
        self.assertEqual(str(ma), "management.CustomUserAdmin")

    def test_definition(self):
        from management.admin import CustomUserAdmin
        from management.models import User

        ma = CustomUserAdmin(User, self.site)
        self.assertEqual(ma.model, User)

    def test_list_fields(self):
        from management.admin import CustomUserAdmin
        from management.models import User

        ma = CustomUserAdmin(User, self.site)
        self.assertEqual(
            list(ma.get_list_display(request)),
            ["username", "email", "first_name", "last_name", "is_staff"],
        )
        self.assertEqual(
            list(ma.get_list_filter(request)),
            ["is_staff", "is_superuser", "is_active", "groups"],
        )
