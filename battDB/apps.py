from django.apps import AppConfig


class BattdbConfig(AppConfig):
    name = "battDB"

    def ready(self):
        import battDB.signals.handlers
