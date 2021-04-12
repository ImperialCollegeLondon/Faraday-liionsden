# Generated by Django 3.1.2 on 2020-11-01 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0050_ExperimentDataFile"),
        ("battDB", "0134_ExperimentDataFile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datacolumn", old_name="signal_name", new_name="column_name",
        ),
        migrations.AlterField(
            model_name="experimentdatafile",
            name="raw_data_file",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="used_by",
                to="common.uploadedfile",
            ),
        ),
    ]
