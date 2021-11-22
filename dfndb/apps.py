from django.apps import AppConfig


class DfndbConfig(AppConfig):
    name = "dfndb"

    def ready(self):
        import dfndb.signals.handlers
