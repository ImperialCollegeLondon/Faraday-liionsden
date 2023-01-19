import tempfile
from datetime import datetime

from django.contrib.auth.models import Group
from django.test import TestCase, override_settings
from django.urls import reverse
from model_bakery import baker
from override_storage import override_storage

import battDB.models as bdb

# flake8: noqa: E501


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

    def test_can_see_formsets(self):
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
            '<input type="text" name="deviceparameter_set-0-value" value="0.0" class="textinput textInput form-control" id="id_deviceparameter_set-0-value">',
        )
        self.assertContains(
            response,
            '<select name="devicecomponent_set-0-component" class="select form-select" id="id_devicecomponent_set-0-component">',
        )

    def test_create_update_delete_devices(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Create new abstract device spec.
        abstract_device = baker.make_recipe(
            "tests.battDB.device_specification", name="Abstract Device", abstract=True
        )

        # Create new device spec.
        response = self.client.post(
            reverse("battDB:New Device"),
            {
                "name": "Actual device",
                "abstract": False,
                "device_type": abstract_device.id,
                "notes": "Some notes",
                "deviceparameter_set-INITIAL_FORMS": 0,
                "deviceparameter_set-TOTAL_FORMS": 0,
                "devicecomponent_set-INITIAL_FORMS": 0,
                "devicecomponent_set-TOTAL_FORMS": 0,
            },
        )
        device = bdb.DeviceSpecification.objects.get(name="Actual device")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/battDB/devices/{device.id}/")
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
                "deviceparameter_set-INITIAL_FORMS": 0,
                "deviceparameter_set-TOTAL_FORMS": 0,
                "devicecomponent_set-INITIAL_FORMS": 0,
                "devicecomponent_set-TOTAL_FORMS": 0,
            },
        )
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.url, f"/battDB/devices/{device.id}/")

        device.refresh_from_db()
        self.assertEqual(device.status, "public")
        self.assertEqual(device.notes, "Some other notes")

        # Delete device spec.
        delete_response = self.client.post(
            reverse("battDB:Delete Device", kwargs={"pk": device.id})
        )
        # Initially check user cannot delete public entry
        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(
            delete_response.url,
            f"/accounts/login/?next=/battDB/devices/delete/{device.id}/",
        )
        # Set status manually to private and check delete mechanism
        device.status = "private"
        device.save()
        device.refresh_from_db()
        delete_response = self.client.post(
            reverse("battDB:Delete Device", kwargs={"pk": device.id})
        )
        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(delete_response.url, "/battDB/devices/")
        device.refresh_from_db()
        self.assertEqual(device.status, "deleted")


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

    def test_create_update_delete_equipment(self):
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
        equipment = bdb.Equipment.objects.get(name="A cycler")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/battDB/equipment/{equipment.id}/")
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
        self.assertEqual(update_response.url, f"/battDB/equipment/{equipment.id}/")

        equipment.refresh_from_db()
        self.assertEqual(equipment.name, "A different cycler")

        # Delete equipment
        delete_response = self.client.post(
            reverse("battDB:Delete Equipment", kwargs={"pk": equipment.id})
        )
        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(delete_response.url, "/battDB/equipment/")
        equipment.refresh_from_db()
        self.assertEqual(equipment.status, "deleted")


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

        self.institution = baker.make_recipe("tests.common.org", is_mfg_cells=True)
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
        batch = bdb.Batch.objects.get(serialNo="abc-123")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/battDB/batches/{batch.id}/")
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
        self.assertEqual(update_response.url, f"/battDB/batches/{batch.id}/")

        batch.refresh_from_db()
        self.assertEqual(batch.serialNo, "abc-123456")

        # Delete batch
        delete_response = self.client.post(
            reverse("battDB:Delete Batch", kwargs={"pk": batch.id})
        )
        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(delete_response.url, "/battDB/batches/")
        batch.refresh_from_db()
        self.assertEqual(batch.status, "deleted")


class ExperimentViewTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_readonly",
        )
        self.user.is_active = True
        self.user.set_password("readonlypass")
        self.user.save()
        group = Group.objects.get(name="Read only")
        group.user_set.add(self.user)

        self.experiment = baker.make_recipe(
            "tests.battDB.experiment", name="test experiment", status="public"
        )

    def test_table_view(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        response = self.client.get(reverse("battDB:Experiments"))
        self.assertContains(response, "<td >test experiment</td>")

    def test_detail_view(self):
        # check redirect without login
        response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertEqual(
            response.url,
            f"/accounts/login/?next=/battDB/exps/{self.experiment.id}/",
        )

        # login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # check can view
        response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(response, "<h4> test experiment </h4>")


class CreateExperimentTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contribpass")
        self.user.institution = baker.make_recipe("tests.common.org")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)
        self.device_config = baker.make_recipe(
            "tests.battDB.device_config", name="test device config", config_type="expmt"
        )

    def test_create_update_delete_experiment(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contribpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        form_fields = {
            "name": "Experiment 1",
            "date": datetime.now().date(),
            "exp_type": "constant",
            "thermal": "no",
            "summary": "Not long enough",
            "config": self.device_config.id,
            "devices-TOTAL_FORMS": 0,
            "devices-INITIAL_FORMS": 0,
        }

        # Invalid Form (short summary)
        response = self.client.post(reverse("battDB:New Experiment"), form_fields)
        with self.assertRaises(bdb.Experiment.DoesNotExist):
            bdb.Experiment.objects.get()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ensure this value has at least 20 characters")

        # Create new experiment
        form_fields["summary"] = "At least 20 characters"
        response = self.client.post(reverse("battDB:New Experiment"), form_fields)
        experiment = bdb.Experiment.objects.get(name="Experiment 1")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, f"/battDB/exps/{experiment.id}/")
        self.assertEqual(experiment.user_owner.username, "test_contributor")
        self.assertEqual(experiment.user_owner.institution, self.user.institution)
        self.assertEqual(experiment.status, "private")
        self.assertEqual(getattr(experiment, "config").id, form_fields["config"])
        for key, val in form_fields.items():
            if key not in ["config", "devices-TOTAL_FORMS", "devices-INITIAL_FORMS"]:
                self.assertEqual(getattr(experiment, key), val)

        # Create new experiment with same name - should fail
        response = self.client.post(reverse("battDB:New Experiment"), form_fields)
        self.assertEqual(len(bdb.Experiment.objects.all()), 1)
        self.assertEqual(bdb.Experiment.objects.get(name="Experiment 1"), experiment)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, " is already used in your institution")
        self.assertContains(response, form_fields["name"])

        # Update experiment
        form_fields["summary"] = "A longer and more detailed summary"
        update_response = self.client.post(
            reverse("battDB:Update Experiment", kwargs={"pk": experiment.id}),
            form_fields,
        )
        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.url, f"/battDB/exps/{experiment.id}/")

        experiment.refresh_from_db()
        self.assertEqual(experiment.summary, "A longer and more detailed summary")

        # Delete experiment
        delete_response = self.client.post(
            reverse("battDB:Delete Experiment", kwargs={"pk": experiment.id})
        )
        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(delete_response.url, "/battDB/exps/")
        experiment.refresh_from_db()
        self.assertEqual(experiment.status, "deleted")


class DeviceSpecificationViewTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_readonly",
        )
        self.user.is_active = True
        self.user.set_password("readonlypass")
        self.user.save()
        group = Group.objects.get(name="Read only")
        group.user_set.add(self.user)

        self.device = baker.make_recipe(
            "tests.battDB.device_specification", name="test cell", status="public"
        )

    def test_table_view(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        response = self.client.get(reverse("battDB:Devices"))
        self.assertContains(response, "<td >test cell</td>")

    def test_detail_view(self):
        # check redirect without login
        response = self.client.get(
            reverse("battDB:Device", kwargs={"pk": self.device.id})
        )
        self.assertEqual(
            response.url,
            f"/accounts/login/?next=/battDB/devices/{self.device.id}/",
        )

        # login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # check can view
        response = self.client.get(
            reverse("battDB:Device", kwargs={"pk": self.device.id})
        )
        self.assertContains(response, "<h4> test cell </h4>")


class EquipmentViewTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_readonly",
        )
        self.user.is_active = True
        self.user.set_password("readonlypass")
        self.user.save()
        group = Group.objects.get(name="Read only")
        group.user_set.add(self.user)

        self.equipment = baker.make_recipe(
            "tests.battDB.equipment", name="test cycler", status="public"
        )

    def test_table_view(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        response = self.client.get(reverse("battDB:Equipment list"))
        self.assertContains(response, "<td >test cycler</td>")

    def test_detail_view(self):
        # check redirect without login
        response = self.client.get(
            reverse("battDB:Equipment", kwargs={"pk": self.equipment.id})
        )
        self.assertEqual(
            response.url,
            f"/accounts/login/?next=/battDB/equipment/{self.equipment.id}/",
        )

        # login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # check can view
        response = self.client.get(
            reverse("battDB:Equipment", kwargs={"pk": self.equipment.id})
        )
        self.assertContains(
            response, '<td style="text-align:center" ><h4> test cycler </h4></td>'
        )


class BatchViewTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_readonly",
        )
        self.user.is_active = True
        self.user.set_password("readonlypass")
        self.user.save()
        group = Group.objects.get(name="Read only")
        group.user_set.add(self.user)

        self.batch = baker.make_recipe(
            "tests.battDB.batch", serialNo="test-batch", status="public"
        )

    def test_table_view(self):
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        response = self.client.get(reverse("battDB:Batches"))
        self.assertContains(response, "<td >test-batch</td>")

    def test_detail_view(self):
        # check redirect without login
        response = self.client.get(
            reverse("battDB:Batch", kwargs={"pk": self.batch.id})
        )
        self.assertEqual(
            response.url,
            f"/accounts/login/?next=/battDB/batches/{self.batch.id}/",
        )

        # login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_readonly", "password": "readonlypass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # check can view
        response = self.client.get(
            reverse("battDB:Batch", kwargs={"pk": self.batch.id})
        )
        self.assertContains(
            response, '<td style="text-align:center" ><h4> test-batch </h4></td>'
        )


class DataUploadViewTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contributorpass")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)

        self.experiment = baker.make_recipe(
            "tests.battDB.experiment",
            name="test experiment",
            status="public",
            user_owner=self.user,
        )
        self.biologic_parser = bdb.Parser.objects.get(name="Biologic")
        self.maccor_parser = bdb.Parser.objects.get(name="Maccor")

    def test_upload_view_biologic_data(self):
        """
        Test uploading and parsing of biologic_example.csv.
        """
        import os

        from liionsden.settings import settings

        # Login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Check access to view the file upload page
        data_upload_get_response = self.client.get(
            reverse("battDB:New File", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(data_upload_get_response, "Upload the raw data file here.")

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example.csv",
        )
        with open(file_path) as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device Biologic Example",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                    "raw_data_file-0-use_parser": self.biologic_parser.id,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created and parsed
        edf = bdb.ExperimentDataFile.objects.get(name="Device Biologic Example")
        self.assertTrue(edf.file_exists())
        self.assertEqual(len(edf.parsed_columns()), 7)

        # Check Experiment Detail view contains experimental data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "Ecell/V")
        self.assertContains(get_response, "Ns changes")
        self.assertContains(get_response, "19.0")

        # Finally, check the raw data file can be downloaded
        # Note: this will currently fail if azure storage isn't used
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        print(download_response.url)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/biologic_example"
            ),
        )

    def test_upload_view_biologic_data_2(self):
        """
        Test uploading and parsing of biologic_example_Ewe.tsv.
        """
        import os

        from liionsden.settings import settings

        # Login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example_Ewe.tsv",
        )
        with open(file_path) as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device Biologic Example Ewe",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                    "raw_data_file-0-use_parser": self.biologic_parser.id,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created and parsed
        edf = bdb.ExperimentDataFile.objects.get(name="Device Biologic Example Ewe")
        self.assertTrue(edf.file_exists())
        self.assertEqual(len(edf.parsed_columns()), 7)

        # Check Experiment Detail view contains experimental data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "Ecell/V")
        self.assertContains(get_response, "Ewe/V")

        # Finally, check the raw data file can be downloaded
        # Note: this will currently fail if azure storage isn't used
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        print(download_response.url)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/biologic_example_Ewe"
            ),
        )

    def test_upload_view_maccor_data(self):
        """
        Test uploading and parsing of maccor_example.xlsx.
        """
        import os

        from liionsden.settings import settings

        # Login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )
        self.assertEqual(login_response.status_code, 302)
        self.assertEqual(login_response.url, "/")

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/maccor_example_new.xlsx",
        )
        with open(file_path, "rb") as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device Maccor Example",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                    "raw_data_file-0-use_parser": self.maccor_parser.id,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created and parsed
        edf = bdb.ExperimentDataFile.objects.get(name="Device Maccor Example")
        self.assertTrue(edf.file_exists())
        self.assertEqual(len(edf.parsed_columns()), 10)

        # Check Experiment Detail view contains experimental data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "TestTime")
        self.assertContains(get_response, "StepTime")
        self.assertContains(get_response, "3.93")

        # Finally, check the raw data file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/maccor_example_new"
            ),
        )

    def test_upload_view_maccor_data_2(self):
        """
        Test uploading and parsing of maccor_example_discharge_test.xls.
        """
        import os

        from liionsden.settings import settings

        # Login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/maccor_example_discharge_test.xls",
        )
        with open(file_path, "rb") as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device Maccor Example Discharge Test",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                    "raw_data_file-0-use_parser": self.maccor_parser.id,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created and parsed
        edf = bdb.ExperimentDataFile.objects.get(
            name="Device Maccor Example Discharge Test"
        )
        self.assertTrue(edf.file_exists())
        self.assertEqual(len(edf.parsed_columns()), 10)

        # Check Experiment Detail view contains experimental data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "TestTime(s)")
        self.assertContains(get_response, "StepTime(s)")

        # Finally, check the raw data file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/maccor_example_discharge_test"
            ),
        )

    def test_upload_view_maccor_data_3(self):
        """
        Test uploading and parsing of maccor_example_discharge_test.csv.
        """
        import os

        from liionsden.settings import settings

        # Login
        login_response = self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/maccor_example_discharge_test.csv",
        )
        with open(file_path, "rb") as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device Maccor Example Discharge Test",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                    "raw_data_file-0-use_parser": self.maccor_parser.id,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created and parsed
        edf = bdb.ExperimentDataFile.objects.get(
            name="Device Maccor Example Discharge Test"
        )
        self.assertTrue(edf.file_exists())
        self.assertEqual(len(edf.parsed_columns()), 10)

        # Check Experiment Detail view contains experimental data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "TestTime(s)")
        self.assertContains(get_response, "StepTime(s)")

        # Finally, check the raw data file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/maccor_example_discharge_test"
            ),
        )

    def test_upload_view_unparsed_data(self):
        import os

        from liionsden.settings import settings

        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example.csv",
        )
        with open(file_path) as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device 3",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                },
            )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created
        edf = bdb.ExperimentDataFile.objects.get(name="Device 3")
        self.assertTrue(edf.file_exists())

        # Check Experiment Detail view contains message about unparsed data
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(
            get_response, "This file was uploaded without being processed."
        )

    def test_upload_view_binary_file(self):
        import os

        from liionsden.settings import settings

        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example.csv",
        )

        binary_file_path = os.path.join(
            settings.BASE_DIR,
            "tests/common/sample_files/sample_binary.mpr",
        )

        with open(file_path) as input_file:
            with open(binary_file_path, "rb") as binary_file:
                post_response = self.client.post(
                    reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                    {
                        "name": "Device 4",
                        "devices": baker.make_recipe("tests.battDB.device").id,
                        "binary_file": binary_file,
                        "raw_data_file-TOTAL_FORMS": 1,
                        "raw_data_file-INITIAL_FORMS": 0,
                        "raw_data_file-0-file": input_file,
                    },
                )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created
        edf = bdb.ExperimentDataFile.objects.get(name="Device 4")
        self.assertTrue(edf.file_exists())

        # Check Experiment Detail view contains button to download binary file
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "Download binary")

        # Finally, check the binary file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download Binary File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/sample_binary"
            ),
        )

    def test_upload_view_settings_file(self):
        import os

        from liionsden.settings import settings

        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example.csv",
        )

        settings_file_path = os.path.join(
            settings.BASE_DIR,
            "tests/common/sample_files/sample_settings.mps",
        )

        with open(file_path) as input_file:
            with open(settings_file_path, "rb") as settings_file:
                post_response = self.client.post(
                    reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                    {
                        "name": "Device 5",
                        "devices": baker.make_recipe("tests.battDB.device").id,
                        "settings_file": settings_file,
                        "raw_data_file-TOTAL_FORMS": 1,
                        "raw_data_file-INITIAL_FORMS": 0,
                        "raw_data_file-0-file": input_file,
                    },
                )
        # Check redirect to correct page
        self.assertEqual(post_response.url, f"/battDB/exps/{self.experiment.id}")

        # Check ExperimentDataFile has been created
        edf = bdb.ExperimentDataFile.objects.get(name="Device 5")
        self.assertTrue(edf.file_exists())

        # Check Experiment Detail view contains button to download settings file
        get_response = self.client.get(
            reverse("battDB:Experiment", kwargs={"pk": self.experiment.id})
        )
        self.assertContains(get_response, "settings file")

        # Finally, check the settings file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download Settings File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "http://localhost:10000/devstoreaccount1/test/uploaded_files/sample_settings"
            ),
        )

    def test_update_data(self):
        import os

        from liionsden.settings import settings

        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        # Check file upload response
        file_path = os.path.join(
            settings.BASE_DIR,
            "tests/parsing_engines/example_files/biologic_example.csv",
        )
        with open(file_path) as input_file:
            post_response = self.client.post(
                reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
                {
                    "name": "Device 6",
                    "devices": baker.make_recipe("tests.battDB.device").id,
                    "raw_data_file-TOTAL_FORMS": 1,
                    "raw_data_file-INITIAL_FORMS": 0,
                    "raw_data_file-0-file": input_file,
                },
            )
        # Go to update page for this experiment data file
        edf = bdb.ExperimentDataFile.objects.get(name="Device 6")
        update_response = self.client.get(
            reverse("battDB:Update File", kwargs={"pk": edf.id})
        )
        self.assertContains(update_response, "Device 6")

        # Make an update to the form
        updated_post_response = self.client.post(
            reverse("battDB:Update File", kwargs={"pk": edf.id}),
            {
                "name": "Device 6 updated",
                "devices": baker.make_recipe("tests.battDB.device").id,
            },
        )
        self.assertEqual(
            updated_post_response.url, f"/battDB/exps/{self.experiment.id}"
        )
        # Check the name has been updated
        edf = bdb.ExperimentDataFile.objects.get(name="Device 6 updated")
        self.assertTrue(edf.file_exists())
        # Check the original name is no longer in the database
        with self.assertRaises(bdb.ExperimentDataFile.DoesNotExist):
            bdb.ExperimentDataFile.objects.get(name="Device 6")

    def test_invalid_form(self):
        import os

        from liionsden.settings import settings

        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )
        # This is invalid because the raw_data_file formset is missing
        post_response = self.client.post(
            reverse("battDB:New File", kwargs={"pk": self.experiment.id}),
            {
                "name": "Device 7",
                "devices": baker.make_recipe("tests.battDB.device").id,
            },
        )
        # Check redirect to correct page
        self.assertContains(post_response, "Could not save data file - form not valid.")
        # Check ExperimentDataFile has not been created
        with self.assertRaises(bdb.ExperimentDataFile.DoesNotExist):
            bdb.ExperimentDataFile.objects.get(name="Device 7")


