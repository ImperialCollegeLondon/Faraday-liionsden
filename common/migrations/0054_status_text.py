# Generated by Django 3.1.2 on 2020-12-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0053_status_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("submitted", "Submitted"),
                    ("accepted", "Accepted"),
                    ("published", "Published"),
                    ("deleted", "Deleted"),
                ],
                default="draft",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="uploadedfile",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("submitted", "Submitted"),
                    ("accepted", "Accepted"),
                    ("published", "Published"),
                    ("deleted", "Deleted"),
                ],
                default="draft",
                max_length=16,
            ),
        ),
    ]
