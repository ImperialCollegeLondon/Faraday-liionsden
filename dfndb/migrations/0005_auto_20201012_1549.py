# Generated by Django 3.1.2 on 2020-10-12 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dfndb", "0004_auto_20201012_1126"),
    ]

    operations = [
        migrations.RemoveField(model_name="data", name="name",),
        migrations.RemoveField(model_name="material", name="name",),
        migrations.RemoveField(model_name="method", name="name",),
        migrations.RemoveField(model_name="parameter", name="name",),
        migrations.AlterField(
            model_name="data",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (10, "Draft"),
                    (20, "Submitted"),
                    (30, "Accepted"),
                    (40, "Published"),
                    (50, "Deleted"),
                ],
                default=10,
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="user_owner",
            field=models.ForeignKey(
                blank=True,
                help_text="leave blank for default user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="material",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (10, "Draft"),
                    (20, "Submitted"),
                    (30, "Accepted"),
                    (40, "Published"),
                    (50, "Deleted"),
                ],
                default=10,
            ),
        ),
        migrations.AlterField(
            model_name="material",
            name="user_owner",
            field=models.ForeignKey(
                blank=True,
                help_text="leave blank for default user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="method",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (10, "Draft"),
                    (20, "Submitted"),
                    (30, "Accepted"),
                    (40, "Published"),
                    (50, "Deleted"),
                ],
                default=10,
            ),
        ),
        migrations.AlterField(
            model_name="method",
            name="user_owner",
            field=models.ForeignKey(
                blank=True,
                help_text="leave blank for default user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="parameter",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (10, "Draft"),
                    (20, "Submitted"),
                    (30, "Accepted"),
                    (40, "Published"),
                    (50, "Deleted"),
                ],
                default=10,
            ),
        ),
        migrations.AlterField(
            model_name="parameter",
            name="user_owner",
            field=models.ForeignKey(
                blank=True,
                help_text="leave blank for default user",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
