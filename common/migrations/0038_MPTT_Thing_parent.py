# Generated by Django 3.1.2 on 2020-10-26 15:05

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0037_auto_20201026_1412"),
    ]

    operations = [
        migrations.RemoveField(model_name="thing", name="parent",),
        migrations.AddField(
            model_name="thing",
            name="part_of",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                help_text="Is this Thing a physical part of another Thing?",
                limit_choices_to={"is_composite": True},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="components",
                to="common.thing",
            ),
        ),
        migrations.AddField(
            model_name="thing",
            name="type",
            field=models.CharField(default="Thing", max_length=16),
        ),
    ]
