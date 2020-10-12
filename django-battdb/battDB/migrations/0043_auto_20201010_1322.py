# Generated by Django 3.1.2 on 2020-10-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20201008_1430'),
        ('battDB', '0042_auto_20201010_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmenttype',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.org'),
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]
