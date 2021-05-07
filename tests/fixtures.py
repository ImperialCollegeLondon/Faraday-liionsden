from django.db import connection
from django.db.models.base import ModelBase
from django.db.utils import ProgrammingError
from django.test import TestCase

db_user = dict(
    username="MichaelF",
    first_name="Michael",
    last_name="Faraday",
    password="C@cina27",
)

db_unit = dict(
    quantityName="Charge",
    quantitySymbol="Q",
    unitName="Coulombs",
    unitSymbol="C",
    is_SI_unit=True,
)

db_paper = dict(
    authors="Michael Faraday",
    title="Chemical Manipulation, Being Instructions to Students in Chemistry",
    year=1827,
)


class AbstractModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins/abstract models.
    To use, subclass and specify the mixin class variable.
    A model using the mixin will be made available in self.model
    """

    mixin: ModelBase
    model: ModelBase

    @classmethod
    def setUpClass(cls):
        """Create a dummy model or a schema for our model which extends the mixin.

        A RuntimeWarning will occur if the model is registered twice. If the table
        already exists, will pass.
        """
        if not hasattr(cls, "model"):
            cls.model = ModelBase(
                "__TestModel__" + cls.mixin.__name__,
                (cls.mixin,),
                {"__module__": cls.mixin.__module__},
            )

        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(cls.model)
            super(AbstractModelMixinTestCase, cls).setUpClass()
        except ProgrammingError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Delete the schema for the test model. If no table, will pass"""
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.delete_model(cls.model)
            super(AbstractModelMixinTestCase, cls).tearDownClass()
        except ProgrammingError:
            pass
