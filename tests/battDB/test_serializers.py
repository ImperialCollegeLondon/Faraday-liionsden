from django.test import TestCase


class TestDataFileSerializer(TestCase):
    from battDB.serializers import DataFileSerializer

    model = DataFileSerializer

    def test_meta(self):
        from battDB.models import ExperimentDataFile

        self.assertEqual(self.model.Meta.model, ExperimentDataFile)
        self.assertEqual(self.model.Meta.exclude, [])


class TestNewDataFileSerializer(TestCase):
    from battDB.serializers import NewDataFileSerializer

    model = NewDataFileSerializer

    def test_meta(self):
        from battDB.models import ExperimentDataFile

        self.assertEqual(self.model.Meta.model, ExperimentDataFile)
        self.assertEqual(self.model.Meta.exclude, ["user_owner"])


class TestExperimentSerializer(TestCase):
    from battDB.serializers import ExperimentSerializer

    model = ExperimentSerializer

    def test_meta(self):
        from battDB.models import Experiment

        self.assertEqual(self.model.Meta.model, Experiment)
        self.assertEqual(self.model.Meta.exclude, [])


class TestDataRangeSerializer(TestCase):
    from battDB.serializers import DataRangeSerializer

    model = DataRangeSerializer

    def test_meta(self):
        from battDB.models import DataRange

        self.assertEqual(self.model.Meta.model, DataRange)
        self.assertEqual(self.model.Meta.exclude, [])


class TestFileHashSerializer(TestCase):
    from battDB.serializers import FileHashSerializer

    model = FileHashSerializer

    def test_meta(self):
        from battDB.models import UploadedFile

        self.assertEqual(self.model.Meta.model, UploadedFile)
        self.assertEqual(self.model.Meta.fields, ["id", "hash", "edf_id"])


class TestGeneralSerializer(TestCase):
    from battDB.serializers import GeneralSerializer

    model = GeneralSerializer

    def test_meta(self):
        self.assertEqual(self.model.Meta.model, None)
