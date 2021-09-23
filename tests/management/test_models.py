from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUser(TestCase):
    def test_user_str(self):
        self.assertEqual(str(User), "<class 'management.models.User'>")


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
