# Generated by Django 3.1.2 on 2020-12-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0193_status_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicebatch',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='deviceconfig',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='devicespecification',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='experiment',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='experimentdatafile',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='filefolder',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='harvester',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='parser',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
    ]