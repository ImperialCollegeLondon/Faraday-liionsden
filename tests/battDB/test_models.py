from unittest import skip
from unittest.mock import MagicMock

from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker


class TestDeviceSpecification(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.device_specification")
        self.model_abstract = baker.make_recipe(
            "tests.battDB.device_specification", abstract=True
        )
        self.model_defined_type = baker.make_recipe(
            "tests.battDB.device_specification",
            abstract=False,
            device_type=self.model_abstract,
        )
        self.model_abstract_defined_type = baker.make_recipe(
            "tests.battDB.device_specification",
            abstract=True,
            device_type=self.model_abstract,
        )

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "parameters"))
        self.assertTrue(hasattr(self.model, "abstract"))
        self.assertTrue(hasattr(self.model, "complete"))
        self.assertTrue(hasattr(self.model, "device_type"))

    def test_clean(self):
        # These three are ok
        self.model.clean()
        self.model_abstract.clean()
        self.model_defined_type.clean()

        # This is not ok
        with self.assertRaises(ValidationError):
            self.model_abstract_defined_type.clean()


class TestDeviceParameter(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.device_parameter")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "spec"))
        self.assertTrue(hasattr(self.model, "parameter"))
        self.assertTrue(hasattr(self.model, "component"))
        self.assertTrue(hasattr(self.model, "value"))
        self.assertTrue(hasattr(self.model, "inherit_to_children"))


class TestBatch(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.batch")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "specification"))
        self.assertTrue(hasattr(self.model, "manufacturer"))
        self.assertTrue(hasattr(self.model, "serialNo"))
        self.assertTrue(hasattr(self.model, "batch_size"))
        self.assertTrue(hasattr(self.model, "manufacturing_protocol"))
        self.assertTrue(hasattr(self.model, "manufactured_on"))


class TestDevice(TestCase):
    def setUp(self):
        batch = baker.make_recipe("tests.battDB.batch")
        self.model = baker.make_recipe("tests.battDB.device")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "batch"))
        self.assertTrue(hasattr(self.model, "seq_num"))

    def test_get_used_in_exps(self):
        exp = self.model.get_used_in_exps()
        self.assertEqual(len(exp), 0)

    def test_last_measured_state_of_health(self):
        soh = self.model.last_measured_state_of_health()
        self.assertEqual(soh, "Not tested")

        self.model.attributes["state_of_health"] = "100%"
        soh = self.model.last_measured_state_of_health()
        self.assertEqual(soh, self.model.attributes["state_of_health"])

    def test_used_in(self):
        used_in = self.model.used_in()
        self.assertEqual(used_in, "0 Experiments")

    def test_serial(self):
        serial = self.model.serial()
        self.assertEqual(serial.split("/")[-1], f"{self.model.seq_num}")

        self.model.batch.serialNo = "BATT"
        serial = self.model.serial()
        self.assertEqual(serial, f"{self.model.batch.serialNo}/{self.model.seq_num}")

    def test_clean(self):
        self.model.clean()
        self.assertIsNotNone(self.model.attributes.get("state_of_health"))

        self.model.seq_num = 2
        self.assertRaises(ValidationError, self.model.clean)


