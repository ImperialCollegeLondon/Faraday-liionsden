# Generated by Django 4.1.3 on 2022-12-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0016_alter_compound_unique_together_alter_component_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='polymer',
        ),
    ]
