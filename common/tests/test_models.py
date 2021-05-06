import time
from unittest import TestCase, skip

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from fixtures import AbstractModelMixinTestCase, db_user


class TestHasName(AbstractModelMixinTestCase):
    from ..models import HasName

    mixin = HasName
    model: mixin

    def setUp(self):
        self.model.objects.create(name="Michael Faraday")

    def test_has_name_creation(self):
        michael = self.model.objects.get()
        self.assertEqual(michael.__str__(), michael.name)


class TestHasStatus(AbstractModelMixinTestCase):
    from ..models import HasStatus

    mixin = HasStatus
    model: mixin

    def setUp(self):
        for (s, _) in self.mixin.OBJ_STATUS:
            self.model.objects.create(status=s)

    def test_has_status_creation(self):
        status = [s[0] for s in self.mixin.OBJ_STATUS]
        for s in self.model.objects.filter():
            assert s.status in status


class TestHasOwner(AbstractModelMixinTestCase):
    from ..models import HasOwner

    mixin = HasOwner
    model: mixin

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.model.objects.create(user_owner=user)

    def test_has_owner_creation(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.user_owner, User.objects.get())


class TestHasCreatedModifiedDates(AbstractModelMixinTestCase):
    from ..models import HasCreatedModifiedDates

    mixin = HasCreatedModifiedDates
    model: mixin

    def setUp(self):
        self.model.objects.create()

    def test_has_dates_creation(self):
        obj = self.model.objects.get()
        self.assertAlmostEqual(
            obj.created_on.timestamp(), obj.modified_on.timestamp(), places=2
        )
        time.sleep(0.1)
        obj.save()
        self.assertNotAlmostEqual(
            obj.created_on.timestamp(), obj.modified_on.timestamp(), places=2
        )


class TestHasAttributes(AbstractModelMixinTestCase):
    from ..models import HasAttributes

    mixin = HasAttributes
    model: mixin

    def setUp(self):
        self.model.objects.create(attributes={"ranges": 2, "colour": "blue"})

    def test_has_attributes_creation(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.attributes, {"ranges": 2, "colour": "blue"})


class TestHasNotes(AbstractModelMixinTestCase):
    from ..models import HasNotes

    mixin = HasNotes
    model: mixin

    def setUp(self):
        self.model.objects.create(notes="May the force be with you...")

    def test_has_notes_creation(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.notes, "May the force be with you...")


class TestHasSlug(AbstractModelMixinTestCase):
    from ..models import HasSlug

    mixin = HasSlug
    model: mixin

    def setUp(self):
        self.model.objects.create()

    def test_has_slug_creation(self):
        from django.utils.text import slugify

        obj = self.model.objects.get()

        # The slug should be a valid slug, so slugify should do nothing
        self.assertEqual(obj.slug, slugify(obj.slug))

    def test_save(self):
        from django.utils.text import slugify

        obj = self.model.objects.get()
        obj.save()
        self.assertEqual(obj.slug, slugify(str(obj)))


@skip("It is unclear how to test this model, at the moment.")
class TestHasMPTT(TestCase):
    def test_metadata(self):
        self.fail()


class TestBaseModelNoName(AbstractModelMixinTestCase):
    from ..models import BaseModelNoName

    mixin = BaseModelNoName
    model: mixin

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.expected = dict(
            user_owner=user,
            status="draft",
            attributes={"ranges": 2, "colour": "blue"},
            notes="May the force be with you...",
        )
        self.model.objects.create(**self.expected)

    def test_has_base_model_no_name_creation(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.user_owner, self.expected["user_owner"])
        self.assertEqual(obj.status, self.expected["status"])
        self.assertEqual(obj.attributes, self.expected["attributes"])
        self.assertEqual(obj.notes, self.expected["notes"])
        self.assertTrue(hasattr(obj, "slug"))
        self.assertTrue(hasattr(obj, "created_on"))
        self.assertTrue(hasattr(obj, "modified_on"))


class TestBaseModel(AbstractModelMixinTestCase):
    from ..models import BaseModel

    mixin = BaseModel
    model: mixin

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.expected = dict(
            user_owner=user,
            status="draft",
            attributes={"ranges": 2, "colour": "blue"},
            notes="May the force be with you...",
        )
        self.model.objects.create(**self.expected)
        self.model.objects.create(name="My model", **self.expected)

    def test_has_base_model_creation(self):
        self.assertEqual(self.model.objects.get(pk=1).name, None)
        self.assertEqual(self.model.objects.get(pk=2).name, "My model")


class TestBaseModelMandatoryName(AbstractModelMixinTestCase):
    from ..models import BaseModelMandatoryName

    mixin = BaseModelMandatoryName
    model: mixin

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.expected = dict(
            user_owner=user,
            status="draft",
            attributes={"ranges": 2, "colour": "blue"},
            notes="May the force be with you...",
        )
        self.model.objects.create(**self.expected)
        self.model.objects.create(name="My model", **self.expected)

    def test_has_base_model_mandatory_name_creation(self):
        self.assertEqual(self.model.objects.get(pk=1).name, "")
        self.assertEqual(self.model.objects.get(pk=2).name, "My model")


