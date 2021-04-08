# Generated by Django 3.1.2 on 2020-11-02 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0051_SlugFieldMaxLen500'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Draft'), (20, 'Submitted'), (30, 'Accepted'), (40, 'Published'), (50, 'Deleted')], default=10),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='user_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='hash',
            field=models.CharField(editable=False, help_text='SHA-1 Hash of uploaded file. You cannot upload the same file twice.', max_length=64, unique=True),
        ),
    ]