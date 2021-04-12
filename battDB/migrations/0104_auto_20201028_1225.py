# Generated by Django 3.1.2 on 2020-10-28 12:25

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0103_auto_20201028_1135"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceList",
            fields=[],
            options={
                "verbose_name_plural": "Device List",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("battDB.device",),
        ),
        migrations.AlterModelOptions(
            name="device", options={"verbose_name_plural": "Device Tree"},
        ),
        migrations.AlterField(
            model_name="device",
            name="devType",
            field=models.CharField(
                choices=[
                    ("component", "Component part of a cell"),
                    ("cell", "Single cell"),
                    ("module", "Module containing cells"),
                    ("battery", "Battery pack containing sub-modules"),
                    ("sensor", "Sensor attached to a device"),
                    ("cycler", "Cycler Machine"),
                ],
                default="cell",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="date",
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
