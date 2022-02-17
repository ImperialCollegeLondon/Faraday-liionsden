import django_tables2 as tables

from .models import Component, Compound


class CompoundTable(tables.Table):
    id = tables.Column(linkify=("dfndb:Update Compound", [tables.A("pk")]))

    class Meta:
        model = Compound
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "formula", "mass")


class ComponentTable(tables.Table):
    id = tables.Column(linkify=True)

    class Meta:
        model = Component
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "composition", "type")

        row_attrs = {"status": lambda record: record.status}
