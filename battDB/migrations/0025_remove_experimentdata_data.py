# Generated by Django 2.2.14 on 2020-08-16 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0024_auto_20200815_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experimentdata',
            name='data',
        ),
    ]