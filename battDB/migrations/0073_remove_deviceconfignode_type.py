# Generated by Django 3.1.2 on 2020-10-18 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0072_auto_20201018_2215"),
    ]

    operations = [
        migrations.RemoveField(model_name="deviceconfignode", name="type",),
    ]
