# Generated by Django 3.1.2 on 2020-10-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0029_auto_20201016_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='method',
            name='name',
            field=models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True),
        ),
    ]
