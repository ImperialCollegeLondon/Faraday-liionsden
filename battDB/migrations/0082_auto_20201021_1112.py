# Generated by Django 3.1.2 on 2020-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0081_auto_20201020_1018"),
    ]

    operations = [
        migrations.RenameField(
            model_name="device", old_name="type", new_name="devType",
        ),
        migrations.AlterField(
            model_name="device",
            name="is_template",
            field=models.BooleanField(
                default=False,
                help_text="Set to true if this object does not describe a real device, but a specification or type of devices",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="slug",
            field=models.SlugField(
                default="autogenerated",
                editable=False,
                help_text="Auto-generated unique name, can be used in URLs",
            ),
        ),
        migrations.AlterField(
            model_name="deviceconfig",
            name="slug",
            field=models.SlugField(
                default="autogenerated",
                editable=False,
                help_text="Auto-generated unique name, can be used in URLs",
            ),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="slug",
            field=models.SlugField(
                default="autogenerated",
                editable=False,
                help_text="Auto-generated unique name, can be used in URLs",
            ),
        ),
        migrations.AlterField(
            model_name="rawdatafile",
            name="slug",
            field=models.SlugField(
                default="autogenerated",
                editable=False,
                help_text="Auto-generated unique name, can be used in URLs",
            ),
        ),
        migrations.DeleteModel(name="Cell",),
        migrations.CreateModel(
            name="Cell",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("battDB.device",),
        ),
    ]
