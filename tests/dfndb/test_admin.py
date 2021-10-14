from unittest.mock import MagicMock

from django.contrib.admin.sites import AdminSite, site
from django.test import TestCase

request = MagicMock()


class TestMaterialCompositionInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_material_composition_inline(self):
        from dfndb.admin import MaterialCompositionInline
        from dfndb.models import CompositionPart

        ma = MaterialCompositionInline(CompositionPart, self.site)
        self.assertEqual(ma.model, CompositionPart)
        self.assertEqual(ma.get_readonly_fields(request), ["percentage"])
        self.assertEqual(ma.get_extra(request), 0)


class TestDataParameterInline(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_data_parameter_inline(self):
        from dfndb.admin import DataParameterInline
        from dfndb.models import DataParameter, Parameter

        ma = DataParameterInline(DataParameter, self.site)
        self.assertEqual(ma.model, DataParameter)
        self.assertEqual(ma.get_extra(request), 1)
        self.assertTrue(site.is_registered(Parameter))


class TestMaterialAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_material_admin(self):
        from common.admin import BaseAdmin
        from dfndb.admin import MaterialAdmin
        from dfndb.models import Material

        ma = MaterialAdmin(Material, self.site)
        self.assertEqual(ma.model, Material)
        self.assertEqual(
            ma.get_list_display(request), BaseAdmin.list_display + ["type", "polymer"]
        )
        self.assertEqual(ma.get_list_filter(request), BaseAdmin.list_filter + ["type"])
        self.assertTrue(site.is_registered(Material))


class TestMethodAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_method_admin(self):
        from common.admin import BaseAdmin
        from dfndb.admin import MethodAdmin
        from dfndb.models import Method

        ma = MethodAdmin(Method, self.site)
        self.assertEqual(ma.model, Method)
        self.assertEqual(
            ma.get_list_display(request), BaseAdmin.list_display + ["type"]
        )
        self.assertEqual(ma.get_list_filter(request), BaseAdmin.list_filter + ["type"])
        self.assertTrue(site.is_registered(Method))


class TestDataAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_data_admin(self):
        from dfndb.admin import DataAdmin, DataParameterInline
        from dfndb.models import Data

        ma = DataAdmin(Data, self.site)
        self.assertEqual(ma.model, Data)
        self.assertEqual(ma.get_inlines(request, ...), (DataParameterInline,))
        self.assertTrue(site.is_registered(Data))


class TestUnitAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_unit_admin(self):
        from dfndb.admin import UnitAdmin
        from dfndb.models import QuantityUnit

        ma = UnitAdmin(QuantityUnit, self.site)
        self.assertEqual(ma.model, QuantityUnit)
        self.assertEqual(
            ma.get_list_display(request),
            ["__str__", "quantityName", "unitName", "is_SI_unit"],
        )
        self.assertEqual(ma.get_list_filter(request), ["is_SI_unit"])
        self.assertTrue(site.is_registered(QuantityUnit))


class TestCompoundAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_unit_admin(self):
        from dfndb.admin import CompoundAdmin
        from dfndb.models import Compound

        ma = CompoundAdmin(Compound, self.site)
        self.assertEqual(ma.model, Compound)
        self.assertEqual(ma.get_list_display(request), ["__str__"])
        self.assertTrue(site.is_registered(Compound))
