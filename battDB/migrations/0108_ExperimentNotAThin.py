# Generated by Django 3.1.2 on 2020-10-28 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0107_ExperimentNotAThing"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="experimentdatafile",
            options={"verbose_name": "dataset", "verbose_name_plural": "Data Files"},
        ),
        migrations.RemoveField(model_name="experimentdatafile", name="raw_data_file",),
    ]
