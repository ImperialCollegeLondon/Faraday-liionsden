# Generated by Django 3.1.2 on 2020-10-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0024_auto_20201016_1354"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="polymer",
            field=models.PositiveIntegerField(
                default=0,
                help_text="If this material is a polymer, enter degree of polymerization",
            ),
        ),
        migrations.AlterField(
            model_name="material",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Anode"),
                    (2, "Cathode"),
                    (3, "Electrolyte"),
                    (4, "Separator"),
                ]
            ),
        ),
    ]
