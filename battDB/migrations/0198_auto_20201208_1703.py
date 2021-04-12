# Generated by Django 3.1.2 on 2020-12-08 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0197_remove_experiment_data_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentdatafile",
            name="experiment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="data_files",
                to="battDB.experiment",
            ),
        ),
    ]
