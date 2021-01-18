# Generated by Django 3.1.4 on 2021-01-18 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0206_auto_20201230_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datacolumn',
            options={},
        ),
        migrations.AddField(
            model_name='datacolumn',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='battDB.experimentdatafile'),
        ),
        migrations.AlterUniqueTogether(
            name='datacolumn',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='datacolumn',
            name='data_file',
        ),
        migrations.RemoveField(
            model_name='datacolumn',
            name='device',
        ),
    ]
