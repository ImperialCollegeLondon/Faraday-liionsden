import datetime
import os

import idutils  # for DOI validation: https://idutils.readthedocs.io/en/latest/
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import JSONField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from .utils import hash_file
from .validators import validate_data_file

# TODO: Add localised strings (l10n) using django_gettext for all string literals in
#  this file


class HasName(models.Model):
    """Abstract base class for any model having a name."""

    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    # Tells Django not to create a table for this model: it's an abstract base class
    class Meta:
        abstract = True


class HasStatus(models.Model):
    """Abstract base for any model having a common object status field."""

    OBJ_STATUS = [
        ("private", "Private"),  # creating user can view and modify
        ("public", "Public"),  # cannot be modified except by maintainers/admin
        ("deleted", "Deleted"),  # hidden to all except maintainers/admin
    ]
    status = models.CharField(max_length=16, default="private", choices=OBJ_STATUS)

    class Meta:
        abstract = True


class HasOwner(models.Model):
    """Abstract base for any model whose objects belong to user and group objects."""

    user_owner = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        abstract = True


class HasCreatedModifiedDates(models.Model):
    """Abstract base for any model with creation and modified dates."""

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HasAttributes(models.Model):
    """Abstract base having JSON attributes.

    TODO: What is the use case for this field?
    """

    attributes = JSONField(
        default=dict, blank=True, help_text="Optional machine-readable JSON metadata"
    )

    class Meta:
        abstract = True


class HasNotes(models.Model):
    """Abstract base having textual notes."""

    notes = models.TextField(
        null=True, blank=True, help_text="Optional human-readable notes"
    )

    class Meta:
        abstract = True


class HasSlug(models.Model):
    """Adds a unique SlugField.

    FIXME: Make unique=True later
    """

    slug = models.SlugField(
        max_length=500,
        unique=False,
        default="autogenerated",
        editable=False,
        help_text="Auto-generated unique name, can be used in URLs",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class HasMPTT(MPTTModel):
    """Adds object hierarchical tree structure using django-MPTT library."""

    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Parent node in object tree hierarchy",
    )

    inherit_metadata = models.BooleanField(
        default=True,
        verbose_name="Inherit metadata attributes from parent",
        help_text="Set to True if this object does not describe a real life thing, but "
        "a specification, type or grouping. "
        "In this case, the metadata will be inherited.",
    )

    class Meta:
        abstract = True

    def metadata(self):
        """Provide the metadata for this object."""
        meta = dict()
        if self.inherit_metadata:
            ancestors = self.get_ancestors(ascending=True, include_self=False)
            for ancestor in ancestors:
                if ancestor.inherit_metadata and hasattr(self, "attributes"):
                    meta.update(ancestor.attributes)
                else:
                    break

        if hasattr(self, "attributes"):
            meta.update(self.attributes)

        return meta


class BaseModelNoName(
    HasSlug, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates
):
    """Abstract base for not named objects inheriting all the common bases as mixins.

    The inherited bases are HasSlug, HasStatus, HasOwner, HasAttributes, HasNotes,
    HasCreatedModifiedDates.
    """

    class Meta:
        abstract = True


class BaseModel(BaseModelNoName, HasName):
    """Abstract base for named objects inheriting all the common bases as mixins.

    The inherited bases are HasName, HasSlug, HasStatus, HasOwner, HasAttributes,
    HasNotes, HasCreatedModifiedDates.
    """

    class Meta:
        abstract = True


class BaseModelMandatoryName(BaseModel):
    """Changed BaseModel.name to blank=False."""

    name = models.CharField(
        max_length=128, blank=False, default="", null=False, unique=True
    )

    class Meta:
        abstract = True


# TODO: ModelForm Org.head = filter on Person WHERE Person.org = this
class Org(HasNotes, HasSlug, HasAttributes, HasCreatedModifiedDates):  # type: ignore
    """Model for organizations.

    Being these publisher, manufacturer or institution, for example.
    """

    name = models.CharField(max_length=128, unique=True, help_text="Organisation name")
    manager = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )
    is_research = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_mfg_cells = models.BooleanField(default=False)
    is_mfg_equip = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    """Describes a person who can be outside the system e.g. an author on a paper."""

    longName = models.CharField(
        max_length=128,
        unique=True,
        help_text="Person's full name e.g. David Wallace Jones",
    )
    shortName = models.CharField(
        max_length=128,
        unique=True,
        help_text="Person's shortened name e.g. 'D.W. Jones'",
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="person",
        help_text="User account in the system, if any.",
    )
    org = models.ForeignKey(
        Org,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Organisation that this person belongs to, if any.",
    )

    def __str__(self):
        return str(self.shortName)

    def user_firstname(self):
        return self.user.first_name or "borked"

    def user_lastname(self):
        return self.user.last_name or "borked"


class DOIField(models.URLField):
    description = "Digital Object Identifier (DOI)"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 128
        super().__init__(*args, **kwargs)

    def validate(self, value, obj):
        if not idutils.is_doi(value):
            raise ValidationError(
                _("%(value)s is not a valid DOI"),
                params={"value": value},
            )
        return super().validate(value, obj)


class YearField(models.IntegerField):
    def validate(self, value, obj):
        """Validates the value of the year."""
        super().validate(value, obj)
        if value > datetime.date.today().year:
            raise ValidationError("Invalid year: Cannot be in the future")
        if value < 1791:
            raise ValidationError(
                "Invalid year: Cannot pre-date the field of Electrochemistry!"
            )


class Reference(  # type: ignore
    HasSlug, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates
):
    """A source of data, typically an academic paper, but can be a dataset or repo."""

    DOI = DOIField(
        blank=True,
        null=True,
        unique=True,
        help_text="DOI for the reference.",
    )
    title = models.CharField(max_length=300, default="")
    url = models.URLField(null=True, blank=True)
    PDF = models.FileField(null=True, blank=True, help_text="Optional PDF copy")

    def has_pdf(self):
        return True if self.PDF else False

    def __str__(self):
        return slugify(str(self.DOI) + "-" + str(self.title))


class HashedFile(models.Model):
    """
    Uploaded files with a unique hash number.
    """

    file = models.FileField(
        upload_to="uploaded_files", null=False, validators=(validate_data_file,)
    )
    hash = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        editable=False,
        help_text="SHA-1 Hash of uploaded file. You cannot upload the same file twice.",
    )

    class Meta:
        abstract = True

    def clean(self):
        print(self.file.name)
        if not self.file:
            raise ValidationError("No file was uploaded.")
        self.hash = hash_file(self.file)
        return super().clean()

    def __str__(self):
        return os.path.basename(self.file.name)

    def exists(self):
        return self.file.storage.exists(self.file.name)

    def size_bytes(self):
        return self.file.storage.size(self.file.name)

    def size(self):
        if not self.exists():
            return "N/A"
        if self.size_bytes() < 1024:
            return "%dB" % self.size_bytes()
        elif self.size_bytes() < 1024**2:
            return "%2.2fkB" % (self.size_bytes() / 1024.0)
        elif self.size_bytes() < 1024**3:
            return "%2.2fMB" % (self.size_bytes() / (1024.0**2))
        else:
            return "%2.2fGB" % (self.size_bytes() / (1024.0**3))
