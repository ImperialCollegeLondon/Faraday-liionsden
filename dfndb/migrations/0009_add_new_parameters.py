# Generated by Django 4.0.2 on 2022-02-17 15:34

from django.db import migrations

from ..initial_parameters import populate_parameters


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0008_add_new_units"),
    ]

    operations = [migrations.RunPython(populate_parameters)]