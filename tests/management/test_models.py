from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker

from tests.fixtures import db_user

User = get_user_model()


class TestUser(TestCase):
    def test_user_model(self):
        from management.models import User

        self.assertIs(User, get_user_model())

    def test_user_perms(self):
        from django.contrib.auth.models import Group

        user = baker.make_recipe("tests.management.user")
        user.is_active = True
        self.assertEqual(len(user.get_all_permissions()), 0)

        user = baker.make_recipe("tests.management.user")
        user.is_active = True
        user.groups.add(Group.objects.get(name="Contributor"))
        self.assertTrue(
            all(i.split(".")[1].startswith("add") for i in user.get_all_permissions())
        )

        user = baker.make_recipe("tests.management.user")
        user.is_active = True
        user.groups.add(Group.objects.get(name="Maintainer"))
        self.assertTrue(
            all(
                i.startswith(("dfndb", "battDB", "common"))
                for i in user.get_all_permissions()
            )
        )

        user = baker.make_recipe("tests.management.user")
        user.is_active = True
        user.groups.add(Group.objects.get(name="User manager"))
        self.assertTrue(
            {
                "management.add_user",
                "management.change_user",
                "management.delete_user",
                "management.view_user",
            }.issubset(user.get_all_permissions())
        )


class TestGroups(TestCase):
    def test_group_names(self):
        from django.contrib.auth.models import Group

        self.assertEqual(
            [i.name for i in Group.objects.all()],
            ["User manager", "Maintainer", "Contributor", "Read only"],
        )

    def test_group_perms(self):
        from django.contrib.auth.models import Group

        grp = Group.objects.get(name="User manager")
        self.assertEqual(
            [i.codename for i in grp.permissions.all()],
            ["add_user", "change_user", "delete_user", "view_user"],
        )

        grp = Group.objects.get(name="Maintainer")
        expected = ["battDB", "dfndb", "common"]
        actual = [i.content_type.app_label for i in grp.permissions.all()]
        self.assertTrue(all(elem in expected for elem in actual))

        grp = Group.objects.get(name="Contributor")
        expected = ["battDB", "dfndb", "common"]
        actual = [i.content_type.app_label for i in grp.permissions.all()]
        self.assertTrue(all(elem in expected for elem in actual))
        self.assertTrue(
            all(i.codename.startswith("add") for i in grp.permissions.all())
        )

        grp = Group.objects.get(name="Read only")
        self.assertEqual(len(grp.permissions.all()), 0)
