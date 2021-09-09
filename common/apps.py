from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CommonConfig(AppConfig):
    name = "common"

    # Populate database with predefined roles
    def ready(self):
        from .signals import populate_groups
        post_migrate.connect(populate_groups, sender=self)