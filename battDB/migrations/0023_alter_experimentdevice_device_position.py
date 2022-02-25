# Generated by Django 3.2.7 on 2022-02-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0022_alter_batch_specification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentdevice',
            name='device_position',
            field=models.CharField(default='cell_01', help_text='Device Position ID in Experiment Config - e.g. Cell_A1 for the first cell of a series-parallel pack (leave as cell_01 for single cell experiments)', max_length=20),
        ),
    ]
