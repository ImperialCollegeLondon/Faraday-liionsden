# Generated by Django 3.1.2 on 2020-11-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0159_ParserBaseModel"),
    ]

    operations = [
        migrations.RemoveField(model_name="harvester", name="user_token",),
    ]
