# Generated by Django 3.1.2 on 2020-10-12 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battDB', '0044_auto_20201012_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cell',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cellbatch',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cellconfig',
            name='name',
        ),
        migrations.RemoveField(
            model_name='celltype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='equipmenttype',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='equipmenttype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='experimentalapparatus',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testprotocol',
            name='name',
        ),
        migrations.AlterField(
            model_name='cell',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='cell',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cellbatch',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='cellbatch',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cellconfig',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='cellconfig',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='celltype',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='celltype',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipmenttype',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='equipmenttype',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experimentalapparatus',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='experimentalapparatus',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testprotocol',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='testprotocol',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional metadata')),
                ('user_owner', models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional metadata')),
                ('user_owner', models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional metadata')),
                ('user_owner', models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
