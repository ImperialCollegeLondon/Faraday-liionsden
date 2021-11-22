from django.contrib.auth.models import Group
from django.test import TestCase
from guardian.shortcuts import get_objects_for_user
from model_bakery import baker


class BaseObjectTest(TestCase):
    @classmethod
    def setUpClass(self):
        super(BaseObjectTest, self).setUpClass()
        self.read_only = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Read only").user_set.add(self.read_only)
        self.contributor = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Contributor").user_set.add(self.contributor)
        self.maintainer = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Maintainer").user_set.add(self.maintainer)


class TestCreatePrivate(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super(TestCreatePrivate, self).setUpClass()
        self.model = baker.make_recipe("tests.common.reference", status="private")
        self.model_owner = self.model.user_owner

    def test_user_perms(self):
        self.assertTrue(
            self.model_owner.has_perms(
                ["common.view_reference", "common.change_reference"], self.model
            )
        )
        self.assertFalse(
            self.model_owner.has_perm("common.delete_reference", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("common.change_reference", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestCreatePublic(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super(TestCreatePublic, self).setUpClass()
        self.model = baker.make_recipe("tests.common.reference", status="public")
        self.model_owner = self.model.user_owner

    def test_user_perms(self):
        self.assertFalse(
            self.model_owner.has_perm("common.change_reference", self.model)
        )
        self.assertFalse(
            self.model_owner.has_perm("common.delete_reference", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("common.change_reference", self.model)
        )

    def test_group_perms(self):
        self.assertIn(
            self.model, get_objects_for_user(self.contributor, "common.view_reference")
        )
        self.assertNotIn(
            self.model,
            get_objects_for_user(self.contributor, "common.change_reference"),
        )
        self.assertIn(
            self.model, get_objects_for_user(self.read_only, "common.view_reference")
        )
        for perm in ["common.change_reference", "common.delete_reference"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestPublicToPrivate(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super(TestPublicToPrivate, self).setUpClass()
        self.model = baker.make_recipe("tests.common.reference", status="public")
        self.model.status = "private"
        self.model.save()
        self.model_owner = self.model.user_owner

    def test_user_perms(self):
        self.assertTrue(
            self.model_owner.has_perms(
                ["common.view_reference", "common.change_reference"], self.model
            )
        )
        self.assertFalse(
            self.model_owner.has_perm("common.delete_reference", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("common.change_reference", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestPublicToDeleted(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super(TestPublicToDeleted, self).setUpClass()
        self.model = baker.make_recipe("tests.common.reference", status="public")
        self.model.status = "deleted"
        self.model.save()
        self.model_owner = self.model.user_owner

    def test_user_perms(self):
        self.assertFalse(self.model_owner.has_perm("common.view_reference", self.model))
        self.assertFalse(
            self.model_owner.has_perm("common.change_reference", self.model)
        )
        self.assertFalse(
            self.model_owner.has_perm("common.delete_reference", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("common.change_reference", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "common.view_reference",
            "common.change_reference",
            "common.delete_reference",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestObjectNoOwner(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super(TestObjectNoOwner, self).setUpClass()
        self.model = baker.make_recipe("tests.common.org")

    def test_group_perms(self):
        self.assertIn(
            self.model, get_objects_for_user(self.contributor, "common.view_org")
        )
        self.assertNotIn(
            self.model, get_objects_for_user(self.contributor, "common.change_org")
        )
        self.assertIn(
            self.model, get_objects_for_user(self.read_only, "common.view_org")
        )
        for perm in ["common.change_org", "common.delete_org"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "common.view_org",
            "common.change_org",
            "common.delete_org",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))
