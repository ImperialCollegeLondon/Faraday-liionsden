# Generated by Django 3.1.2 on 2020-11-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0150_dataparser_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataparser',
            name='module',
            field=models.FileField(blank=True, default='', help_text='Python module to run this parser', upload_to=''),
        ),
    ]