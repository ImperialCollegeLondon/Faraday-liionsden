from django.db.utils import IntegrityError
from django.test import TestCase

from model_bakery import baker


class TestCompound(TestCase):
    from dfndb.models import Compound

    model = Compound

    def setUp(self):
        self.expected = dict(name="Carbon Dioxide", formula="CO2", mass=44.01)
        self.model.objects.get_or_create(
            name="Carbon Dioxide", formula="CO2", mass=44.01
        )

    def test_compound_creation(self):
        obj = self.model.objects.get()
        for k, v in self.expected.items():
            self.assertEqual(getattr(obj, k), v)

    def test_str(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.__str__(), "Carbon Dioxide (CO2)")

    def test_unique_together(self):
        self.model.objects.create(name="Carbon Dioxide", formula="CO3", mass=44.01)

        self.assertRaises(
            IntegrityError,
            self.model.objects.create,
            name="Carbon Dioxide",
            formula="CO2",
            mass=44.01,
        )


class TestMaterial(TestCase):
    from dfndb.models import Material

    model = Material

    def setUp(self):
        from dfndb.models import CompositionPart, Compound

        cmp = Compound.objects.create(name="Carbon Dioxide", formula="CO2")
        cmp2 = Compound.objects.create(name="Sulphur", formula="S")
        mat = self.model.objects.create(name="Contaminant", type=1, polymer=0)
        CompositionPart.objects.create(compound=cmp, material=mat, amount=3)
        CompositionPart.objects.create(compound=cmp2, material=mat, amount=2)

    def test_material_creation(self):
        from dfndb.models import Compound

        name = "Carbon Dioxide"
        mat = self.model.objects.get()
        cmp = Compound.objects.get(name=name)

        self.assertEqual(mat.composition.all().count(), 2)
        self.assertEqual(mat.composition.get(name=name), cmp)
        self.assertEqual(mat.type, 1)
        self.assertEqual(mat.polymer, 0)

    def test_str(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.__str__(), "Contaminant")


class TestCompositionPart(TestCase):
    from dfndb.models import CompositionPart

    model = CompositionPart

    def setUp(self):
        from dfndb.models import Compound, Material

        self.amount = {"CO2": 3, "S": 2}
        cmp = Compound.objects.create(name="Carbon Dioxide", formula="CO2")
        cmp2 = Compound.objects.create(name="Sulphur", formula="S")
        mat = Material.objects.create(name="Contaminant", type=1, polymer=0)
        self.model.objects.create(compound=cmp, material=mat, amount=self.amount["CO2"])
        self.model.objects.create(compound=cmp2, material=mat, amount=self.amount["S"])

    def test_composition_part_creation(self):
        from dfndb.models import Compound, Material

        cmp = Compound.objects.get(name="Carbon Dioxide")
        mat = Material.objects.get()
        cp = self.model.objects.all().first()
        self.assertEqual(cp.compound, cmp)
        self.assertEqual(cp.material, mat)
        self.assertEqual(cp.amount, self.amount[cmp.formula])

    def test_percentage(self):
        cp = self.model.objects.all().first()
        expected = self.amount[cp.compound.formula] * 100 / sum(self.amount.values())
        self.assertEqual(cp.get_percentage(), expected)
        self.assertEqual(cp.percentage(), "%3.03f%%" % expected)

    def test_str(self):
        from dfndb.models import Compound

        cmp = Compound.objects.get(name="Carbon Dioxide")
        cp = self.model.objects.all().first()
        self.assertEqual(cp.__str__(), "%s%d" % (cmp.formula, cp.amount))

    def test_unique_together(self):
        cp = self.model.objects.all().first()
        self.model.objects.create(
            compound=cp.compound, material=cp.material, amount=cp.amount * 2
        )

        self.assertRaises(
            IntegrityError,
            self.model.objects.create,
            compound=cp.compound,
            material=cp.material,
            amount=cp.amount,
        )


class TestMethod(TestCase):
    from dfndb.models import Method

    model = Method

    def setUp(self):
        for k, v in self.model.METHOD_TYPE_CHOICES:
            self.model.objects.create(type=k, description=f"{v} method", name=v)

    def test_method_creation(self):
        choices = dict(self.model.METHOD_TYPE_CHOICES)
        methods = tuple(choices.keys())
        for obj in self.model.objects.all():
            self.assertIn(obj.type, methods)
            self.assertEqual(obj.name, choices[obj.type])
            self.assertIn(obj.name, obj.description)


