# Generated by Django 3.2.7 on 2021-11-12 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0006_auto_20211104_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicespecification',
            name='config',
            field=models.ForeignKey(blank=True, help_text='Configuration of sub-devices if the device type is a module or pack.', limit_choices_to={'config_type': 'module'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_in_modules', to='battDB.deviceconfig'),
        ),
    ]
