from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import JSONField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
import idutils  # for DOI validation: https://idutils.readthedocs.io/en/latest/
import datetime
from django.utils import timezone


# TODOnt: Add localised strings (l10n) using django_gettext for all string literals in this file

class HasName(models.Model):
    """
    Abstract base class for any model having a name
    """
    name = models.CharField(max_length=128, blank=True, null=True, help_text="Name for this object")

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True  # this tells Django not to create a table for this model - it's an abstract base class


class HasStatus(models.Model):
    """
   Abstract base for any model having a common object status field
   """
    OBJ_STATUS_DRAFT = 10  # viewable and editable only by owner
    OBJ_STATUS_SUBMITTED = 20  # viewable by others, modifiable by owner
    OBJ_STATUS_ACCEPTED = 30  # cannot be modified by owner, except to return status to draft
    OBJ_STATUS_PUBLISHED = 40  # cannot be modified except by admin
    OBJ_STATUS_DELETED = 50  # hidden to all except admin

    OBJ_STATUS = [
        (OBJ_STATUS_DRAFT, 'Draft'),
        (OBJ_STATUS_SUBMITTED, 'Submitted'),
        (OBJ_STATUS_ACCEPTED, 'Accepted'),
        (OBJ_STATUS_PUBLISHED, 'Published'),
        (OBJ_STATUS_DELETED, 'Deleted'),
    ]
    status = models.PositiveSmallIntegerField(default=OBJ_STATUS_DRAFT, choices=OBJ_STATUS)

    class Meta:
        abstract = True


class HasOwner(models.Model):
    """
   Abstract base for any model whose objects belong to user and group objects
   """
    user_owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    # org_owner = models.ForeignKey('Org', on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        abstract = True


class HasCreatedModifiedDates(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HasAttributes(models.Model):
    """
   Abstract base having JSON attributes
   """
    attributes = JSONField(default=dict, blank=True, help_text="Optional machine-readable JSON metadata")

    class Meta:
        abstract = True


class HasNotes(models.Model):
    """
   Abstract base having textual notes
   """
    notes = models.TextField(null=True, blank=True, help_text="Optional human-readable notes")

    class Meta:
        abstract = True


class HasSlug(models.Model):
    """
    Adds a unique SlugField
    """
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseModel(HasName, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates):
    """
   Abstract base Inheriting all the common bases as mixins:<br>
   HasName, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates
   """
    class Meta:
        abstract = True


class BaseModelWithSlug(BaseModel, HasSlug):
    pass


# TODO: ModelForm Org.head = filter on Person WHERE Person.org = this
class Org(models.Model):
    """
   Organisation, e.g. publisher, manufacturer or institution
   """
    name = models.CharField(max_length=128, unique=True, help_text="Organisation name")
    manager = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    is_research = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_mfg_cells = models.BooleanField(default=False)
    is_mfg_equip = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    """
    describes a person who can be outside the system e.g. an author on a paper
    """
    longName = models.CharField(max_length=128, unique=True,
                                help_text="Person's full name e.g. David Wallace Jones")
    shortName = models.CharField(max_length=128, unique=True,
                                 help_text="Person's shortened name e.g. 'D.W. Jones'")
    user = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="person",
                                help_text="User account in the system")
    org = models.ForeignKey(Org, on_delete=models.SET_NULL, null=True, blank=True,
                            help_text="Organisation that this person belongs to")

    def __str__(self):
        return str(self.shortName)

    def user_firstname(self):
        return self.user.first_name or "borked"

    def user_lastname(self):
        return self.user.last_name or "borked"
# class UserRole


class DOIField(models.URLField):
    description = "Digital Object Identifier (DOI)"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 128;
        super(DOIField, self).__init__(*args, **kwargs)

    def validate(self, value, obj):
        if not idutils.is_doi(value):
            raise ValidationError(
                _('%(value)s is not a valid DOI'),
                params={'value': value},
            )
        return super().validate(value, obj)

    def get_url(self):
        pass  # TODO: implement a method to resolve the URL of a DOI

    def get_name(self):
        pass  # TODO: implement a method to fetch the document name


class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super(YearField, self).__init__(*args, **kwargs)

    def validate(self, value, obj):
        super().validate(value, obj)
        if value > datetime.date.today().year:
            raise ValidationError("Invalid year: Cannot be in the future")
        if value < 1791:
            raise ValidationError("Invalid year: Cannot pre-date the field of Electrochemistry!")


# https://djangosnippets.org/snippets/2206/
class ContentTypeRestrictedFileField(models.FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
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
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        content_type = file.content_type

        if content_type in self.content_types:
            if file._size > self.max_upload_size:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
        else:
            raise forms.ValidationError(_('Filetype not supported.'))

        return data


class Paper(HasSlug, HasStatus, HasOwner, HasAttributes, HasNotes, HasCreatedModifiedDates):
    """
    An academic paper
   """
    DOI = DOIField(unique=True, blank=True, null=True,
                   help_text="Paper DOI. In future, this could populate the other fields automatically.")
    year = YearField(default=datetime.date.today().year)
    title = models.CharField(max_length=300)
    # authors = models.ManyToManyField(Person) # no - see above
    publisher = models.ForeignKey(Org, on_delete=models.SET_NULL, null=True, blank=True,
                                  limit_choices_to={'is_publisher': True})
    authors = models.ManyToManyField(Person,
                                     through='PaperAuthor',
                                     related_name='papers', help_text="Contributing Persons.")
    url = models.URLField(null=True, blank=True)
    PDF = models.FileField(null=True, blank=True, help_text="Optional PDF copy")

    def has_pdf(self):
        return self.PDF is not None

    def __str__(self):
        return slugify(str(self.title) + "-" + str(self.year))

# TODO: ModelForm paper.publisher = filter on Org where Org.type = PUBLISHER


class PaperAuthor(models.Model):
    """
    Author on paper
    """
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_principal = models.BooleanField(default=False)

    # def __str__(self):
    #     return "%s%d" % (self.compound.formula, self.amount)

    # class Meta:
    #     unique_together = ('data', 'parameter')