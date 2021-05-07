from django.test import TestCase


class TestParameterSerializer(TestCase):
    from dfndb.serializers import ParameterSerializer

    model = ParameterSerializer

    def test_meta(self):
        from dfndb.models import Parameter

        self.assertEqual(self.model.Meta.model, Parameter)
        self.assertEqual(self.model.Meta.exclude, [])
