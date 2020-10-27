# Generated by Django 3.1.2 on 2020-10-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0044_MPTT_Device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='is_template',
        ),
        migrations.AddField(
            model_name='thing',
            name='inherit_metadata',
            field=models.BooleanField(default=True, help_text='Set to true if this object does not describe a real life object, but a specification, type or grouping of objects. If so, the metadata will be inherited'),
        ),
    ]
