# Generated by Django 3.1.2 on 2020-11-02 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0148_auto_20201102_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataparser',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='modified_on',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='dataparser',
            name='user_owner',
        ),
    ]
