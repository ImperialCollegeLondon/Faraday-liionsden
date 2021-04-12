# Generated by Django 3.1.2 on 2020-10-16 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0023_auto_20201016_1219"),
    ]

    operations = [
        migrations.RemoveField(model_name="person", name="name",),
        migrations.AddField(
            model_name="person",
            name="longName",
            field=models.CharField(
                default="nobby",
                help_text="Person's full name e.g. David Wallace Jones",
                max_length=128,
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="shortName",
            field=models.CharField(
                default="n",
                help_text="Person's shortened name e.g. 'D.W. Jones'",
                max_length=128,
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="person",
            name="org",
            field=models.ForeignKey(
                blank=True,
                help_text="Organisation that this user belongs to",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.org",
            ),
        ),
    ]
