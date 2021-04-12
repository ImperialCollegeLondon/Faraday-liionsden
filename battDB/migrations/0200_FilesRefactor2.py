# Generated by Django 3.1.2 on 2020-12-17 14:04

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0199_FilesRefactor1"),
    ]

    operations = [
        migrations.AddField(
            model_name="experimentdatafile",
            name="raw_data_file",
            field=models.OneToOneField(
                help_text="In most cases, a ",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="battDB.uploadedfile",
            ),
        ),
        migrations.AddField(
            model_name="experimentdatafile",
            name="use_parser",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="battDB.parser",
            ),
        ),
        migrations.AddField(
            model_name="uploadedfile",
            name="local_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="uploadedfile",
            name="local_path",
            field=models.CharField(default="", max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="experimentdatafile",
            unique_together={("raw_data_file", "experiment")},
        ),
    ]
