# Generated by Django 3.1.2 on 2020-10-12 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battDB', '0051_auto_20201012_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarange',
            name='attributes',
            field=models.JSONField(blank=True, default=dict, help_text='Optional metadata'),
        ),
        migrations.AddField(
            model_name='datarange',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarange',
            name='name',
            field=models.CharField(blank=True, help_text='Unique name for this object', max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='datarange',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AddField(
            model_name='datarange',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='attributes',
            field=models.JSONField(blank=True, default=dict, help_text='Optional metadata'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='name',
            field=models.CharField(blank=True, help_text='Unique name for this object', max_length=128, null=True, unique=True),
        ),
    ]