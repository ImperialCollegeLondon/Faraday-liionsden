# Generated by Django 3.1.2 on 2020-10-16 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0026_auto_20201016_1655"),
    ]

    operations = [
        migrations.RemoveField(model_name="data", name="data",),
    ]
