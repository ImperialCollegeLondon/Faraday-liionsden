from django.db.utils import IntegrityError
from django.test import TestCase
from model_bakery import baker

from dfndb.models import Data


class TestCompound(TestCase):
    def setUp(self):
        self.expected = dict(name="Carbon Dioxide", formula="CO2", mass=44.01)
        self.model = baker.make_recipe(
            "tests.dfndb.compound", name="Carbon Dioxide", formula="CO2", mass=44.01
        )

    def test_compound_creation(self):
        for k, v in self.expected.items():
            self.assertEqual(getattr(self.model, k), v)

    def test_str(self):
        self.assertEqual(self.model.__str__(), "Carbon Dioxide (CO2)")

    def test_unique_together(self):
        baker.make_recipe(
            "tests.dfndb.compound", name="Carbon Dioxide", formula="CO3", mass=44.01
        )
        with self.assertRaises(IntegrityError):
            baker.make_recipe(
                "tests.dfndb.compound", name="Carbon Dioxide", formula="CO2", mass=44.01
            )


class TestComponent(TestCase):
    def setUp(self):
        comp = baker.make_recipe(
            "tests.dfndb.compound", name="Carbon Dioxide", formula="CO2"
        )
        comp2 = baker.make_recipe("tests.dfndb.compound", name="Sulphur", formula="S")
        self.model = baker.make_recipe(
            "tests.dfndb.component", name="Contaminant", type=1, polymer=0
        )
        baker.make_recipe(
            "tests.dfndb.composition_part",
            compound=comp,
            component=self.model,
            amount=3,
        )
        baker.make_recipe(
            "tests.dfndb.composition_part",
            compound=comp2,
            component=self.model,
            amount=2,
        )

    def test_component_creation(self):
        from dfndb.models import Compound

        name = "Carbon Dioxide"
        cmp = Compound.objects.get(name=name)

        self.assertEqual(self.model.composition.all().count(), 2)
        self.assertEqual(self.model.composition.get(name=name), cmp)
        self.assertEqual(self.model.type, 1)
        self.assertEqual(self.model.polymer, 0)

    def test_str(self):
        self.assertEqual(self.model.__str__(), "Contaminant")


class TestCompositionPart(TestCase):
    def setUp(self):
        self.amount = {"CO2": 3, "S": 2}
        comp = baker.make_recipe(
            "tests.dfndb.compound", name="Carbon Dioxide", formula="CO2"
        )
        mat = baker.make_recipe("tests.dfndb.component")
        self.model = baker.make_recipe(
            "tests.dfndb.composition_part", compound=comp, component=mat, amount=3
        )
        baker.make_recipe("tests.dfndb.composition_part", component=mat, amount=2)

    def test_composition_part_creation(self):
        from dfndb.models import Component, Compound

        comp = Compound.objects.get(name="Carbon Dioxide")
        mat = Component.objects.get()
        self.assertEqual(self.model.compound, comp)
        self.assertEqual(self.model.component, mat)
        self.assertEqual(self.model.amount, self.amount[comp.formula])

    def test_percentage(self):
        expected = (
            self.amount[self.model.compound.formula] * 100 / sum(self.amount.values())
        )
        self.assertEqual(self.model.get_percentage(), expected)
        self.assertEqual(self.model.percentage(), "%3.03f%%" % expected)

    def test_str(self):
        from dfndb.models import Compound

        comp = Compound.objects.get(name="Carbon Dioxide")
        self.assertEqual(
            self.model.__str__(), "%s%d" % (comp.formula, self.model.amount)
        )

    def test_unique_together(self):
        baker.make_recipe(
            "tests.dfndb.composition_part",
            compound=self.model.compound,
            component=self.model.component,
            amount=self.model.amount * 2,
        )

        with self.assertRaises(IntegrityError):
            baker.make_recipe(
                "tests.dfndb.composition_part",
                compound=self.model.compound,
                component=self.model.component,
                amount=self.model.amount,
            )


