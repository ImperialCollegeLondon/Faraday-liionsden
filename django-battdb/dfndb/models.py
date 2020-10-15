from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import common.models as cm


# Create your models here.

# I don't like Material having a column for each chemical compound - that seems nasty.
# Instead I will use one of Django's special ManyToManyFields with a "Through" relationship.
# This specifies the table a mapping table with an extra column for the composition number
# actually, don't even need a "through" for this.

class Compound(models.Model):
    formula = models.CharField(max_length=20, unique=True)  # "Li"
    name = models.CharField(max_length=100, unique=True)  # "Lithium"

    def __str__(self):
        return "%s (%s)" % (self.name, self.formula)


class CompositionPart(models.Model):
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return "%s%d" % (self.compound.formula, self.amount)


class Material(cm.BaseModel):
    composition = models.ManyToManyField(CompositionPart)
    MATERIAL_TYPE_CHOICES = [
        (1, 'Anode'),
        (2, 'Cathode'),
        (3, 'Electrolyte'),
        (4, 'Separator'),
    ]
    type = models.IntegerField(choices=MATERIAL_TYPE_CHOICES)
    polymer = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Method(cm.BaseModel):
    # what does the 'method class' do??
    # in any case it's a bad idea to have something called class, it gets confusing
    # Using 'choices' will cause Django to use multiple choice validators & drop down menus
    # see: https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices
    METHOD_TYPE_CHOICES = [
        (1, 'Experimental'),
        (2, 'Modelling'),
    ]
    type = models.IntegerField(choices=METHOD_TYPE_CHOICES)
    description = models.TextField(blank=True)


class QuantityUnit(models.Model):
    name = name = models.CharField(max_length=100, unique=True)  # Voltage
    symbol = models.CharField(max_length=40, unique=True)  # V
    symbolName = models.CharField(max_length=40, blank=True)  # Volts

    def __str__(self):
        return "%s/%s" % (self.name, self.symbol)


class Parameter(cm.BaseModel):
    symbol = models.CharField(max_length=40, unique=True)
    PARAM_TYPE_CHOICES = [
        (1, 'ParamType1'),
        (2, 'ParamType2'),
    ]
    type = models.IntegerField(choices=PARAM_TYPE_CHOICES)
    unit = models.ForeignKey(QuantityUnit, blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "%s: %s" % (self.name, self.symbol)


class Data(cm.BaseModel):
    paper = models.ForeignKey(cm.Paper, on_delete=models.CASCADE)
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
        verbose_name_plural = "Data"  # don't pluralise to "Datas"
