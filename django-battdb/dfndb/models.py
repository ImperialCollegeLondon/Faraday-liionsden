from django.db import models
import idutils # for DOI validation: https://idutils.readthedocs.io/en/latest/
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

# any model can inherit this one to add these columns
class BaseModel(models.Model):
   name =  models.CharField(max_length=100, unique=True)
   owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
   created_on = models.DateField(auto_now_add=True)
   accepted = models.BooleanField(default=False)
   class Meta:
      abstract=True  # this tells Django not to create a table for this model - it's an abstract base class
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
      if (value < 1791 or value > datetime.date.today().year):
         raise ValidationError("Invalid year")

# I think this would be unnecessary for now - we don't need a full contact info DB!
#class Person(models.Model):
#   first_name = models.CharField()
#   last_name  = models.CharField()
#   institution = models.ForteignKey( ... )

class Paper(models.Model):
  DOI = DOIField(unique=True)  # use our custom DOI field
  paper_tag = models.SlugField(max_length=100, unique=True)  # SlugField is a CharField with validation, like my DOIField
  year = YearField(default=datetime.date.today().year)
  title = models.CharField(max_length=300)
  #authors = models.ManyToManyField(Person) # no - see above
  authors = models.CharField(max_length=500)
  url = models.URLField(null=True, blank=True) # blank=true means not a required field in forms. null=True means don't set NOT NULL in SQL
  created_on = models.DateField(auto_now_add=True)
  accepted = models.BooleanField(default=False)  
  def __str__(self):
    return self.paper_tag

# I don't like Material having a column for each chemical compound - that seems nasty.
# Instead I will use one of Django's special ManyToManyFields with a "Through" relationship.
# This specifies the table a mapping table with an extra column for the composition number
# actually, don't even need a "through" for this.

class Compound(models.Model):
  formula = models.CharField(max_length=20, unique=True) #  "Li"
  name = models.CharField(max_length=100, unique=True) #  "Lithium"
  def __str__(self):
    return "%s (%s)"%(self.name,self.formula)

class CompositionPart(models.Model):
  compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
  amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
  def __str__(self):
    return "%s%d"%(self.compound.formula,self.amount)

class Material(BaseModel):
  composition = models.ManyToManyField(CompositionPart)
  MATERIAL_TYPE_CHOICES = [
     (1, 'Anode'),
     (2, 'Cathode'),
     (3, 'Electrolyte'),
     (4, 'Separator'),
  ]
  type = models.IntegerField(choices=MATERIAL_TYPE_CHOICES)
  polymer = models.IntegerField(default=0,validators=[MinValueValidator(0)])
  def __str__(self):
    return self.name

class Method(BaseModel):
  # what does the 'method class' do??
  # in any case it's a bad idea to have something called class, it gets confusing
  # Using 'choices' will cause Django to use multiple choice validators & drop down menus
  # see: https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices
  METHOD_TYPE_CHOICES = [
    (1, 'Experimental'),
    (2, 'Modelling'),
  ]
  type = models.IntegerField(choices=METHOD_TYPE_CHOICES)
  description =  models.TextField(blank=True)

class QuantityUnit(models.Model):
  name = name = models.CharField(max_length=100, unique=True) # Voltage
  symbol = models.CharField(max_length=40, unique=True)  # V
  symbolName = models.CharField(max_length=40, blank=True) # Volts
  def __str__(self):
    return "%s/%s"%(self.name,self.symbol)

class Parameter(BaseModel):
  symbol = models.CharField(max_length=40, unique=True)
  PARAM_TYPE_CHOICES = [
    (1, 'ParamType1'),
    (2, 'ParamType2'),
  ]
  type = models.IntegerField(choices=PARAM_TYPE_CHOICES)
  unit = models.ForeignKey(QuantityUnit, blank=True, null=True, on_delete=models.SET_NULL)
  notes = models.TextField(blank=True)
  def __str__(self):
    return "%s: %s"%(self.name,self.symbol)

class Data(BaseModel):
  paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
  parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
  material = models.ForeignKey(Material, on_delete=models.CASCADE)
  DATA_TYPE_CHOICES = [
    (1, 'DataType1'),  
    (2, 'DataType2'),
  ]
  type = models.IntegerField(choices=DATA_TYPE_CHOICES)
  data = models.TextField()
  # other fields to be added... I'm not sure what the numrange fields are for?
  class Meta:
     verbose_name_plural="Data"  # don't pluralise to "Datas"
