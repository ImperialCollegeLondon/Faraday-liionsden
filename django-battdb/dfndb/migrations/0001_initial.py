# Generated by Django 3.1.2 on 2020-10-08 11:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositionPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('symbol', models.CharField(max_length=40, unique=True)),
                ('symbolName', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('symbol', models.CharField(max_length=40, unique=True)),
                ('type', models.IntegerField(choices=[(1, 'ParamType1'), (2, 'ParamType2')])),
                ('notes', models.TextField(blank=True)),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.quantityunit')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'Experimental'), (2, 'Modelling')])),
                ('description', models.TextField(blank=True)),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'Anode'), (2, 'Cathode'), (3, 'Electrolyte'), (4, 'Separator')])),
                ('polymer', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('composition', models.ManyToManyField(to='dfndb.CompositionPart')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'DataType1'), (2, 'DataType2')])),
                ('data', models.TextField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.material')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.paper')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.parameter')),
                ('user_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data',
            },
        ),
        migrations.AddField(
            model_name='compositionpart',
            name='compound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.compound'),
        ),
    ]
