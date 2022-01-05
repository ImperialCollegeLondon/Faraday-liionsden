import django_filters
from django.db import models

from .models import Experiment


class ExperimentFilter(django_filters.FilterSet):
    class Meta:
        model = Experiment
        fields = ["id", "name", "date", "status"]

        # Allow filtering on partial matches for charfield
        filter_overrides = {
            models.CharField: {
                "filter_class": django_filters.CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            }
        }
