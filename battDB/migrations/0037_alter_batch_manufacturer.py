# Generated by Django 4.1.3 on 2023-01-04 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20211115_1357'),
        ('battDB', '0036_alter_batch_serialno_alter_experiment_thermal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='manufacturer',
            field=models.ForeignKey(default=1, limit_choices_to={'is_mfg_cells': True}, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.org'),
        ),
    ]
