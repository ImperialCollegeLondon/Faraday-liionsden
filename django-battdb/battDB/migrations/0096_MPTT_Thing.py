# Generated by Django 3.1.2 on 2020-10-26 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0095_auto_20201026_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='device',
            name='parent_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='device',
            name='user_owner',
        ),
        migrations.RemoveField(
            model_name='deviceconfig',
            name='devices',
        ),
        migrations.RemoveField(
            model_name='deviceconfig',
            name='user_owner',
        ),
        migrations.RemoveField(
            model_name='deviceconfignode',
            name='config',
        ),
        migrations.RemoveField(
            model_name='deviceconfignode',
            name='device',
        ),
        migrations.RemoveField(
            model_name='deviceconfignode',
            name='next',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='config',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='device',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='protocol',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='user_owner',
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='DeviceConfig',
        ),
        migrations.DeleteModel(
            name='DeviceConfigNode',
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
    ]
