# Generated by Django 3.1.2 on 2020-10-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0079_auto_20201020_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceconfignode',
            name='deviceConfig',
        ),
        migrations.RemoveField(
            model_name='deviceconfignode',
            name='deviceType',
        ),
        migrations.AddField(
            model_name='deviceconfignode',
            name='Device_terminal_name',
            field=models.CharField(blank=True, help_text="Name of device port or terminal. e.g. 'Anode'", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='deviceconfignode',
            name='Net_name',
            field=models.CharField(blank=True, help_text='Name of electrical signal e.g. cell_1_v', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='deviceconfignode',
            name='config',
            field=models.ForeignKey(default=0, help_text='Config instance to which this node belongs', on_delete=django.db.models.deletion.CASCADE, to='battDB.deviceconfig'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceconfignode',
            name='device',
            field=models.ForeignKey(default=0, help_text='Related device specification e.g. cell or sensor. Must have is_template=True', limit_choices_to={'is_template': True}, on_delete=django.db.models.deletion.CASCADE, to='battDB.device'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceconfignode',
            name='next',
            field=models.ForeignKey(blank=True, help_text='Connected node in chain. Must be part of the same config.In a series pack, this would be the negative terminal of the next cell', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.deviceconfignode'),
        ),
    ]