from django.contrib.admin.sites import AdminSite
from django.test import TestCase


class MockRequest:
    pass


request = MockRequest()


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
        from dfndb.models import DataParameter

        ma = DataParameterInline(DataParameter, self.site)
        self.assertEqual(ma.model, DataParameter)
        self.assertEqual(ma.get_extra(request), 1)
