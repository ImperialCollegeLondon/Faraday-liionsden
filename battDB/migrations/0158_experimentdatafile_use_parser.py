# Generated by Django 3.1.2 on 2020-11-10 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0157_ParserSignal"),
    ]

    operations = [
        migrations.AddField(
            model_name="experimentdatafile",
            name="use_parser",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="battDB.parser",
            ),
        ),
    ]
