from unittest import TestCase, expectedFailure

from django.core.exceptions import ValidationError


class TestDeviceSpecification(TestCase):
    from battDB.models import DeviceSpecification

    model = DeviceSpecification

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "parameters"))
        self.assertTrue(hasattr(self.model, "abstract"))
        self.assertTrue(hasattr(self.model, "complete"))
        self.assertTrue(hasattr(self.model, "device_type"))

    def test_clean(self):
        # These three are ok
        self.model.objects.create().clean()
        obj = self.model.objects.create(abstract=True)
        obj.clean()
        self.model.objects.create(abstract=False, device_type=obj).clean()

        # This is not ok
        with self.assertRaises(ValidationError):
            self.model.objects.create(abstract=True, device_type=obj).clean()


class TestDeviceParameter(TestCase):
    from battDB.models import DeviceParameter

    model = DeviceParameter

    def test_definition(self):
        self.assertTrue(hasattr(self.model, "spec"))
        self.assertTrue(hasattr(self.model, "parameter"))
        self.assertTrue(hasattr(self.model, "material"))
        self.assertTrue(hasattr(self.model, "value"))
        self.assertTrue(hasattr(self.model, "inherit_to_children"))


@expectedFailure
class TestBatch(TestCase):
    pass


@expectedFailure
class TestDevice(TestCase):
    def test_get_used_in_exps(self):
        self.fail()

    def test_last_measured_state_of_health(self):
        self.fail()

    def test_used_in(self):
        self.fail()

    def test_serial(self):
        self.fail()

    def test_clean(self):
        self.fail()


@expectedFailure
class TestDeviceConfig(TestCase):
    pass


@expectedFailure
class TestDeviceConfigNode(TestCase):
    pass


@expectedFailure
class TestParser(TestCase):
    pass


@expectedFailure
class TestEquipment(TestCase):
    pass


@expectedFailure
class TestExperiment(TestCase):
    def test_devices_(self):
        self.fail()

    def test_files_(self):
        self.fail()

    def test_cycles_(self):
        self.fail()

    def test_get_absolute_url(self):
        self.fail()


@expectedFailure
class TestExperimentDataFile(TestCase):
    def test_num_cycles(self):
        self.fail()

    def test_num_ranges(self):
        self.fail()

    def test_file_rows(self):
        self.fail()

    def test_parsed_ranges(self):
        self.fail()

    def test_parsed_columns(self):
        self.fail()

    def test_missing_columns(self):
        self.fail()

    def test_file_columns(self):
        self.fail()

    def test_is_parsed(self):
        self.fail()

    def test_file_exists(self):
        self.fail()

    def test_file_hash(self):
        self.fail()

    def test_create_ranges(self):
        self.fail()

    def test_clean(self):
        self.fail()


@expectedFailure
class TestUploadedFile(TestCase):
    pass


@expectedFailure
class TestExperimentDevice(TestCase):
    def test_get_serial_no(self):
        self.fail()

    def test_clean(self):
        self.fail()


@expectedFailure
class TestDataColumn(TestCase):
    def test_clean(self):
        self.fail()

    def test_experiment(self):
        self.fail()


@expectedFailure
class TestDataRange(TestCase):
    pass


@expectedFailure
class TestSignalType(TestCase):
    pass