class ExperimentDataDeviceTest(TestCase):
    def setUp(self):
        self.user = baker.make_recipe(
            "tests.management.user",
            username="test_contributor",
        )
        self.user.is_active = True
        self.user.set_password("contributorpass")
        self.user.save()
        group = Group.objects.get(name="Contributor")
        group.user_set.add(self.user)

        self.experiment1 = baker.make_recipe(
            "tests.battDB.experiment", user_owner=self.user
        )
        self.experiment2 = baker.make_recipe(
            "tests.battDB.experiment", user_owner=self.user
        )
        self.batch = baker.make_recipe(
            "tests.battDB.batch", batch_size=5, serialNo="abc-123"
        )
        self.experiment_device = baker.make_recipe(
            "tests.battDB.experiment_device",
            experiment=self.experiment1,
            batch=self.batch,
            batch_sequence=1,
        )
        self.experiment_device.clean()

    def test_available_devices(self):
        # Login
        self.client.post(
            "/accounts/login/",
            {"username": "test_contributor", "password": "contributorpass"},
        )

        response = self.client.get(
            reverse("battDB:New File", kwargs={"pk": self.experiment1.id})
        )
        self.assertContains(response, "/abc-123/1")
        response = self.client.get(
            reverse("battDB:New File", kwargs={"pk": self.experiment2.id})
        )
        self.assertNotContains(response, "/abc-123/1")
