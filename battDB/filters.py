from django.db import models
from django_filters import CharFilter, DateFilter, FilterSet
from django_filters.filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import Experiment


class ExperimentFilter(FilterSet):
    date = DateFromToRangeFilter(
        widget=RangeWidget(attrs={"type": "date"}), label="Date range"
    )

    class Meta:
        model = Experiment
        fields = ["id", "name", "status", "user_owner"]

        # Allow filtering on partial matches for charfield
        filter_overrides = {
            models.CharField: {
                "filter_class": CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            }
        }
