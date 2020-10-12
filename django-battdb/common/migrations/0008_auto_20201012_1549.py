# Generated by Django 3.1.2 on 2020-10-12 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0007_auto_20201012_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='name',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='paper',
            name='attributes',
            field=models.JSONField(blank=True, default=dict, help_text='Optional metadata'),
        ),
        migrations.AddField(
            model_name='paper',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AddField(
            model_name='paper',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='org',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='org',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_owner',
            field=models.ForeignKey(blank=True, help_text='leave blank for default user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
