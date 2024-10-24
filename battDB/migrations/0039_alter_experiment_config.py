# Generated by Django 4.1.3 on 2023-01-05 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0038_initial_device_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='config',
            field=models.ForeignKey(default=1, help_text='All devices in the same experiment must be of the same configuration, i.e. an experiment must use all single cells, or all 2s2p modules, not a mixture of both.', limit_choices_to={'config_type': 'expmt'}, on_delete=django.db.models.deletion.CASCADE, related_name='used_in', to='battDB.deviceconfig'),
        ),
    ]
