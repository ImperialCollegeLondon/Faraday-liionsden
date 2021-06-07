from rest_framework import serializers

from .models import DataRange, Experiment, ExperimentDataFile, UploadedFile


class DataFileSerializer(serializers.ModelSerializer):
    """Serializer for existing data file objects."""

    class Meta:
        model = ExperimentDataFile
        exclude = []


class NewDataFileSerializer(DataFileSerializer):
    """Serializer for new data file objects."""

    class Meta:
        model = ExperimentDataFile
        exclude = ["user_owner"]


class ExperimentSerializer(serializers.ModelSerializer):
    """Serializer for experiment objects."""

    class Meta:
        model = Experiment
        exclude = []


class DataRangeSerializer(serializers.ModelSerializer):
    """Serializer for existing data range objects."""

    class Meta:
        model = DataRange
        exclude = []


class FileHashSerializer(serializers.ModelSerializer):
    """Serializer for file hashes."""

    edf_id = serializers.IntegerField(source="experimentdatafile.id")

    class Meta:
        model = UploadedFile
        fields = ["id", "hash", "edf_id"]


class GeneralSerializer(serializers.ModelSerializer):
    """General purpose serializer."""

    class Meta:
        model = None
