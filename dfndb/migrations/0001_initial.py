# Generated by Django 3.2.7 on 2021-09-14 13:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompositionPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full name for the element or compound', max_length=100)),
                ('formula', models.CharField(help_text='Chemical formula', max_length=20)),
                ('mass', models.FloatField(default=0, help_text='Optional molar mass, in g/mol', validators=[django.core.validators.MinValueValidator(0, 'Mass cannot be negative!')])),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Data',
            },
        ),
        migrations.CreateModel(
            name='DataParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(10, 'None'), (20, 'Input'), (30, 'Output')], default=10)),
                ('value', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Anode'), (2, 'Cathode'), (3, 'Electrolyte'), (4, 'Separator')])),
                ('polymer', models.PositiveIntegerField(default=0, help_text='If this material is a polymer, enter degree of polymerization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('type', models.IntegerField(choices=[(2000, 'Experimental'), (1000, 'Modelling'), (3000, 'Manufacture')], default=1000)),
                ('description', models.TextField(blank=True, help_text='Method description in PyBaMM format')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuantityUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityName', models.CharField(help_text="Readable name e.g. 'Charge'", max_length=100)),
                ('quantitySymbol', models.CharField(help_text="e.g. 'Q', Will be decoded as LaTeX", max_length=40)),
                ('unitName', models.CharField(blank=True, help_text="e.g. 'Coulombs'", max_length=40)),
                ('unitSymbol', models.CharField(help_text="e.g. 'C'", max_length=40)),
                ('is_SI_unit', models.BooleanField(default=False)),
                ('related_scale', models.FloatField(blank=True, help_text='Scaling of this unit from the SI unit', null=True)),
                ('related_unit', models.ForeignKey(blank=True, help_text='If this unit is NOT an SI unit, it should relate to one', limit_choices_to={'is_SI_unit': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.quantityunit')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('attributes', models.JSONField(blank=True, default=dict, help_text='Optional machine-readable JSON metadata')),
                ('notes', models.TextField(blank=True, help_text='Optional human-readable notes', null=True)),
                ('slug', models.SlugField(default='autogenerated', editable=False, help_text='Auto-generated unique name, can be used in URLs', max_length=500)),
                ('symbol', models.CharField(help_text='Parameter symbol. Will be decoded as LaTeX', max_length=40)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dfndb.quantityunit')),
            ],
        ),
    ]
