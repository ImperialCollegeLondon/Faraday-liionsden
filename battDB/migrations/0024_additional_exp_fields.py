# Generated by Django 3.2.7 on 2022-02-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0023_alter_experimentdevice_device_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='c_rate',
            field=models.FloatField(blank=True, help_text='C-rate for this experiment.', null=True, verbose_name='C-rate'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='exp_type',
            field=models.CharField(choices=[('constant', 'Constant current'), ('gitt', 'GITT'), ('hpcc', 'HPCC'), ('drivecycle', 'Drivecycle'), ('other', 'Other')], default='constant', help_text="Type of experiment carried out. If 'other', experiment type should be specified in the notes section.", max_length=50, verbose_name='Experiment type'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='temperature',
            field=models.FloatField(blank=True, help_text='Experiment temperature in degrees Celcius.', null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='thermal',
            field=models.CharField(choices=[('none', 'None'), ('chamber', 'Thermal chamber'), ('base', 'Base cooled'), ('surface', 'Surface cooled'), ('tab', 'Tab cooled'), ('other', 'Other')], default='none', help_text="Thermal management technique used in this experiment.  If 'other', technique should be specified in the notes section.", max_length=50, verbose_name='Thermal management'),
        ),
    ]
