# Generated by Django 3.1.2 on 2020-10-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0112_experimentdatafile_parsed_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentdatafile',
            name='parsed_data',
            field=models.JSONField(default=dict, editable=False),
        ),
    ]
