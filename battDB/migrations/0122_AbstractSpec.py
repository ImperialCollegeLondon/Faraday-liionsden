# Generated by Django 3.1.2 on 2020-10-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battDB', '0121_Docstrings'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicespecification',
            name='abstract',
            field=models.BooleanField(default=False, help_text='If this is set to True, then all metadata declared here must be overridden in child classes. An abstract specification cannot be used to define a physical device or batch. <BR>There should be at least one abstract specification in the database for each device type listed above.'),
        ),
    ]