# Generated by Django 3.2.7 on 2021-10-04 10:44

import datetime

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dfndb', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('inherit_metadata', models.BooleanField(default=True, help_text='Set to True if this object does not describe a real life thing, but a specification, type or grouping. In this case, the metadata will be inherited.', verbose_name='Inherit metadata attributes from parent')),
                ('serialNo', models.CharField(blank=True, default='%d', help_text='Batch number, optionally indicate serial number format', max_length=60)),
                ('batch_size', models.PositiveSmallIntegerField(default=1)),
                ('manufactured_on', models.DateField(default=datetime.datetime.now)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('manufacturer', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.org')),
                ('manufacturing_protocol', models.ForeignKey(blank=True, help_text='Test protocol used in this experiment', limit_choices_to={'type': 3000}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.method')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent node in object tree hierarchy', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.batch')),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='DeviceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('config_type', models.CharField(choices=[('module', 'Module'), ('expmt', 'Experiment')], default='module', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Device Configurations',
            },
        ),
        migrations.CreateModel(
            name='DeviceParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('value', models.JSONField(blank=True, null=True)),
                ('inherit_to_children', models.BooleanField(default=False)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dfndb.material')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('inherit_metadata', models.BooleanField(default=True, help_text='Set to True if this object does not describe a real life thing, but a specification, type or grouping. In this case, the metadata will be inherited.', verbose_name='Inherit metadata attributes from parent')),
                ('abstract', models.BooleanField(default=False, help_text="\n        This specifies an abstract device, e.g. 'Cell' with child members\n        such as 'Positive Electrode, Negative Electrode, Electrolyte etc. \n        If this is set to True, then all metadata declared here must be \n        overridden in child classes. An abstract specification cannot be used\n        to define a physical device or batch.\n        ", verbose_name='Abstract Specification')),
                ('complete', models.BooleanField(default=False, help_text='This device is complete - it can be used in experiments without a parent')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('device_type', models.ForeignKey(blank=True, help_text='Device type. e.g. Cell, Module, Battery Pack. An abstract \n        specification cannot have a device type -  they define the device types.', limit_choices_to={'abstract': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specifies', to='battDB.devicespecification')),
                ('parameters', models.ManyToManyField(through='battDB.DeviceParameter', to='dfndb.Parameter')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent node in object tree hierarchy', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.devicespecification')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Device Specifications',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('serialNo', models.CharField(blank=True, default='', help_text='Batch number, optionally indicate serial number format', max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Equipment',
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('protocol', models.TextField(blank=True, help_text='Test protocol used in this experiment', null=True)),
                ('config', models.ForeignKey(blank=True, help_text='All devices in the same experiment must be of the same configuration, i.e. an experiment must use all single cells, or all 2s2p modules, not a mixture of both.', limit_choices_to={'config_type': 'expmt'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_in', to='battDB.deviceconfig')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentDataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('ts_headers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, editable=False, help_text='Parsed data column headers', null=True, size=None)),
                ('ts_data', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), blank=True, editable=False, help_text='Parsed time-series data columns (note: this is bulky data!)', null=True, size=None)),
            ],
            options={
                'verbose_name': 'Data File',
            },
        ),
        migrations.CreateModel(
            name='Parser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('name', models.CharField(default='', max_length=128)),
                ('file_format', models.CharField(choices=[('none', 'None'), ('Dummy', 'Dummy parser that does nothing'), ('biologic', 'Biologic CSV/TSV/MPT'), ('maccor', 'Maccor XLS/XLSX')], default='none', help_text='File format', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('hash', models.CharField(editable=False, help_text='SHA-1 Hash of uploaded file. You cannot upload the same file twice.', max_length=64, unique=True)),
                ('local_path', models.CharField(blank=True, default='', max_length=1024)),
                ('local_date', models.DateTimeField(default=datetime.datetime.now)),
                ('parse', models.BooleanField(default=False, help_text='Set to True to import data on save')),
                ('parsed_metadata', models.JSONField(default=dict, editable=False, help_text='metadata automatically extracted from the file')),
                ('edf', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='raw_data_file', to='battDB.experimentdatafile')),
                ('use_parser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.parser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_name', models.CharField(default='', max_length=50)),
                ('order', models.PositiveSmallIntegerField(default=5, help_text='override column ordering')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.parameter')),
                ('parser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='battDB.parser')),
            ],
        ),
        migrations.AddField(
            model_name='parser',
            name='parameters',
            field=models.ManyToManyField(through='battDB.SignalType', to='dfndb.Parameter'),
        ),
        migrations.AddField(
            model_name='parser',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ExperimentDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_sequence', models.PositiveSmallIntegerField(default=1, help_text='sequence number of device within batch', validators=[django.core.validators.MinValueValidator(1)])),
                ('device_position', models.CharField(default='cell_xx', help_text='Device Position ID in Experiment Config - e.g. Cell_A1 for the first cell of a series-parallel pack', max_length=20)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.batch')),
                ('data_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.experimentdatafile')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='battDB.experiment')),
            ],
            options={
                'unique_together': {('device_position', 'data_file'), ('experiment', 'batch', 'batch_sequence', 'data_file')},
            },
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='devices',
            field=models.ManyToManyField(related_name='used_in', through='battDB.ExperimentDevice', to='battDB.Batch'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='experiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data_files', to='battDB.experiment'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='machine',
            field=models.ForeignKey(blank=True, help_text='Equipment on which this data was recorded', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.equipment'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='protocol',
            field=models.ForeignKey(blank=True, help_text='Test protocol used in this experiment', limit_choices_to={'type': 2000}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.method'),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipment',
            name='default_parser',
            field=models.ForeignKey(blank=True, help_text="Default parser for this equipment's data", null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.parser'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='manufacturer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.org'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='specification',
            field=models.ForeignKey(help_text='Batch Specification', limit_choices_to={'abstract': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.devicespecification'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deviceparameter',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.devicespecification'),
        ),
        migrations.CreateModel(
            name='DeviceConfigNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_position_id', models.CharField(blank=True, help_text='Position of device in pack e.g. 1 - identifies this device', max_length=20, null=True)),
                ('pos_netname', models.CharField(blank=True, help_text='Name of electrical signal at positive terminal e.g. cell_1_v', max_length=20, null=True)),
                ('neg_netname', models.CharField(blank=True, help_text='Name of electrical signal at negative terminal e.g. pack_-ve', max_length=20, null=True)),
                ('config', models.ForeignKey(help_text='Config instance to which this node belongs', on_delete=django.db.models.deletion.CASCADE, to='battDB.deviceconfig')),
                ('device', models.ForeignKey(help_text='Related device specification e.g. cell or sensor.', limit_choices_to={'abstract': True}, on_delete=django.db.models.deletion.CASCADE, to='battDB.devicespecification')),
            ],
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='devices',
            field=models.ManyToManyField(through='battDB.DeviceConfigNode', to='battDB.DeviceSpecification'),
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batch',
            name='specification',
            field=models.ForeignKey(help_text='Batch Specification', limit_choices_to={'abstract': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.devicespecification'),
        ),
        migrations.AddField(
            model_name='batch',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='deviceparameter',
            unique_together={('spec', 'name'), ('spec', 'parameter', 'material')},
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('seq_num', models.PositiveSmallIntegerField(default=1, help_text='Sequence number within batch', validators=[django.core.validators.MinValueValidator(1)])),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.batch')),
            ],
            options={
                'unique_together': {('batch', 'seq_num')},
            },
        ),
        migrations.CreateModel(
            name='DataRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('file_offset_start', models.PositiveIntegerField(default=0)),
                ('file_offset_end', models.PositiveIntegerField(default=0)),
                ('label', models.CharField(default='all', max_length=32)),
                ('protocol_step', models.PositiveSmallIntegerField(default=0)),
                ('step_action', models.CharField(choices=[('chg', 'Charging'), ('dchg', 'Discharging'), ('cycle', 'Full cycle'), ('rest', 'Rest'), ('all', 'Entire series'), ('user', 'User defined')], default='all', max_length=8)),
                ('dataFile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ranges', to='battDB.experimentdatafile')),
            ],
            options={
                'verbose_name_plural': 'Data Ranges',
                'unique_together': {('dataFile', 'label')},
            },
        ),
        migrations.CreateModel(
            name='DataColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(default='Ns', max_length=40)),
                ('resample', models.CharField(choices=[('none', 'Do not resample'), ('on_change', 'Sample on change'), ('decimate', 'Take every Nth sample'), ('average', 'Average every Nth sample'), ('max', 'Maximum every Nth sample'), ('min', 'Minimum every Nth sample')], default='none', help_text='Resampling option - TO BE IMPLEMENTED - currently has no effect', max_length=10)),
                ('resample_n', models.PositiveSmallIntegerField(default=1, help_text='Resampling divisor - TO BE IMPLEMENTED', validators=[django.core.validators.MinValueValidator(1)])),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.experimentdatafile')),
                ('device', models.ForeignKey(blank=True, help_text='Device id for parameter mapping', null=True, on_delete=django.db.models.deletion.SET_NULL, to='battDB.experimentdevice')),
                ('parameter', models.ForeignKey(blank=True, help_text='Map this column to a parameter on a device', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.parameter')),
            ],
            options={
                'verbose_name': 'Column Mapping',
                'verbose_name_plural': 'Data Column Mappings to Device Parameters',
                'unique_together': {('column_name', 'data_file'), ('device', 'data_file')},
            },
        ),
    ]
