# Generated by Django 3.1.2 on 2020-10-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0087_deviceconfignode_device_position_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='terminals',
            field=models.TextField(help_text="comma-separated list of terminal names e.g. 'Positive, Negative'", null=True),
        ),
        migrations.AlterField(
            model_name='deviceconfignode',
            name='device_terminal_name',
            field=models.CharField(blank=True, help_text="Name of device port or terminal. e.g. 'Anode'", max_length=10, null=True),
        ),
    ]
