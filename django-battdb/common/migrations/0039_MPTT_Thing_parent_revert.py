# Generated by Django 3.1.2 on 2020-10-26 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0038_MPTT_Thing_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='part_of',
            new_name='parent',
        ),
    ]
