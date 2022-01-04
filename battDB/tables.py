import django_tables2 as tables

from .models import Experiment


class ExperimentTable(tables.Table):
    class Meta:
        model = Experiment
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "status",
            "date",
            "config",
            "created_on",
            "modified_on",
        )
