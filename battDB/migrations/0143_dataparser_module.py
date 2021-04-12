# Generated by Django 3.1.2 on 2020-11-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0142_DataParser"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataparser",
            name="module",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Python module to run this parser",
                max_length=100,
            ),
        ),
    ]
