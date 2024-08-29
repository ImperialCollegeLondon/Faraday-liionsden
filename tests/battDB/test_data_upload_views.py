from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

import battDB.models as bdb

# flake8: noqa: E501


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
            download_response.url.startswith("/uploaded_files/biologic_example"),
        )

    def test_upload_view_biologic_data_2(self):
        """
        Test uploading and parsing of biologic_example_Ewe.tsv.
        """
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
        self.assertNotContains(get_response, "without being processed")

        # Finally, check the raw data file can be downloaded
        # Note: this will currently fail if azure storage isn't used
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        print(download_response.url)
        self.assertTrue(
            download_response.url.startswith("/uploaded_files/biologic_example_Ewe"),
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
            download_response.url.startswith("/uploaded_files/maccor_example_new"),
        )

    def test_upload_view_maccor_data_2(self):
        """
        Test uploading and parsing of maccor_example_discharge_test.xls.
        """
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
        self.assertNotContains(get_response, "without being processed")

        # Finally, check the raw data file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "/uploaded_files/maccor_example_discharge_test"
            ),
        )

    def test_upload_view_maccor_data_3(self):
        """
        Test uploading and parsing of maccor_example_discharge_test.csv.
        """
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
        self.assertNotContains(get_response, "without being processed")

        # Finally, check the raw data file can be downloaded
        download_response = self.client.get(
            reverse("battDB:Download File", kwargs={"pk": edf.id})
        )
        self.assertEqual(download_response.status_code, 302)
        self.assertTrue(
            download_response.url.startswith(
                "/uploaded_files/maccor_example_discharge_test"
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
            download_response.url.startswith("/uploaded_files/sample_binary"),
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
            download_response.url.startswith("/uploaded_files/sample_settings"),
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
            self.client.post(
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
