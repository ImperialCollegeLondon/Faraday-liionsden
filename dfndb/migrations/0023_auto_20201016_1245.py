# Generated by Django 3.1.2 on 2020-10-16 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0022_auto_20201016_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantityunit',
            name='quantityName',
            field=models.CharField(help_text="Readable name e.g. 'Charge'", max_length=100),
        ),
        migrations.AlterField(
            model_name='quantityunit',
            name='quantitySymbol',
            field=models.CharField(help_text="e.g. 'Q', Will be decoded as LaTeX", max_length=40),
        ),
        migrations.AlterField(
            model_name='quantityunit',
            name='related_unit',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_SI_unit': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dfndb.quantityunit'),
        ),
        migrations.AlterField(
            model_name='quantityunit',
            name='unitSymbol',
            field=models.CharField(help_text="e.g. 'C'", max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='quantityunit',
            unique_together={('quantityName', 'unitSymbol')},
        ),
    ]