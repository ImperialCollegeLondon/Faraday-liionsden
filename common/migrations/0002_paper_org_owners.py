# Generated by Django 3.1.2 on 2020-10-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="org_owners",
            field=models.ManyToManyField(related_name="papers", to="common.Org"),
        ),
    ]
