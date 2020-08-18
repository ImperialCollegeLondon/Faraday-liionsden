import os
import traceback
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
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
   pass

def cell_schema():
    return {
       "Description":"Enter cell text description here - add parameters below",
       "porosity_pct" : 10.0,
       "separator" : "example atrtribute",
       "electrolyte" : "example",
       "electrode_material_pos":"example",
       "electrode_material_neg":"example",
    }

class CellType(HasAttributes):
    pass
CellType._meta.get_field('attributes').default = cell_schema

class CellBatch(HasAttributes):
    manufactured_on = models.DateField(null=True, blank=True)
    manufacturer    = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    cells_schema = JSONField(default=dict, blank=True)
    class Meta:
       verbose_name_plural="CellBatches"
CellBatch._meta.get_field('attributes').default = cell_schema

class Cell(HasAttributes):
    batch = models.ForeignKey(CellBatch, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(CellType, on_delete=models.SET_NULL, null=True, blank=True)
Cell._meta.get_field('attributes').default = cell_schema

#class CellTypeConfig(models.Model):
#    cellType=models.ForeignKey(CellType)
#    config=models.ForeignKey('CellConfig')
#    position_in_config = models.PositiveIntegerField()
#    class Meta:
#        ordering=('position_in_config',)

class CellConfig(HasAttributes):
    # TODO: think about how to link cells into packs in a flexible way - supports idea #15 (SVG Diagrams)
    # e.g. use this
    # cells = ManyToManyField(CellType, through=CellTypeConfig)
    num_cells = models.PositiveIntegerField(default=1)

class ExperimentalApparatus(HasAttributes):
    testEquipment = models.ManyToManyField(Equipment)
    photo = models.ImageField(upload_to='apparatus_photos', null=True, blank=True)
    class Meta:
       verbose_name_plural="Experimental apparatus"

def experimentParameters_schema():
    return {
        "Example Parameter":"Value",
        "NumCycles": 5,
        "MinVoltage": 2.8,
        "MaxVoltage": 4.2
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
    cellConfig = models.ForeignKey(CellConfig, on_delete=models.SET_NULL,  null=True, blank=True)
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

class ExperimentDataFile(models.Model):
    raw_data_file = models.FileField(upload_to='raw_data_files',null=True)
    machine = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True, related_name='all_data')
    metadata = JSONField(default=resultMetadata_schema, blank=True)
    data = JSONField(default=resultData_schema, blank=True, editable=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True, blank=True, related_name='data_file')
    import_columns = models.ManyToManyField(SignalType, blank=True)
    parameters = JSONField(default=experimentParameters_schema, blank=True)
    analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
       return os.path.basename(self.raw_data_file.name)
    class Meta:
       verbose_name_plural="Experiment Data Files"


# TODO: Convert this into a JSON Schema within ExperimentData - see Git issue #23
class DataRange(models.Model):
    dataFile = models.ForeignKey(ExperimentDataFile, on_delete=models.SET_NULL, null=True, blank=True, related_name='ranges')
    file_offset = models.PositiveIntegerField(default=0)
    label= models.CharField(max_length=32, null=True)
    protocol_step = models.PositiveIntegerField()
    step_action = models.CharField(max_length=8, choices=[('chg', 'Charging'), ('dchg', 'Discharging'), ('rest', 'Rest'), (None, 'Undefined')], null=True)
    # TODO: Possibly split these arrays into a new object
    ts_headers = ArrayField(models.CharField(max_length=32, null=True), null=True, blank=True)
    ts_data = ArrayField(ArrayField(models.FloatField(null=True), null=True), null=True, blank=True)
    # TODO: These need a schema
    events = JSONField(null=True, blank=True)
    analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
       return (str(self.label))
    class Meta:
       verbose_name_plural="Data Ranges"

def data_pre_save(sender, instance, *args, **kwargs):
    if not instance:
       return
    if hasattr(instance, '_dirty'):
       return

    try:
       print("result_post_save: Sender: %s, Instance: %s, args: %s, kwargs: %s, base_loc: %s, dilename: %s" % (sender, instance, args, kwargs, instance.raw_data_file.storage.base_location, instance.raw_data_file.name))
       filepath = "/".join([instance.raw_data_file.storage.base_location, instance.raw_data_file.name])
       # TODO: Work out which type of file it is and call the correct parser!
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
signals.post_save.connect(data_pre_save, sender=ExperimentDataFile)

