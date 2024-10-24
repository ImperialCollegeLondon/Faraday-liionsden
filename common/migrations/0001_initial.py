# Generated by Django 3.2.7 on 2021-10-04 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import common.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('name', models.CharField(help_text='Organisation name', max_length=128, unique=True)),
                ('is_research', models.BooleanField(default=False)),
                ('is_publisher', models.BooleanField(default=False)),
                ('is_mfg_cells', models.BooleanField(default=False)),
                ('is_mfg_equip', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longName', models.CharField(help_text="Person's full name e.g. David Wallace Jones", max_length=128, unique=True)),
                ('shortName', models.CharField(help_text="Person's shortened name e.g. 'D.W. Jones'", max_length=128, unique=True)),
                ('org', models.ForeignKey(blank=True, help_text='Organisation that this person belongs to, if any.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.org')),
                ('user', models.OneToOneField(blank=True, help_text='User account in the system, if any.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('DOI', common.models.DOIField(blank=True, help_text='DOI for the paper.', max_length=128, null=True, unique=True)),
                ('year', common.models.YearField(default=2021)),
                ('title', models.CharField(default='', max_length=300)),
                ('authors', models.CharField(default='', max_length=300)),
                ('url', models.URLField(blank=True, null=True)),
                ('PDF', models.FileField(blank=True, help_text='Optional PDF copy', null=True, upload_to='')),
                ('publisher', models.ForeignKey(blank=True, limit_choices_to={'is_publisher': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.org')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
