# Generated by Django 4.0.1 on 2022-01-11 11:05

import django.db.models.deletion
from django.db import migrations, models

import common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0015_devicespecification_spec_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicespecification',
            name='config',
            field=models.ForeignKey(blank=True, help_text='Configuration of sub-devices if the device type is a module or pack.', limit_choices_to={'config_type': 'module'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_in_modules', to='battDB.deviceconfig', verbose_name='Configuration'),
        ),
        migrations.AlterField(
            model_name='devicespecification',
            name='spec_file',
            field=models.FileField(blank=True, help_text='PDF version of spec. sheet for this type of device.', null=True, upload_to='uploaded_files', validators=[common.validators.validate_pdf_file], verbose_name='Specification sheet'),
        ),
    ]
