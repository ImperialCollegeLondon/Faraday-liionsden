from rest_framework import serializers

from . import models


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parameter
        exclude: list[str] = []
