# Generated by Django 3.1.2 on 2020-10-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0033_auto_20201021_1112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="material",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="method",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="parameter",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
