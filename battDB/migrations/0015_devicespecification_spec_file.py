# Generated by Django 4.0.1 on 2022-01-11 10:54

from django.db import migrations, models

import common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0014_alter_batch_serialno'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicespecification',
            name='spec_file',
            field=models.FileField(blank=True, help_text='PDF version of spec. sheet for this type of device.', null=True, upload_to='uploaded_files', validators=[common.validators.validate_pdf_file]),
        ),
    ]
