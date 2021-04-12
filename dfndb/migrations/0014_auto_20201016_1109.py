# Generated by Django 3.1.2 on 2020-10-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfndb", "0013_auto_20201016_1054"),
    ]

    operations = [
        migrations.AddField(
            model_name="compound",
            name="mass",
            field=models.PositiveIntegerField(
                default=0, help_text="optional molar mass"
            ),
        ),
        migrations.AlterField(
            model_name="compound",
            name="formula",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="compound", name="name", field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name="compositionpart", unique_together={("compound", "amount")},
        ),
        migrations.AlterUniqueTogether(
            name="compound", unique_together={("name", "formula")},
        ),
    ]
