import django_tables2 as tables

from .models import Experiment


class ExperimentTable(tables.Table):
    class Meta:
        model = Experiment