class TestOrg(TestCase):
    from ..models import Org

    model = Org

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.expected = dict(
            name="Dharma",
            manager=user,
            is_research=True,
            is_mfg_equip=True,
            attributes={"ranges": 2, "colour": "blue"},
            notes="Research in meteorology, zoology and electromagnetism",
            website="www.dharma.com",
        )
        self.model.objects.create(**self.expected)

    def test_org_creation(self):
        obj = self.model.objects.get()
        for k, v in self.expected.items():
            self.assertEqual(getattr(obj, k), v)
        self.assertFalse(obj.is_publisher)
        self.assertFalse(obj.is_mfg_cells)


class TestPerson(TestCase):
    from ..models import Person

    model = Person

    def setUp(self):
        User.objects.get_or_create(**db_user)
        user = User.objects.get()
        self.expected = dict(
            longName="Michael Faraday",
            shortName="MichaelF",
            user=user,
        )
        self.model.objects.get_or_create(**self.expected)

    def test_person_creation(self):
        obj = self.model.objects.get()
        for k, v in self.expected.items():
            self.assertEqual(getattr(obj, k), v)
        self.assertIsNone(obj.org)

    def test_user_firstname(self):
        obj = self.model.objects.get()
        usr = User.objects.get()
        self.assertEqual(obj.user_firstname(), usr.first_name)

    def test_user_lastname(self):
        obj = self.model.objects.get()
        usr = User.objects.get()
        self.assertEqual(obj.user_lastname(), usr.last_name)


class TestDOIField(TestCase):
    from ..models import DOIField

    model = DOIField

    def test_validate(self):
        doi = self.model()
        self.assertRaises(ValidationError, doi.validate, "www.dharma.com", None)
        doi.validate("https://doi.org/10.1007/s10825-018-1171-3", None)

    @skip("Method not implemented, yet")
    def test_get_url(self):
        self.fail()

    @skip("Method not implemented, yet")
    def test_get_name(self):
        self.fail()


class TestYearField(TestCase):
    from ..models import YearField

    model = YearField

    def test_validate(self):
        year = self.model()
        self.assertRaises(ValidationError, year.validate, 1492, None)
        self.assertRaises(ValidationError, year.validate, 2250, None)
        year.validate(1982, None)


class TestContentTypeRestrictedFileField(TestCase):
    from ..models import ContentTypeRestrictedFileField

    model = ContentTypeRestrictedFileField

    def test_type_restricted_file_field_creation(self):
        content = ["text/x-python", "application/pdf"]
        size = 2621440
        file_field = self.model(content_types=content, max_upload_size=size)
        self.assertEqual(content, file_field.content_types)
        self.assertEqual(size, file_field.max_upload_size)

    def test_clean(self):
        data = SimpleUploadedFile(
            "best_file_eva.txt", b"these are the contents of the txt file"
        )
        file_field = self.model(content_types=[], max_upload_size=1)
        self.assertRaises(ValidationError, file_field.clean, data, file_field)

        file_field = self.model(content_types=["text/plain"], max_upload_size=1)
        self.assertRaises(ValidationError, file_field.clean, data, file_field)

        file_field = self.model(content_types=["text/plain"])
        file_field.clean(data, file_field)


class TestPaper(TestCase):
    from ..models import Paper

    model = Paper

    def setUp(self):
        self.expected = dict(
            authors="Michael Faraday",
            title="Chemical Manipulation, Being Instructions to Students in Chemistry",
            year=1827,
        )
        self.model.objects.get_or_create(**self.expected)

    def test_paper_creation(self):
        obj = self.model.objects.get()
        for k, v in self.expected.items():
            self.assertEqual(getattr(obj, k), v)

    def test_has_pdf(self):
        self.assertFalse(self.model.objects.get().has_pdf())


class TestHashedFile(AbstractModelMixinTestCase):
    from ..models import HashedFile

    mixin = HashedFile
    model: mixin

    def setUp(self):
        self.data = SimpleUploadedFile(
            "best_file_eva.txt", b"these are the contents of the txt file"
        )
        self.model.objects.create(file=self.data)

    def test_hashed_file_creation(self):
        obj = self.model.objects.get()
        self.assertIsNotNone(obj.file.name)
        self.assertEqual(obj.hash, "")

    def test_clean(self):
        from ..utils import hash_file

        obj = self.model.objects.get()
        self.assertEqual(obj.hash, "")
        obj.clean()
        self.assertEqual(obj.hash, hash_file(obj.file))

    def test_exists(self):
        obj = self.model.objects.get()
        self.assertTrue(obj.exists())

    def test_size_bytes(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.size_bytes(), self.data.size)

    def test_size(self):
        obj = self.model.objects.get()
        self.assertEqual(obj.size(), "%dB" % self.data.size)
