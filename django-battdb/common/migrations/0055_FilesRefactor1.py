# Generated by Django 3.1.2 on 2020-12-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0199_FilesRefactor1'),
        ('common', '0054_status_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
