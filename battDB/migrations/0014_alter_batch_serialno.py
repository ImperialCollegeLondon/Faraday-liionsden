# Generated by Django 4.0.1 on 2022-01-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0013_alter_batch_serialno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='serialNo',
            field=models.CharField(blank=True, help_text='Batch number or some other unique identifier', max_length=60),
        ),
    ]
