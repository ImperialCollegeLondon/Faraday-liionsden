# Generated by Django 3.1.2 on 2020-11-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0175_auto_20201112_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchdevice',
            name='seq_num',
            field=models.PositiveSmallIntegerField(default=1, help_text='Sequence number within batch'),
        ),
        migrations.AlterUniqueTogether(
            name='batchdevice',
            unique_together={('batch', 'seq_num')},
        ),
        migrations.RemoveField(
            model_name='batchdevice',
            name='batch_index',
        ),
        migrations.RemoveField(
            model_name='batchdevice',
            name='serialNo',
        ),
    ]
