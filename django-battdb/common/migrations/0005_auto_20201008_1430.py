# Generated by Django 3.1.2 on 2020-10-08 14:30

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20201008_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='DOI',
            field=common.models.DOIField(blank=True, help_text='Paper DOI. In future, this could populate the other fields automatically.', max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='accepted',
            field=models.BooleanField(default=False, help_text='Has this paper been accepted for publication?'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='org_owners',
            field=models.ManyToManyField(help_text='Contributing Organisations.', related_name='papers', to='common.Org'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='tag',
            field=models.SlugField(help_text="Tag or 'slug' used to uniquely identify this paper. This will be auto-generated in future versions.", max_length=100, unique=True),
        ),
    ]
