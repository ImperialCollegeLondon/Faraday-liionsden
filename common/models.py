import datetime
import os

import idutils  # for DOI validation: https://idutils.readthedocs.io/en/latest/
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import JSONField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
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
        ("draft", "Draft"),  # viewable and editable only by owner
        ("submitted", "Submitted"),  # viewable by others, modifiable by owner
        (
            "accepted",
            "Accepted",
        ),  # cannot be modified by owner, except to return status to draft
        ("published", "Published"),  # cannot be modified except by admin
        ("deleted", "Deleted"),  # hidden to all except admin
    ]
    status = models.CharField(max_length=16, default="draft", choices=OBJ_STATUS)

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
        return super(HasSlug, self).save(*args, **kwargs)

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

    name = models.CharField(max_length=128, blank=False, default="", null=False)

    class Meta:
        abstract = True


# TODO: ModelForm Org.head = filter on Person WHERE Person.org = this
class Org(HasNotes, HasSlug, HasAttributes, HasCreatedModifiedDates):
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
        super(DOIField, self).__init__(*args, **kwargs)

    def validate(self, value, obj):
        if not idutils.is_doi(value):
            raise ValidationError(
                _("%(value)s is not a valid DOI"),
                params={"value": value},
            )
        return super().validate(value, obj)

    def get_url(self):
        """Gets the URL of a DOI.

        TODO: implement method
        """
        pass

    def get_name(self):
        """Fetch the document name associated to the DOI.

        TODO: implement method
        """
        pass


class YearField(models.IntegerField):
    def validate(self, value, obj):
        """Validates the value of the year."""
        super(YearField, self).validate(value, obj)
        if value > datetime.date.today().year:
            raise ValidationError("Invalid year: Cannot be in the future")
        if value < 1791:
            raise ValidationError(
                "Invalid year: Cannot pre-date the field of Electrochemistry!"
            )


class ContentTypeRestrictedFileField(models.FileField):
    """A FileField with some extra information.

    https://djangosnippets.org/snippets/2206/

    The extra information than can be added is:
        - content_types - list containing allowed content_types. Eg:
            ['application/pdf', 'image/jpeg']
        - max_upload_size - an integer number indicating the maximum file size allowed
            in bytes. Eg.:
                2.5MB - 2621440
                5MB - 5242880
                10MB - 10485760
                20MB - 20971520
                50MB - 5242880
                100MB 104857600
                250MB - 214958080
                500MB - 429916160
    """

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", 429916160)

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """Validates the value and returns the data."""
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        if data.content_type in self.content_types:
            if data.size > self.max_upload_size:
                raise forms.ValidationError(
                    _("Please keep filesize under %s. Current filesize %s")
                    % (filesizeformat(self.max_upload_size), filesizeformat(data.size))
                )
        else:
            raise forms.ValidationError(_("Filetype not supported."))

        return data


class Paper(
    HasSlug, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates
):
    """An academic paper."""

    DOI = DOIField(
        unique=True,
        blank=True,
        null=True,
        help_text="DOI for the paper.",
    )
    year = YearField(default=datetime.date.today().year)
    title = models.CharField(max_length=300, default="")
    authors = models.CharField(max_length=300, default="")
    publisher = models.ForeignKey(
        Org,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"is_publisher": True},
    )

    url = models.URLField(null=True, blank=True)
    PDF = models.FileField(null=True, blank=True, help_text="Optional PDF copy")

    def has_pdf(self):
        return True if self.PDF else False

    def __str__(self):
        return slugify(str(self.title) + "-" + str(self.year))


class HashedFile(models.Model):
    """A list of user-uploaded files. <BR>

    FIXME: This is pretty insecure - File format & size is not yet enforced, so any kind
     of file can be uploaded, including Python scripts, very large binary files, etc.

    FIXME: Uploaded files should go somewhere else, no within the Django application
        code structure.
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
        self.hash = hash_file(self.file)
        return super(HashedFile, self).clean()

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
        elif self.size_bytes() < 1024 ** 2:
            return "%2.2fkB" % (self.size_bytes() / 1024.0)
        elif self.size_bytes() < 1024 ** 3:
            return "%2.2fMB" % (self.size_bytes() / (1024.0 ** 2))
        else:
            return "%2.2fGB" % (self.size_bytes() / (1024.0 ** 3))
