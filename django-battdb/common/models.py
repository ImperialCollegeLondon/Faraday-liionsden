from django.db import models
from django.db.models import JSONField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import idutils # for DOI validation: https://idutils.readthedocs.io/en/latest/
import datetime

#TODOnt: Add localised strings (l10n) using django_gettext for all string literals in this file

class HasName(models.Model):
    """
    Abstract base class for any model having a unique name
    """
    name = models.CharField(max_length=128, unique=True, blank=True, null=True, help_text="Unique name for this object")
    def __str__(self):
       return str(self.name)
    class Meta:
      abstract=True  # this tells Django not to create a table for this model - it's an abstract base class


OBJ_STATUS_DRAFT = 10  # viewable and editable only by owner
OBJ_STATUS_SUBMITTED = 20 # viewable by others, modifiable by owner
OBJ_STATUS_ACCEPTED = 30 # cannot be modified by owner, except to return status to draft
OBJ_STATUS_PUBLISHED = 40 # cannot be modified except by admin
OBJ_STATUS_DELETED = 50 # hidden to all except admin

class HasStatus(models.Model):
   """
   Abstract base for any model having a common object status field
   """
   created_on = models.DateField(auto_now_add=True)
   OBJ_STATUS = [
            (OBJ_STATUS_DRAFT, 'Draft'),
            (OBJ_STATUS_SUBMITTED, 'Submitted'),
            (OBJ_STATUS_ACCEPTED, 'Accepted'),
            (OBJ_STATUS_PUBLISHED, 'Published'),
            (OBJ_STATUS_DELETED, 'Deleted'),
       ]
   status = models.PositiveSmallIntegerField(default=OBJ_STATUS_DRAFT, choices=OBJ_STATUS)
   class Meta:
      abstract=True    


class HasOwner(models.Model):
   """
   Abstract base for any model whose objects belong to user and group objects
   """
   user_owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
   #org_owner = models.ForeignKey('Org', on_delete=models.SET_NULL, null=True, blank=True)
   class Meta:
      abstract=True


class HasAttributes(models.Model):
   """
   Abstract base having JSON attributes
   """
   attributes = JSONField(default=dict, blank=True, help_text="Optional machine-readable JSON metadata")
   class Meta:
      abstract=True
      
class HasNotes(models.Model):
   """
   Abstract base having textual notes
   """
   notes = models.TextField(null=True, blank=True, help_text="Optional human-readable notes")
   class Meta:
      abstract=True
      

class BaseModel(HasName, HasStatus, HasOwner, HasAttributes, HasNotes):
   """
   Abstract base Inheriting all the common bases as mixins:
   HasName, HasStatus, HasOwner, HasAttributes, HasNotes
   """
   class Meta:
      abstract=True

class Person(BaseModel):
    """
    describes a person in or outside the system e.g. an author on a paper
    """
    pass
 
 # TODO: ModelForm Org.head = filter on Person WHERE Person.org = this
class Org(BaseModel):
   """
   Organisation e.g. publisher, manufacturer or institution 
   """
   is_research = models.BooleanField(default=False)
   is_publisher = models.BooleanField(default=False)
   is_mfg_cells = models.BooleanField(default=False)
   is_mfg_equip = models.BooleanField(default=False)
   website = models.URLField(null=True, blank=True)


#class UserRole




class DeviceType(BaseModel):
    """
    A type of thing, or specification. Provides default metadata for objects referencing this type
    """
    pass


class Batch(BaseModel):
    """  
    Describes a batch of things produced to the same type specification 
    """
    manufacturer = models.ForeignKey(Org, null=True, blank=True, on_delete=models.SET_NULL)
    device_type = models.ForeignKey(DeviceType, null=True, blank=True, on_delete=models.SET_NULL)
    # validate: my manufacturer is an org with mfg_devices=True
    
# a physical thing
class Device(BaseModel):
    pass



class DOIField(models.CharField):
   description = "Digital Object Identifier (DOI)"
   def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 128;
        super(DOIField, self).__init__(*args, **kwargs)
   def validate(self, value, obj):
        super().validate(value, obj)
        if not idutils.is_doi(value):
           raise ValidationError(
              _('%(value)s is not a valid DOI'),
               params={'value': value},
           )
   def get_url(self):
     pass      #TODO: implement a method to resolve the URL of a DOI
   def get_name(self):
     pass      #TODO: implement a method to fetch the document name

class YearField(models.IntegerField):
   def __init__(self, *args, **kwargs):
      super(YearField, self).__init__(*args, **kwargs)
   def validate(self, value, obj):
      super().validate(value, obj)
      if (value > datetime.date.today().year):
         raise ValidationError("Invalid year: Cannot be in the future")
      if (value < 1791):
         raise ValidationError("Invalid year: Cannot pre-date the field of Electrochemistry!")

class Paper(BaseModel):
   DOI = DOIField(unique=True, blank=True, null=True, help_text="Paper DOI. In future, this could populate the other fields automatically.")
   tag = models.SlugField(max_length=100, unique=True, help_text="Tag or 'slug' used to uniquely identify this paper. This will be auto-generated in future versions.")
   year = YearField(default=datetime.date.today().year)
   title = models.CharField(max_length=300)
   #authors = models.ManyToManyField(Person) # no - see above
   org_owners = models.ManyToManyField(Org, related_name='papers', help_text="Contributing Organisations.")
   publisher = models.ForeignKey(Org, on_delete=models.SET_NULL, null=True, blank=True)
   authors = models.CharField(max_length=500)
   url = models.URLField(null=True, blank=True) # blank=true means not a required field in forms. null=True means don't set NOT NULL in SQL
   def __unicode__(self):
     return self.tag
   # TODO: Validator which autogenerates 'tag' field from a 'slugification' of principal author surname + year + title
#   def save(self, *args, **kwargs):
#     self.tag = slugify(self.authors + self.year + self.title)
#     super().save(*args,**kwargs)
  # TODO: ModelForm paper.publisher = filter on Org where Org.type = PUBLISHER

