import django_tables2 as tables

from .models import Compound, Material


class CompoundTable(tables.Table):
    id = tables.Column(linkify=("dfndb:Update Compound", [tables.A("pk")]))

    class Meta:
        model = Compound
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "formula", "mass")


class MaterialTable(tables.Table):
    id = tables.Column(linkify=True)

    class Meta:
        model = Material
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "composition", "type")

        row_attrs = {"status": lambda record: record.status}
