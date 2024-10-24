# Generated by Django 4.1 on 2022-08-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0011_alter_component_polymer'),
        ('battDB', '0026_devicecomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicespecification',
            name='components',
            field=models.ManyToManyField(through='battDB.DeviceComponent', to='dfndb.component'),
        ),
    ]
