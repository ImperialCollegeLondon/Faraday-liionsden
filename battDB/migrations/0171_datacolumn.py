# Generated by Django 3.1.2 on 2020-11-12 15:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0037_ManufacturingProtocol"),
        ("battDB", "0170_delete_datacolumn"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataColumn",
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
                ("column_name", models.CharField(default="Ns", max_length=40)),
                (
                    "resample",
                    models.CharField(
                        choices=[
                            ("none", "Do not resample"),
                            ("on_change", "Sample on change"),
                            ("decimate", "Take every Nth sample"),
                            ("average", "Average every Nth sample"),
                            ("max", "Maximum every Nth sample"),
                            ("min", "Minimum every Nth sample"),
                        ],
                        default="none",
                        help_text="Resampling option - TO BE IMPLEMENTED - currently has no effect",
                        max_length=10,
                    ),
                ),
                (
                    "resample_n",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Resampling divisor - TO BE IMPLEMENTED",
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "data_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="battDB.experimentdatafile",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        blank=True,
                        help_text="Device id for parameter mapping",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="battDB.experimentdevice",
                    ),
                ),
                (
                    "parameter",
                    models.ForeignKey(
                        blank=True,
                        help_text="Map this column to a parameter on a device",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dfndb.parameter",
                    ),
                ),
            ],
            options={
                "verbose_name": "Column Mapping",
                "verbose_name_plural": "Data Column Mappings to Device Parameters",
                "unique_together": {
                    ("column_name", "data_file"),
                    ("device", "data_file"),
                },
            },
        ),
    ]
