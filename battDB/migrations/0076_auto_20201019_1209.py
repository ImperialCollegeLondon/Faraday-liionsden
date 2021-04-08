# Generated by Django 3.1.2 on 2020-10-19 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0030_auto_20201018_2254'),
        ('battDB', '0075_auto_20201018_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='protocol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.method'),
        ),
        migrations.DeleteModel(
            name='TestProtocol',
        ),
    ]