class TestQuantityUnit(TestCase):
    from dfndb.models import QuantityUnit

    model = QuantityUnit

    def setUp(self):
        from tests.fixtures import db_unit

        self.expected = db_unit.copy()
        self.model.objects.create(**self.expected)

    def test_quantity_unit_creation(self):
        obj = self.model.objects.get()
        for k, v in self.expected.items():
            self.assertEqual(getattr(obj, k), v)
        self.assertIsNone(obj.related_unit)

    def test_str(self):
        obj = self.model.objects.get()
        self.assertEqual(
            obj.__str__(),
            "%s (%s) / %s"
            % (
                self.expected["quantityName"],
                self.expected["quantitySymbol"],
                self.expected["unitSymbol"],
            ),
        )

    def test_unique_together(self):
        self.expected["unitSymbol"] = "e"
        self.model.objects.create(**self.expected)
        self.assertRaises(IntegrityError, self.model.objects.create, **self.expected)


class TestParameter(TestCase):
    from dfndb.models import Parameter

    def setUp(self):
        from dfndb.models import QuantityUnit
        from tests.fixtures import db_unit

        unit = QuantityUnit.objects.create(**db_unit)
        self.expected = dict(name="Ionized donors", symbol="Nd-", unit=unit)
        self.model = baker.make_recipe("tests.dfndb.parameter", 
                                name="Ionized donors", 
                                symbol="Nd-", 
                                unit=unit
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
        from dfndb.models import QuantityUnit
        from tests.fixtures import db_unit
        self.expected["symbol"] = "Na+"
        with self.assertRaises(IntegrityError):
            baker.make_recipe("tests.dfndb.parameter", symbol="Na+", 
            unit=QuantityUnit.objects.create(**db_unit))


class TestData(TestCase):
    from dfndb.models import Data

    model = Data

    def setUp(self):
        from common.models import Paper
        from dfndb.models import (
            CompositionPart,
            Compound,
            DataParameter,
            Material,
            Parameter,
            QuantityUnit,
        )
        from tests.fixtures import db_paper, db_unit

        unit = QuantityUnit.objects.create(**db_unit)
        param = Parameter.objects.create(name="Ionized donors", symbol="Nd-", unit=unit)
        cmp = Compound.objects.create(name="Carbon Dioxide", formula="CO2")
        mat = Material.objects.create(name="Contaminant", type=1, polymer=0)
        CompositionPart.objects.create(compound=cmp, material=mat, amount=3)
        paper = Paper.objects.create(**db_paper)
        data = self.model.objects.create(paper=paper)
        DataParameter.objects.create(
            data=data,
            parameter=param,
            type=DataParameter.PARAM_TYPE_NONE,
            material=mat,
            value={},
        )

    def test_data_creation(self):
        from common.models import Paper
        from dfndb.models import Parameter

        obj = self.model.objects.get()
        param = Parameter.objects.get()
        paper = Paper.objects.get()
        self.assertEqual(obj.paper, paper)
        self.assertEqual(obj.parameter.get(), param)


class TestDataParameter(TestCase):
    from dfndb.models import DataParameter

    model = DataParameter

    def setUp(self):
        from common.models import Paper
        from dfndb.models import (
            CompositionPart,
            Compound,
            Data,
            Material,
            Parameter,
            QuantityUnit,
        )
        from tests.fixtures import db_paper, db_unit

        unit = QuantityUnit.objects.create(**db_unit)
        param = Parameter.objects.create(name="Ionized donors", symbol="Nd-", unit=unit)
        cmp = Compound.objects.create(name="Carbon Dioxide", formula="CO2")
        mat = Material.objects.create(name="Contaminant", type=1, polymer=0)
        CompositionPart.objects.create(compound=cmp, material=mat, amount=3)
        paper = Paper.objects.create(**db_paper)
        data = Data.objects.create(paper=paper)
        self.model.objects.create(
            data=data,
            parameter=param,
            type=self.model.PARAM_TYPE_NONE,
            material=mat,
            value={},
        )

    def test_data_parameter_creation(self):
        from dfndb.models import Data, Material, Parameter

        data = Data.objects.get()
        param = Parameter.objects.get()
        mat = Material.objects.get()
        obj = self.model.objects.get()

        self.assertEqual(obj.data, data)
        self.assertEqual(obj.parameter, param)
        self.assertEqual(obj.material, mat)
        self.assertEqual(obj.value, {})
        self.assertIn(obj.type, list(zip(*self.model.PARAM_TYPE))[0])

    def test_str(self):
        from dfndb.models import Parameter

        param = Parameter.objects.get()
        self.assertEqual(self.model.objects.get().__str__(), str(param))
