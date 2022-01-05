import django_tables2 as tables

from .models import Experiment


class ExperimentTable(tables.Table):
    id = tables.Column(linkify=True)

    class Meta:
        model = Experiment
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "user_owner__institution",
            "status",
            "date",
            "config",
            "created_on",
        )
