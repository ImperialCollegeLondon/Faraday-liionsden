# Generated by Django 3.1.2 on 2020-10-18 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0073_remove_deviceconfignode_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeviceConfigNode',
        ),
    ]
