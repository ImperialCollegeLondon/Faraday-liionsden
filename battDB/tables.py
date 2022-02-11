import django_tables2 as tables

from .models import (
    Batch,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDevice,
    Parser,
)


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
    id = tables.Column(linkify=True)

    class Meta:
        model = Batch
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "user_owner",
            "manufacturer",
            "manufactured_on",
            "specification",
            "batch_size",
            "serialNo",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}


class DeviceSpecificationTable(tables.Table):
    id = tables.Column(linkify=True)
    user_owner = tables.Column(verbose_name="Added by")
    spec_file = tables.FileColumn(text="download")

    class Meta:
        model = DeviceSpecification
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "device_type",
            "created_on",
            "spec_file",
        )
        row_attrs = {"status": lambda record: record.status}


class EquipmentTable(tables.Table):
    id = tables.Column(linkify=True)

    class Meta:
        model = Equipment
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "user_owner",
            "institution",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}


class BatchDevicesTable(tables.Table):
    class Meta:
        model = ExperimentDevice
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "batch",
        )


class ParserTable(tables.Table):
    # name = tables.Column(linkify=True)
    num_cols = tables.Column(
        accessor="get_number_parameters", verbose_name="# Columns parsed"
    )

    class Meta:
        model = Parser
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "name",
            "notes",
            "num_cols",
            "created_on",
        )
        row_attrs = {"status": lambda record: record.status}
