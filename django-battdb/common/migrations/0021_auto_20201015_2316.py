# Generated by Django 3.1.2 on 2020-10-15 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_auto_20201015_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='device',
            name='user_owner',
        ),
        migrations.RemoveField(
            model_name='devicetype',
            name='user_owner',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='DeviceType',
        ),
    ]
