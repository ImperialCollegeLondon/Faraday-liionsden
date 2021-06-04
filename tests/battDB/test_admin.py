from unittest import expectedFailure

from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from model_bakery import baker


class MockRequest:
    pass


request = MockRequest()


class TestMaterialCompositionInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceParameterInline
        from battDB.models import DeviceParameter

        ma = DeviceParameterInline(DeviceParameter, self.site)
        self.assertEqual(ma.model, DeviceParameter)
        self.assertEqual(ma.get_extra(request), 1)


class TestDeviceSpecInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceSpecInline
        from battDB.models import DeviceSpecification

        ma = DeviceSpecInline(DeviceSpecification, self.site)
        self.assertEqual(ma.model, DeviceSpecification)
        self.assertEqual(ma.get_extra(request), 1)


class TestDeviceSpecAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import (
            DeviceParameterInline,
            DeviceSpecAdmin,
            DeviceSpecInline,
        )
        from battDB.models import DeviceSpecification

        baker.make("battDB.DeviceSpecification")
        ma = DeviceSpecAdmin(DeviceSpecification, self.site)
        self.assertEqual(ma.model, DeviceSpecification)
        for d in ["device_type", "abstract", "complete"]:
            self.assertIn(d, ma.get_list_display(request))
            self.assertIn(d, ma.get_list_filter(request))
        self.assertEqual(
            ma.get_inlines(request, DeviceSpecification.objects.get()),
            [DeviceSpecInline, DeviceParameterInline],
        )


class TestDeviceInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceInline
        from battDB.models import Device

        ma = DeviceInline(Device, self.site)
        self.assertEqual(ma.model, Device)
        self.assertEqual(ma.get_extra(request), 0)
        self.assertEqual(
            ma.get_readonly_fields(request),
            ["used_in", "last_measured_state_of_health", "attributes"],
        )
        self.assertEqual(ma.get_exclude(request), ["attributes"])


class TestBatchInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import BatchInline
        from battDB.models import Batch

        ma = BatchInline(Batch, self.site)
        self.assertEqual(ma.model, Batch)
        self.assertEqual(ma.get_extra(request), 0)
        self.assertEqual(ma.get_exclude(request), ["attributes"])


class TestBatchAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import BatchAdmin, BatchInline, DeviceInline
        from battDB.models import Batch

        baker.make("battDB.Batch", manufacturer=baker.make("common.Org"))
        ma = BatchAdmin(Batch, self.site)
        self.assertEqual(ma.model, Batch)
        for d in ["manufacturer", "batch_size"]:
            self.assertIn(d, ma.get_list_display(request))
            self.assertIn(d, ma.get_list_filter(request))
        for d in ["__str__", "manufacturer", "serialNo"]:
            self.assertIn(d, ma.get_list_display(request))
        self.assertEqual(
            ma.get_inlines(request, Batch.objects.get()), [BatchInline, DeviceInline]
        )


class TestExperimentDataInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import ExperimentDataInline
        from battDB.models import ExperimentDataFile

        ma = ExperimentDataInline(ExperimentDataFile, self.site)
        self.assertEqual(ma.model, ExperimentDataFile)
        self.assertEqual(ma.get_extra(request), 0)
        self.assertEqual(
            ma.get_exclude(request), ["attributes", "file_hash", "user_owner"]
        )


class TestExperimentDeviceInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import ExperimentDeviceInline
        from battDB.models import ExperimentDevice

        ma = ExperimentDeviceInline(ExperimentDevice, self.site)
        self.assertEqual(ma.model, ExperimentDevice)
        self.assertEqual(ma.get_extra(request), 1)
        self.assertEqual(ma.get_readonly_fields(request), ["get_serial_no"])


class TestExperimentAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import ExperimentAdmin, ExperimentDeviceInline
        from battDB.models import Experiment

        baker.make("battDB.Experiment")
        ma = ExperimentAdmin(Experiment, self.site)
        self.assertEqual(ma.model, Experiment)
        self.assertIn("data_files_list", ma.get_readonly_fields(request))
        for d in ["__str__", "devices_", "files_", "cycles_"]:
            self.assertIn(d, ma.get_list_display(request))
        self.assertEqual(
            ma.get_inlines(request, Experiment.objects.get()), [ExperimentDeviceInline]
        )
        self.assertTrue(ma.save_as)

    def test_data_files_list(self):
        from battDB.admin import ExperimentAdmin
        from battDB.models import Experiment

        baker.make("battDB.Experiment")
        ma = ExperimentAdmin(Experiment, self.site)
        self.assertEqual(ma.data_files_list(Experiment.objects.get()), "")


class TestDeviceConfigInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceConfigInline
        from battDB.models import DeviceConfigNode

        ma = DeviceConfigInline(DeviceConfigNode, self.site)
        self.assertEqual(ma.model, DeviceConfigNode)
        self.assertEqual(ma.get_extra(request), 2)


class TestDeviceConfigAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceConfigAdmin, DeviceConfigInline
        from battDB.models import DeviceConfig

        baker.make("battDB.DeviceConfig")
        ma = DeviceConfigAdmin(DeviceConfig, self.site)
        self.assertEqual(ma.model, DeviceConfig)
        self.assertEqual(
            ma.get_inlines(request, DeviceConfig.objects.get()), [DeviceConfigInline]
        )


class TestDeviceDataInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DeviceDataInline
        from battDB.models import DataColumn

        ma = DeviceDataInline(DataColumn, self.site)
        self.assertEqual(ma.model, DataColumn)
        self.assertEqual(ma.get_extra(request), 0)


class TestDataFileInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import DataFileInline
        from battDB.models import UploadedFile

        ma = DataFileInline(UploadedFile, self.site)
        self.assertEqual(ma.model, UploadedFile)
        self.assertEqual(ma.get_max_num(request), 1)
        self.assertEqual(
            ma.get_readonly_fields(request), ["size", "local_date", "exists", "hash"]
        )


@expectedFailure
class TestDataRangeInline(TestCase):
    def test_size(self):
        self.fail()

    def test_get_graph_link(self):
        self.fail()

    def test_columns(self):
        self.fail()


@expectedFailure
class TestDataAdmin(TestCase):
    def test_file_data(self):
        self.fail()

    def test_parsed_data(self):
        self.fail()

    def test_get_experiment_link(self):
        self.fail()

    def test_get_file_link(self):
        self.fail()


@expectedFailure
class TestFolderAdmin(TestCase):
    pass


class TestParserSignalInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import ParserSignalInline
        from battDB.models import SignalType

        ma = ParserSignalInline(SignalType, self.site)
        self.assertEqual(ma.model, SignalType)
        self.assertEqual(ma.get_extra(request), 1)
        self.assertEqual(ma.get_ordering(request), ["order"])


class TestParserAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_definition(self):
        from battDB.admin import ParserAdmin, ParserSignalInline
        from battDB.models import Parser

        baker.make("battDB.Parser")
        ma = ParserAdmin(Parser, self.site)
        self.assertEqual(ma.model, Parser)
        self.assertEqual(
            ma.get_inlines(request, Parser.objects.get()), [ParserSignalInline]
        )
        self.assertTrue(ma.save_as)
