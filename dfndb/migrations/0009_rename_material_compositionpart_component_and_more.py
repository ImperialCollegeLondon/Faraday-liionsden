# Generated by Django 4.0.2 on 2022-02-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfndb', '0008_rename_material_component'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compositionpart',
            old_name='material',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='dataparameter',
            old_name='material',
            new_name='component',
        ),
        migrations.AlterField(
            model_name='component',
            name='polymer',
            field=models.PositiveIntegerField(default=0, help_text='If this component is a polymer, enter degree of polymerization'),
        ),
        migrations.AlterUniqueTogether(
            name='compositionpart',
            unique_together={('compound', 'amount', 'component')},
        ),
        migrations.AlterUniqueTogether(
            name='dataparameter',
            unique_together={('data', 'parameter', 'component')},
        ),
    ]
