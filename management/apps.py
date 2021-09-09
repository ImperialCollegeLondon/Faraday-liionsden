from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'management'

    # Populate database with predefined roles
    def ready(self):
        from .signals import populate_groups
        post_migrate.connect(populate_groups, sender=self)