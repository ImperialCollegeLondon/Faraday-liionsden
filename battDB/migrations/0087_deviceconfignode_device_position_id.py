# Generated by Django 3.1.2 on 2020-10-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0086_auto_20201022_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceconfignode',
            name='device_position_id',
            field=models.CharField(blank=True, help_text='Position of device in pack e.g. 1 - identifies this device', max_length=20, null=True),
        ),
    ]