# Generated by Django 4.1.3 on 2022-11-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0032_alter_experimentdevice_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentdatafile',
            name='devices',
            field=models.ManyToManyField(related_name='data_files', to='battDB.device'),
        ),
    ]