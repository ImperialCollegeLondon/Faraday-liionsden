# Generated by Django 4.1.3 on 2023-01-17 14:16

from django.db import migrations


def simplify_biologic_parsers(apps, schema_editor):
    """Separates the Biologic parser into two parsers.

    Args:
        apps (_type_): app registry with the current status of the apps in the migration
            process.
        schema_editor (_type_): Not used.
    """
    Parser = apps.get_model("battDB", "Parser")

    parser = Parser.objects.get(name="Biologic Ecell")
    parser.name = "Biologic"
    parser.save()

    parser = Parser.objects.get(name="Biologic Ewe")
    parser.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0042_alter_deviceparameter_value"),
    ]

    operations = [migrations.RunPython(simplify_biologic_parsers)]