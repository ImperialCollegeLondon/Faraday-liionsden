# Generated by Django 3.1.2 on 2020-10-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0056_rawdatafile_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdatafile',
            name='file_hash',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]