# Generated by Django 3.1.2 on 2020-10-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0110_auto_20201028_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentdatafile',
            name='file_hash',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]