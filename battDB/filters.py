import django_filters

from .models import Experiment


class ExperimentFilter(django_filters.FilterSet):
    class Meta:
        model = Experiment
        fields = ["id", "name", "date"]
