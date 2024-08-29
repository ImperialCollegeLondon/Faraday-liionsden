from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from guardian.shortcuts import get_objects_for_user
from model_bakery import baker

User = get_user_model()


class BaseObjectTest(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.read_only = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Read only").user_set.add(self.read_only)
        self.contributor = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Contributor").user_set.add(self.contributor)
        self.maintainer = baker.make_recipe("tests.management.user")
        Group.objects.get(name="Maintainer").user_set.add(self.maintainer)


class TestCreatePrivate(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.model = baker.make_recipe("tests.dfndb.parameter", status="private")
        self.model_owner = self.model.user_owner
        self.model_owner.is_active = True

    def test_user_perms(self):
        self.assertTrue(
            self.model_owner.has_perms(
                ["dfndb.view_parameter", "dfndb.change_parameter"], self.model
            )
        )
        self.assertFalse(
            self.model_owner.has_perm("dfndb.delete_parameter", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("dfndb.change_parameter", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestCreatePublic(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.model = baker.make_recipe("tests.dfndb.parameter", status="public")
        self.model_owner = self.model.user_owner
        self.model_owner.is_active = True

    def test_user_perms(self):
        self.assertFalse(
            self.model_owner.has_perm("dfndb.change_parameter", self.model)
        )
        self.assertFalse(
            self.model_owner.has_perm("dfndb.delete_parameter", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("dfndb.change_parameter", self.model)
        )

    def test_group_perms(self):
        self.assertIn(
            self.model, get_objects_for_user(self.contributor, "dfndb.view_parameter")
        )
        self.assertNotIn(
            self.model, get_objects_for_user(self.contributor, "dfndb.change_parameter")
        )
        self.assertIn(
            self.model, get_objects_for_user(self.read_only, "dfndb.view_parameter")
        )
        for perm in ["dfndb.change_parameter", "dfndb.delete_parameter"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestPublicToPrivate(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.model = baker.make_recipe("tests.dfndb.parameter", status="public")
        self.model.status = "private"
        self.model.save()
        self.model_owner = self.model.user_owner
        self.model_owner.is_active = True

    def test_user_perms(self):
        self.assertTrue(
            self.model_owner.has_perms(
                ["dfndb.view_parameter", "dfndb.change_parameter"], self.model
            )
        )
        self.assertFalse(
            self.model_owner.has_perm("dfndb.delete_parameter", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("dfndb.change_parameter", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestPublicToDeleted(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.model = baker.make_recipe("tests.dfndb.parameter", status="public")
        self.model.status = "deleted"
        self.model.save()
        self.model_owner = self.model.user_owner

    def test_user_perms(self):
        self.assertFalse(self.model_owner.has_perm("dfndb.view_parameter", self.model))
        self.assertFalse(
            self.model_owner.has_perm("dfndb.change_parameter", self.model)
        )
        self.assertFalse(
            self.model_owner.has_perm("dfndb.delete_parameter", self.model)
        )
        self.assertFalse(
            self.contributor.has_perm("dfndb.change_parameter", self.model)
        )

    def test_group_perms(self):
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertNotIn(
                    self.model, get_objects_for_user(self.contributor, perm)
                )
        for perm in [
            "dfndb.view_parameter",
            "dfndb.change_parameter",
            "dfndb.delete_parameter",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))


class TestObjectNoOwner(BaseObjectTest):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.model = baker.make_recipe("tests.dfndb.compound")

    def test_group_perms(self):
        self.assertIn(
            self.model, get_objects_for_user(self.contributor, "dfndb.view_compound")
        )
        self.assertNotIn(
            self.model, get_objects_for_user(self.contributor, "dfndb.change_compound")
        )
        self.assertIn(
            self.model, get_objects_for_user(self.read_only, "dfndb.view_compound")
        )
        for perm in ["dfndb.change_compound", "dfndb.delete_compound"]:
            with self.subTest(perm):
                self.assertNotIn(self.model, get_objects_for_user(self.read_only, perm))
        for perm in [
            "dfndb.view_compound",
            "dfndb.change_compound",
            "dfndb.delete_compound",
        ]:
            with self.subTest(perm):
                self.assertIn(self.model, get_objects_for_user(self.maintainer, perm))
