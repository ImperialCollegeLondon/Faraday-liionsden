# Generated by Django 3.1.2 on 2020-11-12 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0180_remove_harvester_upload_to_folder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='harvester',
            old_name='attach_to_equipment',
            new_name='equipment_type',
        ),
    ]
