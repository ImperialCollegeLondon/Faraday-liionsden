# Generated by Django 2.2.14 on 2020-08-05 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0011_auto_20200804_1926"),
    ]

    operations = [
        migrations.AddField(
            model_name="cell",
            name="separator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="battDB.CellSeparator",
            ),
        ),
    ]
