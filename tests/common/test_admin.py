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


class TestPaperAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_paper_str(self):
        from common.admin import PaperAdmin
        from common.models import Paper

        ma = PaperAdmin(Paper, self.site)
        self.assertEqual(str(ma), "common.PaperAdmin")

    def test_list_fields(self):
        from common.admin import PaperAdmin
        from common.models import Paper

        ma = PaperAdmin(Paper, self.site)
        self.assertEqual(
            list(ma.get_list_display(request)), ["title", "DOI", "year", "has_pdf"]
        )
        self.assertEqual(
            list(ma.get_list_filter(request)), ["year", "publisher", "authors"]
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
