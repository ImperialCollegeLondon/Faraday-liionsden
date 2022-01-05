import django_tables2 as tables

from .models import Batch, Experiment


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
        row_attrs = {"status": lambda record: record.status}


class BatchTable(tables.Table):
    # id = tables.Column(linkify=True)

    class Meta:
        model = Batch
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "user_owner",
            "manufacturer",
            "status",
            "manufactured_on",
            "specification",
            "serialNo",
            "created_on",
        )
