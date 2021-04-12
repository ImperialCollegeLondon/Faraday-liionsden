# Generated by Django 3.1.2 on 2020-10-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0027_remove_data_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataparameter",
            name="value",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="dataparameter", unique_together={("data", "parameter", "material")},
        ),
    ]
