# Generated by Django 4.0 on 2021-12-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0012_alter_batch_serialno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='serialNo',
            field=models.CharField(blank=True, default='20211210-090158', help_text='Batch number, default is date-time stamp', max_length=60),
        ),
    ]