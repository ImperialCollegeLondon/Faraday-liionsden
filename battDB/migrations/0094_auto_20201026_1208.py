# Generated by Django 3.1.2 on 2020-10-26 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0033_auto_20201021_1112"),
        ("battDB", "0093_auto_20201026_1141"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="parent_device",
            field=models.ForeignKey(
                blank=True,
                help_text="If this device is part of a module or pack, link to it here",
                limit_choices_to={"devType": 30},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="child_devices",
                to="battDB.device",
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="protocol",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"type": 2000},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dfndb.method",
            ),
        ),
    ]
