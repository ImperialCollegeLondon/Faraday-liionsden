# Generated by Django 3.1.2 on 2020-10-28 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0033_auto_20201021_1112'),
        ('battDB', '0108_ExperimentNotAThin'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.PositiveSmallIntegerField(default=0)),
                ('signal_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Data File to Device Mapping',
                'verbose_name_plural': 'Data File to Device Mappings',
            },
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='file_hash',
            field=models.CharField(default='', max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='raw_data_file',
            field=models.FileField(null=True, upload_to='raw_data_files'),
        ),
        migrations.DeleteModel(
            name='RawDataFile',
        ),
        migrations.AddField(
            model_name='devicedata',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.experimentdatafile'),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.device'),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='parameter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.parameter'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='devices',
            field=models.ManyToManyField(blank=True, related_name='data_files', through='battDB.DeviceData', to='battDB.Device'),
        ),
        migrations.AlterUniqueTogether(
            name='devicedata',
            unique_together={('device', 'data', 'batch_id')},
        ),
    ]