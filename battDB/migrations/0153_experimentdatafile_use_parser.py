# Generated by Django 3.1.2 on 2020-11-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("battDB", "0152_auto_20201102_1733"),
    ]

    operations = [
        migrations.AddField(
            model_name="experimentdatafile",
            name="use_parser",
            field=models.CharField(
                choices=[
                    ("none", "None"),
                    ("auto", "Auto-detect"),
                    ("csv", "Generic CSV/TSV"),
                    ("biologic", "Biologic CSV/TSV/MPT"),
                    ("maccor", "Maccor XLS/XLSX"),
                    ("ivium", "Ivium TXT"),
                    ("novonix", "Novonix TXT"),
                ],
                default="auto",
                help_text="Parser to use for this DataFile",
                max_length=20,
            ),
        ),
    ]
