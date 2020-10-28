# Generated by Django 3.1.2 on 2020-10-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0101_BatchDeviceAttributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='specification',
            field=models.ForeignKey(blank=True, help_text='Copy metadata from another device?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.device'),
        ),
    ]
