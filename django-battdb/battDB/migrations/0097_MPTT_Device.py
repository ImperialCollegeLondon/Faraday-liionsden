# Generated by Django 3.1.2 on 2020-10-26 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0044_MPTT_Device'),
        ('dfndb', '0033_auto_20201021_1112'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battDB', '0096_MPTT_Thing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('thing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.thing')),
                ('devType', models.PositiveSmallIntegerField(choices=[('cell', 'Single cell'), ('module', 'Module containing multiple cells'), ('battery', 'Battery containing cells OR modules'), ('sensor', 'Sensor attached to a device'), ('cycler', 'Cycler Machine')], default='cell')),
                ('serialNo', models.CharField(blank=True, help_text='Serial Number - or format, for device templates', max_length=60, null=True)),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.org')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.thing',),
        ),
        migrations.CreateModel(
            name='DeviceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name for this object', max_length=128, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs')),
                ('date', models.DateField()),
                ('config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_in', to='battDB.deviceconfig')),
                ('device', models.ManyToManyField(related_name='used_in', to='battDB.Device')),
                ('protocol', models.ForeignKey(blank=True, limit_choices_to={'type': 2000}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.method')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceConfigNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_position_id', models.CharField(blank=True, help_text='Position of device in pack e.g. 1 - identifies this device', max_length=20, null=True)),
                ('device_terminal_name', models.CharField(blank=True, help_text="Name of device port or terminal. e.g. 'Anode'", max_length=10, null=True)),
                ('net_name', models.CharField(blank=True, help_text='Name of electrical signal e.g. cell_1_v', max_length=20, null=True)),
                ('config', models.ForeignKey(help_text='Config instance to which this node belongs', on_delete=django.db.models.deletion.CASCADE, to='battDB.deviceconfig')),
                ('device', models.ForeignKey(help_text='Related device specification e.g. cell or sensor. Must have is_template=True', limit_choices_to={'is_template': True}, on_delete=django.db.models.deletion.CASCADE, to='battDB.device')),
                ('next', models.ForeignKey(blank=True, help_text='Connected node in chain. Must be part of the same config.In a series pack, this would be the negative terminal of the next cell', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.deviceconfignode')),
            ],
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='devices',
            field=models.ManyToManyField(through='battDB.DeviceConfigNode', to='battDB.Device'),
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('battDB.device',),
        ),
    ]
