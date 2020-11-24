from rest_framework import serializers
from .models import *
from common.models import UploadedFile

# class DataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DataRange
#         exclude=[]
        
class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentDataFile
        exclude=[]


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
    class Meta:
        model = UploadedFile
        fields = ['id', 'hash']


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
