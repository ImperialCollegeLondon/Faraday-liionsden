# Generated by Django 3.1.2 on 2020-11-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0189_harvester_parser_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvester',
            name='local_folder',
            field=models.CharField(default='.', max_length=500),
        ),
    ]