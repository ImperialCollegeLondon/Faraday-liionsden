from rest_framework import serializers
from .models import *


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        exclude = []
