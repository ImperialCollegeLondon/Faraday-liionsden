import time
from unittest import TestCase, expectedFailure

from django.contrib.auth.models import User

from fixtures import AbstractModelMixinTestCase


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
        user = User.objects.create(username="MichaelF", password="C@cina27")
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


@expectedFailure
class TestHasMPTT(TestCase):
    def test_metadata(self):
        self.fail()


class TestBaseModelNoName(AbstractModelMixinTestCase):
    from ..models import BaseModelNoName

    mixin = BaseModelNoName
    model: mixin

    def setUp(self):
        user = User.objects.create(username="MichaelF", password="C@cina27")
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
        user = User.objects.create(username="MichaelF", password="C@cina27")
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
        user = User.objects.create(username="MichaelF", password="C@cina27")
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


@expectedFailure
class TestOrg(TestCase):
    pass


@expectedFailure
class TestPerson(TestCase):
    def test_user_firstname(self):
        self.fail()

    def test_user_lastname(self):
        self.fail()


@expectedFailure
class TestDOIField(TestCase):
    def test_validate(self):
        self.fail()

    def test_get_url(self):
        self.fail()

    def test_get_name(self):
        self.fail()


@expectedFailure
class TestYearField(TestCase):
    def test_validate(self):
        self.fail()


@expectedFailure
class TestContentTypeRestrictedFileField(TestCase):
    def test_clean(self):
        self.fail()


@expectedFailure
class TestPaper(TestCase):
    def test_has_pdf(self):
        self.fail()


@expectedFailure
class TestHashedFile(TestCase):
    def test_clean(self):
        self.fail()

    def test_exists(self):
        self.fail()

    def test_size_bytes(self):
        self.fail()

    def test_size(self):
        self.fail()
