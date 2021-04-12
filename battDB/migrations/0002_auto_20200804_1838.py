# Generated by Django 2.2.14 on 2020-08-04 18:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

import battDB.models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EquipmentType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "attributes",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.AlterModelOptions(
            name="cellbatch", options={"verbose_name_plural": "CellBatches"},
        ),
        migrations.AlterModelOptions(
            name="equipment", options={"verbose_name_plural": "Equipment"},
        ),
        migrations.AlterModelOptions(
            name="experimentalapparatus",
            options={"verbose_name_plural": "ExperimentalApparatus"},
        ),
        migrations.AlterField(
            model_name="cellseparator",
            name="attributes",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=battDB.models.cellSeparator_schema
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="analysis",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=battDB.models.experimentAnalysis_schema
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="parameters",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=battDB.models.experimentParameters_schema
            ),
        ),
    ]