class TestMethod(TestCase):
    def setUp(self):
        from dfndb.models import Method

        self.model = Method
        for k, v in self.model.METHOD_TYPE_CHOICES:
            baker.make_recipe(
                "tests.dfndb.method", type=k, description=[f"{v} method"], name=v
            )

    def test_method_creation(self):
        choices = dict(self.model.METHOD_TYPE_CHOICES)
        methods = tuple(choices.keys())
        for obj in self.model.objects.all():
            self.assertIn(obj.type, methods)
            self.assertEqual(obj.name, choices[obj.type])
            self.assertIn(obj.name, obj.description[0])


class TestQuantityUnit(TestCase):
    def setUp(self):
        self.expected = dict(
            quantityName="Depth",
            quantitySymbol="D",
            unitName="Light years",
            unitSymbol="LY",
            is_SI_unit=True,
        )
        self.model = baker.make_recipe("tests.dfndb.quantity_unit", **self.expected)

    def test_quantity_unit_creation(self):
        for k, v in self.expected.items():
            self.assertEqual(getattr(self.model, k), v)
        self.assertIsNone(self.model.related_unit)

    def test_str(self):
        self.assertEqual(
            self.model.__str__(),
            "%s (%s) / %s"
            % (
                self.expected["quantityName"],
                self.expected["quantitySymbol"],
                self.expected["unitSymbol"],
            ),
        )

    def test_unique_together(self):
        expected = self.expected.copy()
        expected["unitSymbol"] = "ly"
        baker.make_recipe("tests.dfndb.quantity_unit", **expected)
        with self.assertRaises(IntegrityError):
            baker.make_recipe("tests.dfndb.quantity_unit", **self.expected)


class TestParameter(TestCase):
    def setUp(self):
        self.unit = baker.make_recipe("tests.dfndb.quantity_unit")
        self.expected = dict(name="Ionized donors", symbol="Nd-", unit=self.unit)
        self.model = baker.make_recipe(
            "tests.dfndb.parameter", name="Ionized donors", symbol="Nd-", unit=self.unit
        )

    def test_parameter_creation(self):
        for k, v in self.expected.items():
            self.assertEqual(getattr(self.model, k), v)

    def test_str(self):
        self.assertEqual(
            self.model.__str__(),
            "%s: %s / %s"
            % (
                self.expected["name"],
                self.expected["symbol"],
                self.expected["unit"].unitSymbol,
            ),
        )

    def test_unique_together(self):
        baker.make_recipe(
            "tests.dfndb.parameter", name="Ionized donors", symbol="Na+", unit=self.unit
        )
        with self.assertRaises(IntegrityError):
            baker.make_recipe(
                "tests.dfndb.parameter",
                name="Ionized donors",
                symbol="Nd-",
                unit=self.unit,
            )


class TestData(TestCase):
    def setUp(self):
        self.parameter = baker.make_recipe("tests.dfndb.parameter", _quantity=2)
        self.reference = baker.make_recipe("tests.common.reference")
        self.model = baker.make_recipe(
            "tests.dfndb.data",
            reference=self.reference,
            parameter=self.parameter,
            make_m2m=True,
        )

    def test_data_creation(self):
        self.assertEqual(self.model.reference, self.reference)
        self.assertIn(self.model.parameter.get_queryset().first(), self.parameter)


class TestDataParameter(TestCase):
    def setUp(self):
        from dfndb.models import DataParameter

        model = DataParameter

        self.param = baker.make_recipe("tests.dfndb.parameter")
        self.mat = baker.make_recipe("tests.dfndb.component")
        self.data = baker.make_recipe("tests.dfndb.data")
        self.model = baker.make_recipe(
            "tests.dfndb.data_parameter",
            data=self.data,
            parameter=self.param,
            type=model.PARAM_TYPE_NONE,
            component=self.mat,
            value={},
        )

    def test_data_parameter_creation(self):
        from dfndb.models import DataParameter

        model = DataParameter

        self.assertEqual(self.model.data, self.data)
        self.assertEqual(self.model.parameter, self.param)
        self.assertEqual(self.model.component, self.mat)
        self.assertEqual(self.model.value, {})
        self.assertIn(self.model.type, list(zip(*model.PARAM_TYPE))[0])

    def test_str(self):
        self.assertEqual(self.model.__str__(), str(self.param))
