# Generated by Django 3.1.2 on 2020-10-18 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battDB', '0071_auto_20201017_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceConfigNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Unique name for this object', max_length=128, null=True, unique=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.devicetype')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='SignalType',
        ),
    ]