# Generated by Django 3.1.2 on 2020-11-02 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0147_DataEquipment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentdatafile",
            name="machine",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="battDB.equipment",
            ),
        ),
    ]
