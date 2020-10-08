from django.db import models
from django.contrib.auth import get_user_model
import idutils # for DOI validation: https://idutils.readthedocs.io/en/latest/
import datetime

# base class for any model having a unique name
class NamedModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
       return self.name
    class Meta:
      abstract=True  # this tells Django not to create a table for this model - it's an abstract base class

class Org(NamedModel):
   parent = models.ForeignKey('Org', null=True, blank=True, on_delete=models.SET_NULL, related_name='child_orgs')
   head = models.ForeignKey('Person', null=True, blank=True, on_delete=models.SET_NULL, related_name='head_of')


# this duplicates some stuff in the User model, maybe it's not needed at all
class Person(models.Model):
   authUser = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
   firstName = models.CharField(max_length=40)
   lastName = models.CharField(max_length=40)
   email=models.EmailField(unique=True,blank=True,null=True)
   org = models.ForeignKey(Org, on_delete=models.SET_NULL, null=True, blank=True)
   def __str__(self):
       return self.firstName + " " + self.lastName

#class UserRole

# any model can inherit this one to add these columns
class BaseModel(models.Model):
   name =  models.CharField(max_length=100, unique=True)
   user_owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
   created_on = models.DateField(auto_now_add=True)
   accepted = models.BooleanField(default=False)
   class Meta:
      abstract=True
   def __str__(self):
      return self.name


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
     pass      # implement a method to resolve the URL of a DOI
   def get_name(self):
     pass      # implement a method to fetch the document name

class YearField(models.IntegerField):
   def __init__(self, *args, **kwargs):
      super(YearField, self).__init__(*args, **kwargs)
   def validate(self, value, obj):
      super().validate(value, obj)
      if (value > datetime.date.today().year):
         raise ValidationError("Invalid year: Cannot be in the future")
      if (value < 1791):
         raise ValidationError("Invalid year: Cannot predate the field of Electrochemistry!")

class Paper(models.Model):
   DOI = DOIField(unique=True, blank=True, null=True)  # use our custom DOI field
   tag = models.SlugField(max_length=100, unique=True)  # SlugField is a CharField with validation, like my DOIField
   year = YearField(default=datetime.date.today().year)
   title = models.CharField(max_length=300)
   #authors = models.ManyToManyField(Person) # no - see above
   org_owners = models.ManyToManyField(Org, related_name='papers')
   authors = models.CharField(max_length=500)
   url = models.URLField(null=True, blank=True) # blank=true means not a required field in forms. null=True means don't set NOT NULL in SQL
   created_on = models.DateField(auto_now_add=True)
   accepted = models.BooleanField(default=False)
   def __str__(self):
     return self.tag
   # TODO: Validator which autogenerates 'tag' field from a 'slugification' of principal author surname + year + title
   #def validate(self, value, obj):
   #  if not self.tag.validate(value):
   #    obj.tag = make_paper_tag(obj)
   #  return super().validate(value, obj)

