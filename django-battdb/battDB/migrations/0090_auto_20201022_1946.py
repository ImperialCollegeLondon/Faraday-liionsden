# Generated by Django 3.1.2 on 2020-10-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0089_auto_20201022_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduledevice',
            name='device',
        ),
        migrations.RemoveField(
            model_name='moduledevice',
            name='module',
        ),
        migrations.DeleteModel(
            name='CompositeDevice',
        ),
        migrations.DeleteModel(
            name='ModuleDevice',
        ),
    ]
