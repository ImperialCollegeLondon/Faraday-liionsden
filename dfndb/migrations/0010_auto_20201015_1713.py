# Generated by Django 3.1.2 on 2020-10-15 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0009_auto_20201015_1712"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="data",
            name="modified_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="material",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="material",
            name="modified_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="method",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="method",
            name="modified_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="parameter",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="parameter",
            name="modified_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
