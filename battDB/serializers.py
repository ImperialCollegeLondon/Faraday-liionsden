from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers

from .models import Experiment, ExperimentDataFile, UploadedFile


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    """https://stackoverflow.com/questions/28009829/creating-and-saving-foreign-key-
    objects-using-a-slugrelatedfield."""

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail(
                "does_not_exist", slug_name=self.slug_field, value=smart_text(data)
            )
        except (TypeError, ValueError):
            self.fail("invalid")


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
    """Serializer for existing data range objects.

    FIXME: Seems identical to ExperimentSerializer
    """

    class Meta:
        model = Experiment
        exclude = []


class FileHashSerializer(serializers.ModelSerializer):
    """Serializer for file hashes."""

    edf_id = serializers.IntegerField(source="experimentdatafile.id")

    class Meta:
        model = UploadedFile
        fields = ["id", "hash", "edf_id"]


class GeneralSerializer(serializers.ModelSerializer):
    """General purpose serializer.

    FIXME: What is this for?
    """

    class Meta:
        model = None
