# Generated by Django 3.1.2 on 2020-10-15 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0066_auto_20201015_2316'),
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
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
