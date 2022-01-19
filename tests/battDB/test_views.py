from django.test import Client, TestCase
from django.urls import reverse
from model_bakery import baker

from battDB.models import Equipment


class EquipmentUpdateTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="super",
            is_superuser=True,
        )
        self.user.set_password("superpass")
        self.user.save()

        self.model = baker.make_recipe(
            "tests.battDB.equipment", name="My Cycler", user_owner=self.user
        )

    def test_owner(self):
        self.assertEqual(self.model.user_owner.username, self.user.username)

    def test_user(self):
        self.assertEqual(self.user.username, "super")
        self.assertTrue(self.user.is_superuser)

    def test_update_equipment(self):
        # Check login OK
        login_response = self.client.post(
            "/accounts/login/", {"username": "super", "password": "superpass"}
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Check initial model name
        self.assertEqual(self.model.name, "My Cycler")

        # Change name and check again
        response = self.client.post(
            reverse("battDB:Update Equipment", kwargs={"pk": self.model.id}),
            {
                "name": "A different cycler",
                "institution": self.model.institution.id,
                "serialNo": self.model.serialNo,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/battDB/equipment/")

        self.model.refresh_from_db()
        self.assertEqual(self.model.name, "A different cycler")
