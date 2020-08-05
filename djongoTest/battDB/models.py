from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
#from jsonfield_schema import JSONSchema


class HasAttributes(models.Model):
    name = models.CharField(max_length=32, unique=True)
    attributes = JSONField(default=dict, blank=True)
    def __str__(self):
       return self.name
    class Meta:
        abstract = True


class SignalType(HasAttributes):
    pass

class TestProtocol(HasAttributes):
    description = models.TextField()
    parameters=JSONField(default=dict, blank=True)

class Manufacturer(HasAttributes):
    pass


def equipmentType_schema():
    return {
       "channels":None,
    }

class EquipmentType(HasAttributes):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
EquipmentType._meta.get_field('attributes').default = equipmentType_schema


class Equipment(HasAttributes):
    type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True, blank=True)
    serialNo = models.CharField(max_length=64)
    class Meta:
       verbose_name_plural="Equipment"

def cellSeparator_schema():
    return {
       "material":None,
       "porosity_pct" : None
    }

class CellSeparator(HasAttributes):
    pass
CellSeparator._meta.get_field('attributes').default = cellSeparator_schema


class CellBatch(HasAttributes):
    manufactured_on = models.DateField(null=True, blank=True)
    manufacturer    = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    cells_schema = JSONField(default=dict, blank=True)
    class Meta:
       verbose_name_plural="CellBatches"

class CellConfig(HasAttributes):
    pass

class Cell(HasAttributes):
    batch = models.ForeignKey(CellBatch, on_delete=models.SET_NULL, null=True, blank=True)
    separator = models.ForeignKey(CellSeparator, on_delete=models.SET_NULL, null=True, blank=True)

class ExperimentalApparatus(HasAttributes):
    testEquipment = models.ManyToManyField(Equipment)
    cellConfig = models.ForeignKey(CellConfig, on_delete=models.SET_NULL,  null=True, blank=True)
    protocol = models.ForeignKey(TestProtocol, on_delete=models.SET_NULL,  null=True, blank=True)
    photo = models.ImageField(upload_to='apparatus_photos', null=True, blank=True)
    class Meta:
       verbose_name_plural="ExperimentalApparatus"

def experimentParameters_schema():
    return {
        "StartVoltage":None,
        "EndVoltage":None,
    }

def experimentAnalysis_schema():
    return {
        "MeasuredCapacity":None,
        "MeasuredResistance":None,
    }

class Experiment(models.Model):
    name = models.SlugField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    apparatus = models.ForeignKey(TestProtocol, on_delete=models.SET_NULL,  null=True, blank=True)
    cells = models.ManyToManyField(Cell)
    raw_data_file = models.FileField(upload_to='raw_data_files',null=True)
    processed_data_file = models.FileField(upload_to='processed_data_files',null=True, blank=True)
    parameters = JSONField(default=experimentParameters_schema, blank=True)
    analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
        return str(self.owner) + "/" + str(self.name) + "/" + str(self.date)
    @property
    def slug(self):
        return str(self)
    def get_absolute_url(self):
        #return reverse('Experiment', kwargs={'slug': self.slug})
        return reverse('Experiment', kwargs={'pk': self.pk})
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'name', 'date'], name='unique_slugname')
        ]

