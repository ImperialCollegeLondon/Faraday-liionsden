from unittest.mock import MagicMock

from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from model_bakery import baker

from tests.fixtures import db_user, staff_user

request = MagicMock()
User = get_user_model()


class TestCustomUserAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

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


class TestUserAdminPermissions(TestCase):
    def setUp(self):
        from django.contrib.auth.models import Group

        self.site = AdminSite()
        self.factory = RequestFactory()

        self.user = baker.make_recipe("tests.management.user")
        self.user.is_active = True
        for name in ["Read only", "Contributor", "Maintainer"]:
            group = Group.objects.get(name=name)
            group.user_set.add(self.user)

        self.staff_user = baker.make_recipe("tests.management.user")
        self.staff_user.is_active = True
        self.staff_user.is_staff = True
        user_managers = Group.objects.get(name="User manager")
        user_managers.user_set.add(self.staff_user)

    def test_user_groups(self):
        self.assertFalse(self.user.is_staff)
        self.assertCountEqual(
            [i.name for i in self.user.groups.all()],
            ["Read only", "Contributor", "Maintainer"],
        )
        self.assertCountEqual(
            [i.name for i in self.staff_user.groups.all()], ["User manager"]
        )
        self.assertTrue(self.staff_user.is_staff)

    def test_user_admin_access(self):
        from management.admin import CustomUserAdmin

        ma = CustomUserAdmin(User, self.site)
        test_set = [
            {
                "request": self.staff_user,
                "obj": self.staff_user,
                "disabled": [
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "password",
                ],
            },
            {
                "request": self.staff_user,
                "obj": self.user,
                "disabled": ["is_superuser", "user_permissions", "password"],
            },
            {"request": self.user, "obj": self.staff_user, "disabled": ["password"]},
        ]

        for i in test_set:
            with self.subTest(i):
                request = self.factory.request()
                request.user = i["request"]
                form = ma.get_form(request, obj=i["obj"], change=True)
                self.assertCountEqual(
                    [k for k, v in form.base_fields.items() if v.disabled],
                    i["disabled"],
                )
