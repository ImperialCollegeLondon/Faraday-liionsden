# Generated by Django 3.1.2 on 2020-11-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0160_remove_harvester_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='parser',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
