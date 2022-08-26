# Generated by Django 4.1 on 2022-08-24 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0011_alter_component_polymer'),
        ('battDB', '0025_alter_deviceparameter_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('inherit_to_children', models.BooleanField(default=False)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dfndb.component')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battDB.devicespecification')),
            ],
            options={
                'unique_together': {('spec', 'name'), ('spec', 'component')},
            },
        ),
    ]
