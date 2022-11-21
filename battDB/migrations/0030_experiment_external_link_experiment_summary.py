# Generated by Django 4.1.3 on 2022-11-18 11:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0029_alter_signaltype_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='external_link',
            field=models.URLField(blank=True, help_text='Specific link to a reference for this experiment.', null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='summary',
            field=models.TextField(default='', help_text='Summary of what was done in the experiment e.g. what was the motivation, etc.', validators=[django.core.validators.MinLengthValidator(20)]),
            preserve_default=False,
        ),
    ]