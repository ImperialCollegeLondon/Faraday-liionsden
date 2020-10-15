# Generated by Django 3.1.2 on 2020-10-15 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0059_auto_20201015_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cell',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cellbatch',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cellbatch',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cellconfig',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cellconfig',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='celltype',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celltype',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='datarange',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datarange',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='equipmenttype',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmenttype',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experiment',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rawdatafile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawdatafile',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testprotocol',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testprotocol',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
