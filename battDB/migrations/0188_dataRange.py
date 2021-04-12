# Generated by Django 3.1.2 on 2020-11-13 16:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0187_dataRange"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datarange",
            name="ts_data",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.FloatField(), size=None
                ),
                blank=True,
                editable=False,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="datarange",
            name="ts_headers",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                editable=False,
                null=True,
                size=None,
            ),
        ),
    ]
