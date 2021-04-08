# Generated by Django 3.1.2 on 2020-12-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0040_status_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='material',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='method',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
        migrations.AddField(
            model_name='parameter',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('published', 'Published'), ('deleted', 'Deleted')], default='draft', max_length=16),
        ),
    ]