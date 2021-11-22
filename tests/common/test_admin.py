from unittest import skip
from unittest.mock import MagicMock

from django.contrib.admin.sites import AdminSite
from django.test import TestCase

request = MagicMock()


@skip("It is unclear how to test this one")
class TestBaseAdmin(TestCase):
    pass


class TestOrgAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_org_str(self):
        from common.admin import OrgAdmin
        from common.models import Org

        ma = OrgAdmin(Org, self.site)
        self.assertEqual(str(ma), "common.OrgAdmin")

    def test_list_fields(self):
        from common.admin import OrgAdmin
        from common.models import Org

        ma = OrgAdmin(Org, self.site)
        self.assertEqual(
            list(ma.get_list_display(request)),
            [
                "name",
                "manager",
                "website",
                "is_research",
                "is_publisher",
                "is_mfg_cells",
                "is_mfg_equip",
            ],
        )
        self.assertEqual(
            list(ma.get_list_filter(request)),
            ["is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"],
        )


class TestReferenceAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_reference_str(self):
        from common.admin import ReferenceAdmin
        from common.models import Reference

        ma = ReferenceAdmin(Reference, self.site)
        self.assertEqual(str(ma), "common.ReferenceAdmin")

    def test_list_fields(self):
        from common.admin import ReferenceAdmin
        from common.models import Reference

        ma = ReferenceAdmin(Reference, self.site)
        self.assertEqual(
            list(ma.get_list_display(request)), ["title", "DOI", "has_pdf"]
        )


class TestPersonAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_person_str(self):
        from common.admin import PersonAdmin
        from common.models import Person

        ma = PersonAdmin(Person, self.site)
        self.assertEqual(str(ma), "common.PersonAdmin")

    def test_list_fields(self):
        from common.admin import PersonAdmin
        from common.models import Person

        ma = PersonAdmin(Person, self.site)
        self.assertEqual(
            list(ma.get_list_display(request)), ["longName", "shortName", "user", "org"]
        )
        self.assertEqual(list(ma.get_list_filter(request)), ["org"])

    def test_readonly_fields(self):
        from common.admin import PersonAdmin
        from common.models import Person

        ma = PersonAdmin(Person, self.site)
        self.assertEqual(list(ma.get_readonly_fields(request)), ["user_firstname"])
