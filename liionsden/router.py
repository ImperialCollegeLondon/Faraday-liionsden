class DBRouter:
    """
    A router to control all database operations on models in the
    user application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read research-related models go to research_db.
        """
        if model._meta.app_label == "research_data":
            return "research_db"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write research-related models go to research_db.
        """
        if model._meta.app_label == "research_data":
            return "research_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the research apps is involved.
        """
        if (
            obj1._meta.app_label == "research_data"
            or obj2._meta.app_label == "research_data"
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the research-related apps only appear in the 'research_db' database.
        """
        if app_label == "research_data":
            return db == "research_db"
        return None
