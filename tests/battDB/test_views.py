from datetime import datetime

from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

import battDB.models as bdb


class CreateDeviceSpecificationTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contribpass")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)

    def test_can_see_parameter_formset(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        response = self.client.get(reverse("battDB:New Device"))
        self.assertContains(
            response,
            '<select name="deviceparameter_set-0-parameter" class="select form-select" id="id_deviceparameter_set-0-parameter">',
        )
        self.assertContains(
            response,
            '<input type="text" name="deviceparameter_set-0-value" value="null" class="textinput textInput form-control" id="id_deviceparameter_set-0-value">',
        )
        self.assertContains(
            response,
            '<select name="deviceparameter_set-0-material" class="select form-select" id="id_deviceparameter_set-0-material">',
        )

    def test_create_update_devices(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Create new abstract device spec.
        abstract_response = self.client.post(
            reverse("battDB:New Device"),
            {
                "name": "Abstract device",
                "abstract": True,
            },
        )
        self.assertEqual(abstract_response.status_code, 302)
        self.assertEqual(abstract_response.url, "/battDB/new_device/")
        abstract_device = bdb.DeviceSpecification.objects.get(name="Abstract device")
        self.assertTrue(abstract_device.abstract)
        self.assertEqual(abstract_device.status, "private")

        # Create new device spec.
        response = self.client.post(
            reverse("battDB:New Device"),
            {
                "name": "Actual device",
                "abstract": False,
                "device_type": abstract_device.id,
                "notes": "Some notes",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/battDB/new_device/")
        device = bdb.DeviceSpecification.objects.get(name="Actual device")
        self.assertFalse(device.abstract)
        self.assertEqual(device.user_owner.username, "test_contributor")
        self.assertEqual(device.status, "private")

        # Update device spec.
        update_response = self.client.post(
            reverse("battDB:Update Device", kwargs={"pk": device.id}),
            {
                "name": "Actual device",
                "abstract": False,
                "make_public": True,
                "device_type": abstract_device.id,
                "notes": "Some other notes",
            },
        )
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.url, "/battDB/devices/")

        device.refresh_from_db()
        self.assertEqual(device.status, "public")
        self.assertEqual(device.notes, "Some other notes")


class CreateEquipmentTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contribpass")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)

        self.institution = baker.make_recipe("tests.common.org")

    def test_create_update_equipment(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Create new equipment
        response = self.client.post(
            reverse("battDB:New Equipment"),
            {
                "name": "A cycler",
                "institution": self.institution.id,
                "serialNo": "abc-123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/battDB/new_equipment/")
        equipment = bdb.Equipment.objects.get(name="A cycler")
        self.assertEqual(equipment.user_owner.username, "test_contributor")
        self.assertEqual(equipment.status, "private")
        self.assertEqual(equipment.serialNo, "abc-123")

        # Update equipment
        update_response = self.client.post(
            reverse("battDB:Update Equipment", kwargs={"pk": equipment.id}),
            {
                "name": "A different cycler",
                "institution": self.institution.id,
                "serialNo": equipment.serialNo,
            },
        )
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.url, "/battDB/equipment/")

        equipment.refresh_from_db()
        self.assertEqual(equipment.name, "A different cycler")


class CreateBatchTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contribpass")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)

        self.institution = baker.make_recipe("tests.common.org")
        self.specification = baker.make_recipe(
            "tests.battDB.device_specification", abstract=False
        )

    def test_create_update_batch(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Create new batch
        response = self.client.post(
            reverse("battDB:New Batch"),
            {
                "manufactured_on": "01/01/2022",
                "manufacturer": self.institution.id,
                "batch_size": 10,
                "serialNo": "abc-123",
                "specification": self.specification.id,
            },
        )
        print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/battDB/new_batch/")
        batch = bdb.Batch.objects.get(serialNo="abc-123")
        self.assertEqual(batch.user_owner.username, "test_contributor")
        self.assertEqual(batch.status, "private")
        self.assertEqual(batch.serialNo, "abc-123")

        # Update batch
        update_response = self.client.post(
            reverse("battDB:Update Batch", kwargs={"pk": batch.id}),
            {
                "manufactured_on": "01/01/2022",
                "manufacturer": self.institution.id,
                "batch_size": 10,
                "serialNo": "abc-123456",
                "specification": self.specification.id,
            },
        )
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.url, "/battDB/batches/")

        batch.refresh_from_db()
        self.assertEqual(batch.serialNo, "abc-123456")
