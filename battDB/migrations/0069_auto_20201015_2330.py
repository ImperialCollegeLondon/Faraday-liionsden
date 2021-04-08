# Generated by Django 3.1.2 on 2020-10-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0068_device_devicebatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellbatch',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='cellbatch',
            name='user_owner',
        ),
        migrations.RemoveField(
            model_name='celltype',
            name='user_owner',
        ),
        migrations.AlterModelOptions(
            name='devicebatch',
            options={'verbose_name_plural': 'Device Batches'},
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='cells',
        ),
        migrations.AddField(
            model_name='devicebatch',
            name='manufactured_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testprotocol',
            name='description',
            field=models.TextField(help_text='Protocol description, ideally in PyBaMM format'),
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
        migrations.DeleteModel(
            name='CellBatch',
        ),
        migrations.DeleteModel(
            name='CellType',
        ),
    ]