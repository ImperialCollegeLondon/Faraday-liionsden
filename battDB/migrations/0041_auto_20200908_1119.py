# Generated by Django 3.1.1 on 2020-09-08 11:19

from django.db import migrations, models

import battDB.models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0040_auto_20200903_1816"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cell",
            name="attributes",
            field=models.JSONField(blank=True, default=battDB.models.cell_schema),
        ),
        migrations.AlterField(
            model_name="cellbatch",
            name="attributes",
            field=models.JSONField(blank=True, default=battDB.models.cell_schema),
        ),
        migrations.AlterField(
            model_name="cellbatch",
            name="cells_schema",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="cellconfig",
            name="attributes",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="celltype",
            name="attributes",
            field=models.JSONField(blank=True, default=battDB.models.cell_schema),
        ),
        migrations.AlterField(
            model_name="datarange",
            name="analysis",
            field=models.JSONField(
                blank=True, default=battDB.models.experimentAnalysis_schema
            ),
        ),
        migrations.AlterField(
            model_name="datarange",
            name="events",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="attributes",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="equipmenttype",
            name="attributes",
            field=models.JSONField(
                blank=True, default=battDB.models.equipmentType_schema
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="analysis",
            field=models.JSONField(
                blank=True, default=battDB.models.experimentAnalysis_schema
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="parameters",
            field=models.JSONField(
                blank=True, default=battDB.models.experimentParameters_schema
            ),
        ),
        migrations.AlterField(
            model_name="experimentalapparatus",
            name="attributes",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="experimentdatafile",
            name="analysis",
            field=models.JSONField(
                blank=True, default=battDB.models.experimentAnalysis_schema
            ),
        ),
        migrations.AlterField(
            model_name="experimentdatafile",
            name="data",
            field=models.JSONField(blank=True, default=battDB.models.resultData_schema),
        ),
        migrations.AlterField(
            model_name="experimentdatafile",
            name="metadata",
            field=models.JSONField(
                blank=True, default=battDB.models.resultMetadata_schema
            ),
        ),
        migrations.AlterField(
            model_name="experimentdatafile",
            name="parameters",
            field=models.JSONField(
                blank=True, default=battDB.models.experimentParameters_schema
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="attributes",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="testprotocol",
            name="attributes",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="testprotocol",
            name="parameters",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
