# Generated by Django 4.1 on 2022-08-30 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0012_parameter_parameter_type'),
        ('battDB', '0028_alter_deviceparameter_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signaltype',
            name='parameter',
            field=models.ForeignKey(limit_choices_to={'parameter_type': 'experiment'}, on_delete=django.db.models.deletion.CASCADE, to='dfndb.parameter'),
        ),
    ]