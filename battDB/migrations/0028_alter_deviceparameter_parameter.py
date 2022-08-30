# Generated by Django 4.1 on 2022-08-30 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0012_parameter_parameter_type'),
        ('battDB', '0027_devicespecification_components'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceparameter',
            name='parameter',
            field=models.ForeignKey(limit_choices_to={'parameter_type': 'device'}, on_delete=django.db.models.deletion.CASCADE, to='dfndb.parameter'),
        ),
    ]