from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from guardian.shortcuts import get_objects_for_user
from model_bakery import baker

User = get_user_model()


class TestCreatePrivate(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.batch", status="private")
        self.model_owner = self.model.user_owner
        self.read_only = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Read only").user_set.add(self.read_only)
        self.contributor = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Contributor").user_set.add(self.contributor)
        self.maintainer = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Maintainer").user_set.add(self.maintainer)

    def test_user_perms(self):
        self.assertTrue(
            self.model_owner.has_perms(
                ["battDB.view_batch", "battDB.change_batch"], self.model
            )
        )
        self.assertFalse(self.model_owner.has_perm("battDB.delete_batch", self.model))
        self.assertFalse(self.contributor.has_perm("battDB.change_batch", self.model))

    def test_group_perms(self):
        self.assertNotIn(
            self.model, get_objects_for_user(self.contributor, "battDB.view_batch")
        )
        for perm in ["battDB.view_batch", "battDB.change_batch", "battDB.delete_batch"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in ["battDB.view_batch", "battDB.change_batch", "battDB.delete_batch"]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestCreatePublic(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.batch", status="public")
        self.model_owner = self.model.user_owner
        self.read_only = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Read only").user_set.add(self.read_only)
        self.contributor = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Contributor").user_set.add(self.contributor)
        self.maintainer = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Maintainer").user_set.add(self.maintainer)

    def test_user_perms(self):
        self.assertFalse(self.model_owner.has_perm("battDB.change_batch", self.model))
        self.assertFalse(self.model_owner.has_perm("battDB.delete_batch", self.model))
        self.assertFalse(self.contributor.has_perm("battDB.change_batch", self.model))

    def test_group_perms(self):
        self.assertIn(
            self.model, get_objects_for_user(self.contributor, "battDB.view_batch")
        )
        self.assertNotIn(
            self.model, get_objects_for_user(self.contributor, "battDB.change_batch")
        )
        self.assertIn(
            self.model, get_objects_for_user(self.read_only, "battDB.view_batch")
        )
        for perm in ["battDB.change_batch", "battDB.delete_batch"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in ["battDB.view_batch", "battDB.change_batch", "battDB.delete_batch"]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


# class TestPublicToPrivate(TestCase):

# class TestDelete(TestCase):
