from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from .models import *

# https://stackoverflow.com/questions/28009829/creating-and-saving-foreign-key-objects-using-a-slugrelatedfield
class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

# class DataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DataRange
#         exclude=[]
        
class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentDataFile
        exclude=[]

class NewDataFileSerializer(DataFileSerializer):
    class Meta:
        model = ExperimentDataFile
        exclude=['user_owner']


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        exclude = []
        #fields = ['name']


class DataRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        exclude = []


class HarvesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvester
        exclude = []

class FileHashSerializer(serializers.ModelSerializer):
    #experimentdatafile = DataFileSerializer()
    edf_id = serializers.IntegerField(source="experimentdatafile.id")
    class Meta:
        model = UploadedFile
        fields = ['id', 'hash', 'edf_id']


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
