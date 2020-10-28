from rest_framework import serializers
from .models import *

# class DataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DataRange
#         exclude=[]
        
class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentDataFile
        exclude=[]

