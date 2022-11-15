import os

from django.db import migrations


def add_superuser(apps, schema_editor):
    User = apps.get_model("management", "User")
    User.objects.create_superuser("admin", password=os.environ["ADMIN_PASSWORD"])


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0003_user_institution"),
    ]

    operations = [migrations.RunPython(add_superuser)]
