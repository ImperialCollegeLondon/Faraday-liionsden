import os
import traceback
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
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
    photo = models.ImageField(upload_to='apparatus_photos', null=True, blank=True)
    class Meta:
       verbose_name_plural="Experimental apparatus"

def experimentParameters_schema():
    return {
    }

def experimentAnalysis_schema():
    return {
        "MeasuredCapacity":None,
        "MeasuredResistance":None,
    }

def resultMetadata_schema():
    return {
       "Columns":{},
       "num_rows": 0,
    }

def resultData_schema():
    return {
       "columns":[],
       "rows": []
    }

class Experiment(models.Model):
    name = models.SlugField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    status = models.CharField(max_length=16, choices=[("edit", "Edit") , ("published", "Published")], default="edit")
    apparatus = models.ForeignKey(ExperimentalApparatus, on_delete=models.SET_NULL,  null=True, blank=True)
    cells = models.ManyToManyField(Cell, related_name='experiments')
    protocol = models.ForeignKey(TestProtocol, on_delete=models.SET_NULL,  null=True, blank=True)
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

class ExperimentData(models.Model):
    raw_data_file = models.FileField(upload_to='raw_data_files',null=True)
    metadata = JSONField(default=resultMetadata_schema, blank=True)
    data = JSONField(default=resultData_schema, blank=True, editable=False)
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True, blank=True, related_name='data')
    import_columns = models.ManyToManyField(SignalType, blank=True)
    parameters = JSONField(default=experimentParameters_schema, blank=True)
    analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
       return os.path.basename(self.raw_data_file.name)
    class Meta:
       verbose_name_plural="Experiment Data Files"

def data_pre_save(sender, instance, *args, **kwargs):
    if not instance:
       return
    if hasattr(instance, '_dirty'):
       return

    try:
       print("result_post_save: Sender: %s, Instance: %s, args: %s, kwargs: %s, base_loc: %s, dilename: %s" % (sender, instance, args, kwargs, instance.raw_data_file.storage.base_location, instance.raw_data_file.name))
       filepath = "/".join([instance.raw_data_file.storage.base_location, instance.raw_data_file.name])
       parser = BiologicCSVnTSVParser(filepath)
       (instance.metadata, columns) = (parser.get_metadata())
       instance.metadata['Columns'] = columns
       instance.data['rows'] = [None] * instance.metadata['num_rows']
       gen = parser.get_data_generator_for_columns(columns, 10)
       print(gen)
       for (idx, row) in enumerate(gen):
          print(row)
          instance.data['rows'][idx] = list(row.values())
       instance.data['columns'] = list(row.keys())
    except Exception as e:
       print(e)
       traceback.print_exc()

    # save again after setting metadata but don't get into a recursion loop!
    try:
       instance._dirty = True
       instance.save()
    finally:
       del instance._dirty



from django.dispatch import Signal
from django.db.models import signals
signals.post_save.connect(data_pre_save, sender=ExperimentData)
