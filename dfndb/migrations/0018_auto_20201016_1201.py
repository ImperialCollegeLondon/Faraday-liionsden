# Generated by Django 3.1.2 on 2020-10-16 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0017_auto_20201016_1136"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quantityunit", old_name="name", new_name="quantityName",
        ),
        migrations.RenameField(
            model_name="quantityunit", old_name="symbol", new_name="quantitySymbol",
        ),
        migrations.AlterField(
            model_name="compositionpart",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
    ]
