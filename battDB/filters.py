from django.db import models
from django_filters import CharFilter, FilterSet
from django_filters.filters import ChoiceFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import Experiment


class ExperimentFilter(FilterSet):
    date = DateFromToRangeFilter(
        widget=RangeWidget(attrs={"type": "date"}), label="Date range"
    )

    class Meta:
        model = Experiment
        fields = ["id", "name", "status", "user_owner", "user_owner__institution"]

        # Allow filtering on partial matches for charfield
        filter_overrides = {
            models.CharField: {
                "filter_class": CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            }
        }

    # Modify init slightly to add custom label(s)
    def __init__(self, *args, **kwargs):
        super(ExperimentFilter, self).__init__(*args, **kwargs)
        self.filters["user_owner__institution"].label = "Institution"