class TestDeviceConfig(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.device_config")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "devices"))
        self.assertTrue(hasattr(self.model, "config_type"))


class TestDeviceConfigNode(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.device_config_node")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "device"))
        self.assertTrue(hasattr(self.model, "config"))
        self.assertTrue(hasattr(self.model, "device_position_id"))
        self.assertTrue(hasattr(self.model, "pos_netname"))
        self.assertTrue(hasattr(self.model, "neg_netname"))


class TestParser(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.parser")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "file_format"))
        self.assertTrue(hasattr(self.model, "parameters"))


class TestEquipment(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.equipment")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "institution"))
        self.assertTrue(hasattr(self.model, "serialNo"))
        self.assertTrue(hasattr(self.model, "default_parser"))


class TestExperiment(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.experiment")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "date"))
        self.assertTrue(hasattr(self.model, "config"))

    def test_devices_(self):
        num = self.model.devices_()
        self.assertEqual(num, 0)

    def test_files_(self):
        files = self.model.files_()
        self.assertEqual(files, 0)

    def test_cycles_(self):
        cyc = self.model.cycles_()
        self.assertEqual(cyc, "?")

    def test_get_absolute_url(self):
        url = self.model.get_absolute_url()
        self.assertIn("battDB/exps", url)


class TestExperimentDataFile(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.edf")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "ts_headers"))
        self.assertTrue(hasattr(self.model, "ts_data"))
        self.assertTrue(hasattr(self.model, "experiment"))
        self.assertTrue(hasattr(self.model, "machine"))
        self.assertTrue(hasattr(self.model, "devices"))
        self.assertTrue(hasattr(self.model, "protocol"))

    def test_num_cycles(self):
        self.assertEqual(self.model.num_cycles(), 0)

    def test_num_ranges(self):
        self.assertEqual(self.model.num_ranges(), 0)

    def test_file_rows(self):
        self.assertEqual(self.model.file_rows(), 0)

    def test_parsed_ranges(self):
        self.assertEqual(self.model.parsed_ranges(), [])

    def test_parsed_columns(self):
        self.assertEqual(self.model.parsed_columns(), [])

    def test_missing_columns(self):
        self.assertEqual(self.model.missing_columns(), [])

    def test_file_columns(self):
        self.assertEqual(self.model.file_columns(), [])

    def test_is_parsed(self):
        self.assertFalse(self.model.is_parsed())

    def test_file_exists(self):
        self.assertFalse(self.model.file_exists())

    def test_file_hash(self):
        self.assertEqual(self.model.file_hash(), "N/A")

    def test_create_ranges(self):
        """FIXME: A useless tests. Need to come up with a more meaningful one."""
        before = self.model.num_ranges()
        self.model.create_ranges()
        self.assertEqual(self.model.num_ranges(), before)

    def test_clean(self):
        self.model.save = MagicMock()
        self.model.clean()
        self.assertEqual(self.model.name, "Unnamed data set")
        self.model.save.assert_not_called()


class TestUploadedFile(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.uploaded_file")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "edf"))
        self.assertTrue(hasattr(self.model, "local_path"))
        self.assertTrue(hasattr(self.model, "local_date"))
        self.assertTrue(hasattr(self.model, "parse"))
        self.assertTrue(hasattr(self.model, "use_parser"))
        self.assertTrue(hasattr(self.model, "parsed_metadata"))


class TestExperimentDevice(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.experiment_device")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "experiment"))
        self.assertTrue(hasattr(self.model, "batch"))
        self.assertTrue(hasattr(self.model, "batch_sequence"))
        self.assertTrue(hasattr(self.model, "device_position"))
        self.assertTrue(hasattr(self.model, "data_file"))

    @skip("Wait until this is implemented properly before adding tests.")
    def test_get_serial_no(self):
        self.assertRaises(NotImplementedError, self.model.get_serial_no)

    def test_clean(self):
        from battDB.models import Device

        self.assertEqual(Device.objects.count(), 0)
        self.model.clean()
        self.assertEqual(Device.objects.count(), 1)

        self.model.batch_sequence = 42
        self.assertRaises(ValidationError, self.model.clean)


class TestDataColumn(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.data_column")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "resample"))
        self.assertTrue(hasattr(self.model, "resample_n"))
        self.assertTrue(hasattr(self.model, "parameter"))
        self.assertTrue(hasattr(self.model, "device"))

    def test_clean(self):
        self.assertRaises(ValidationError, self.model.clean)

        self.assertEqual(self.model.resample_n, 0)
        self.assertIsNotNone(self.model.parameter)
        self.model.device = None
        self.model.clean()
        self.assertEqual(self.model.resample_n, 1)
        self.assertIsNone(self.model.parameter)

    def test_experiment(self):
        self.assertEqual(self.model.experiment(), self.model.data_file.experiment)


class TestDataRange(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.data_range")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "dataFile"))
        self.assertTrue(hasattr(self.model, "file_offset_start"))
        self.assertTrue(hasattr(self.model, "file_offset_end"))
        self.assertTrue(hasattr(self.model, "label"))
        self.assertTrue(hasattr(self.model, "protocol_step"))
        self.assertTrue(hasattr(self.model, "step_action"))


class TestSignalType(TestCase):
    def setUp(self):
        self.model = baker.make_recipe("tests.battDB.signal_type")

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "parameter"))
        self.assertTrue(hasattr(self.model, "col_name"))
        self.assertTrue(hasattr(self.model, "order"))
        self.assertTrue(hasattr(self.model, "parser"))
