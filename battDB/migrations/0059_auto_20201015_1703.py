# Generated by Django 3.1.2 on 2020-10-15 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0058_auto_20201015_1653"),
    ]

    operations = [
        migrations.RemoveField(model_name="cell", name="created_on",),
        migrations.RemoveField(model_name="cell", name="modified_on",),
        migrations.RemoveField(model_name="cellbatch", name="created_on",),
        migrations.RemoveField(model_name="cellbatch", name="modified_on",),
        migrations.RemoveField(model_name="cellconfig", name="created_on",),
        migrations.RemoveField(model_name="cellconfig", name="modified_on",),
        migrations.RemoveField(model_name="celltype", name="created_on",),
        migrations.RemoveField(model_name="celltype", name="modified_on",),
        migrations.RemoveField(model_name="datarange", name="created_on",),
        migrations.RemoveField(model_name="datarange", name="modified_on",),
        migrations.RemoveField(model_name="equipment", name="created_on",),
        migrations.RemoveField(model_name="equipment", name="modified_on",),
        migrations.RemoveField(model_name="equipmenttype", name="created_on",),
        migrations.RemoveField(model_name="equipmenttype", name="modified_on",),
        migrations.RemoveField(model_name="experiment", name="created_on",),
        migrations.RemoveField(model_name="experiment", name="modified_on",),
        migrations.RemoveField(model_name="experimentdatafile", name="created_on",),
        migrations.RemoveField(model_name="experimentdatafile", name="modified_on",),
        migrations.RemoveField(model_name="rawdatafile", name="created_on",),
        migrations.RemoveField(model_name="rawdatafile", name="modified_on",),
        migrations.RemoveField(model_name="testprotocol", name="created_on",),
        migrations.RemoveField(model_name="testprotocol", name="modified_on",),
    ]
