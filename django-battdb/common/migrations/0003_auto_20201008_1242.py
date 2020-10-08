# Generated by Django 3.1.2 on 2020-10-08 12:42

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_paper_org_owners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='paper_tag',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='paper',
            name='DOI',
            field=common.models.DOIField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
