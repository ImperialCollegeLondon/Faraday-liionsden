# Generated by Django 3.1.2 on 2020-10-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20201008_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'University'), (2, 'Publisher')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.org'),
        ),
    ]
