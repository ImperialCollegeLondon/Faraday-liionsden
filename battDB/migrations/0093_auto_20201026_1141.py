# Generated by Django 3.1.2 on 2020-10-26 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0092_auto_20201022_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='config',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_in', to='battDB.deviceconfig'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='device',
            field=models.ManyToManyField(related_name='used_in', to='battDB.Device'),
        ),
    ]