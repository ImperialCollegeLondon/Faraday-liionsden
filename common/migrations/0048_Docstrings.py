# Generated by Django 3.1.2 on 2020-10-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0047_auto_20201028_1112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thing",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
