import django_tables2 as tables

from .models import Batch, DeviceSpecification, Experiment


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
            "manufactured_on",
            "specification",
            "serialNo",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}


class DeviceSpecificationTable(tables.Table):
    # id = tables.Column(linkify=True)

    user_owner = tables.Column(verbose_name="Added by")

    class Meta:
        model = DeviceSpecification
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "device_type",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}


class EquipmentTable(tables.Table):
    # id = tables.Column(linkify=True)
    class Meta:
        model = DeviceSpecification
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "institution",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}
