# Generated by Django 3.2.7 on 2021-11-12 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0007_devicespecification_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='protocol',
        ),
    ]
