import os
import traceback
from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
import common.models as cm
from .utils import hash_file
import dfndb.models as dfn
from .migration_dummy import *
import hashlib

# from jsonfield_schema import JSONSchema


# class SignalType(models.Model):
#     """
#     This model defines a table of signal types e.g. Cell_voltage.<br>
#     Experiments using the same set of SignalTypes could be assumed to be comparable (issue #16).
#     """
#     name = models.CharField(max_length=30)
#     symbol = models.CharField(max_length=8)
#     unit_name = models.CharField(max_length=30, default="Arb") # could be foreign key to a "SignalTypeUuits" table
#     unit_symbol = models.CharField(max_length=8, default="")
#
#     def __str__(self):
#         return "%s/%s" % (self.name, self.unit_symbol)


# class DeviceType(cm.BaseModel):
#     """
#     A type of thing, or specification. Provides default metadata for objects referencing this type
#     """
#     DEVICE_TYPE_NONE = 1
#     DEVICE_TYPE_CYCLER = 10
#     DEVICE_TYPE_CELL = 20
#     DEVICE_TYPE_MODULE = 30
#     DEVICE_TYPE_SENSOR = 40
#
#     DEVICE_TYPE = (
#         (DEVICE_TYPE_CELL, 'Cell'),
#         (DEVICE_TYPE_CYCLER, 'Cycler'),
#         (DEVICE_TYPE_MODULE, 'Module'),
#         (DEVICE_TYPE_SENSOR, 'Sensor')
#     )
#
#     type = models.PositiveSmallIntegerField(default=DEVICE_TYPE_NONE, choices=DEVICE_TYPE)


# class DeviceBatch(cm.BaseModel):
#     """
#     Describes a batch of things produced to the same type specification
#     """
#     manufacturer = models.ForeignKey(cm.Org, null=True, blank=True, on_delete=models.SET_NULL,
#                                      limit_choices_to={'is_mfg_cells': True})
#     manufactured_on = models.DateField(null=True, blank=True)
#     device_type = models.ForeignKey(DeviceType, null=True, blank=True, on_delete=models.SET_NULL)
#
#     class Meta:
#         verbose_name_plural = "Device Batches"


# a physical thing or specification
class Device(cm.BaseModel):
    DEVICE_TYPE_NONE = 0
    DEVICE_TYPE_CYCLER = 1
    DEVICE_TYPE_SENSOR = 10
    DEVICE_TYPE_CELL = 20
    DEVICE_TYPE_MODULE = 30
    DEVICE_TYPE_PACK = 40

    DEVICE_TYPE = (
        (DEVICE_TYPE_CELL, 'Cell'),
        (DEVICE_TYPE_MODULE, 'Module'),
        (DEVICE_TYPE_PACK, 'Pack'),
        (DEVICE_TYPE_CYCLER, 'Cycler'),
        (DEVICE_TYPE_SENSOR, 'Sensor')
    )

    type = models.PositiveSmallIntegerField(default=DEVICE_TYPE_NONE, choices=DEVICE_TYPE)
    is_template = models.BooleanField(default=False)

    class Meta:
        abstract = True


# class TestProtocol(cm.BaseModel):
#     """
#     Test Protocol description.<br>
#     TODO: Harmonise with PyBaMM protocol specifications (issue #18)
#     """
#     description = models.TextField(help_text="Protocol description, ideally in PyBaMM format")
#     parameters = JSONField(default=dict, blank=True)


# Equipment Type - e.g. model number of cycler machine
# def equipmentType_schema():
# return {
# "channels":None,
# }

# class DeviceConfig(cm.BaseModelWithSlug):
#     devices = models.ManyToManyField(Device, through='DeviceConfigNode', limit_choices_to={'is_template': True})
#
#
# class DeviceConfigNode(cm.BaseModelWithSlug):
#     deviceType = models.ForeignKey(Device, on_delete=models.CASCADE, limit_choices_to={'is_template': True})
#     deviceConfig = models.ForeignKey(DeviceConfig, on_delete=models.CASCADE)





# class EquipmentType(cm.BaseModel):
#     # validate: my manufacturer is an org with mfg_equip=True
#     pass


# EquipmentType._meta.get_field('attributes').default = equipmentType_schema

# Equipment - e.g. Bob's cycler
# class Equipment(cm.BaseModel):
#     """
#     Equipment e.g. cycler machines, etc.
#     """
#     type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True, blank=True)
#     serialNo = models.CharField(max_length=64)
#
#     class Meta:
#         verbose_name_plural = "Equipment"


# TODO: These should be actual enforceable JSON schemas, not just a collection of default values. (Issue #23)
# def cell_schema():
# return {
# "Description":"Enter cell text description here - add parameters below",
# "porosity_pct" : 10.0,
# "separator" : "example atrtribute",
# "electrolyte" : "example",
# "electrode_material_pos":"example",
# "electrode_material_neg":"example",
# }

#class Cell(Device):
#    pass

#class CellBatch(DeviceBatch):
#    materials = models.ManyToManyField(dfn.Material, through=)
#    pass


#class Module(Device):
#    pass

#class Pack(Device):
#    pass


# Cell._meta.get_field('attributes').default = cell_schema

# class CellTypeConfig(models.Model):
#    cellType=models.ForeignKey(CellType)
#    config=models.ForeignKey('CellConfig')
#    position_in_config = models.PositiveIntegerField()
#    class Meta:
#        ordering=('position_in_config',)

#class CellConfig(cm.BaseModel):
    # TODO: think about how to link cells into packs in a flexible way - supports idea #15 (SVG Diagrams)
    # e.g.:
    # cells = ManyToManyField(CellType, through=CellTypeConfig)
#    num_cells = models.PositiveIntegerField(default=1)


# Model class to represent a "system of equipment" - e.g. if more complicated than a standalone cycler machine, user can add descriptive JSON and a photo here
# in future, this can act as a tempate to create new experiments
# This replaces "New Sensor Configuration"
# class ExperimentalApparatus(cm.BaseModel):
# testEquipment = models.ManyToManyField(Equipment, through='ApparatusEquipment')
# photo = models.ImageField(upload_to='apparatus_photos', null=True, blank=True)
# class Meta:
# verbose_name_plural="Experimental apparatus"

# class ApparatusEquipment(models.Model):
# name=models.CharField(max_length=80,blank=True)
# Apparatus=models.ForeignKey(ExperimentalApparatus, on_delete=models.CASCADE)
# Equipment=models.ForeignKey(Equipment, on_delete=models.CASCADE)


# TODO: These should be actual enforcable JSON schemas, not just a collection of default values. (Issue #23)
# def experimentParameters_schema():
# return {
# "Example Parameter":"Value",
# "NumCycles": 5,
# "MinVoltage": 2.8,
# "MaxVoltage": 4.2
# }

# def experimentAnalysis_schema():
# return {
# "MeasuredCapacity":None,
# "MeasuredResistance":None,
# }

# def resultMetadata_schema():
# return {
# "Columns":{},
# "num_rows": 0,
# }

# def resultData_schema():
# return {
# "columns":[],
# "rows": []
# }


class Experiment(cm.BaseModel):
    """
    Main "Experiment" aka DataSet class. <br>
    Has many: data files (from cyclers) <br>
    Has many: devices (actual physical objects e.g. cells) <br>
    """
    #name = models.SlugField()
    # owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    #status = models.CharField(max_length=16, choices=[("edit", "Edit"), ("published", "Published")], default="edit")
    status = None
    # apparatus = models.ForeignKey(ExperimentalApparatus, on_delete=models.SET_NULL,  null=True, blank=True)
    #cells = models.ManyToManyField(Cell, related_name='experiments')
    #cellConfig = models.ForeignKey(CellConfig, on_delete=models.SET_NULL, null=True, blank=True)
    #protocol = models.ForeignKey(dfn.Method, on_delete=models.SET_NULL, null=True, blank=True)

    # parameters = JSONField(default=experimentParameters_schema, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
        return str(self.user_owner) + "/" + str(self.name) + "/" + str(self.date)


    def get_absolute_url(self):
        # return reverse('Experiment', kwargs={'slug': self.slug})
        return reverse('Experiment', kwargs={'pk': self.pk})
    # class Meta:
    # constraints = [
    # models.UniqueConstraint(fields=['owner', 'name', 'date'], name='unique_slugname')
    # ]




class RawDataFile(cm.BaseModel):
    """
        # FIXME: DataFile currently duplicates data. <br>
        # It is stored for posterity in the format in which it was uploaded. <br>
        # It is stored again as JSON within this class <br>
        # Each defined "range" is pulled out and stored again as an ArrayField. <br>
        # As yet unclear to me which is the best approach.
    """

    raw_data_file = models.FileField(upload_to='raw_data_files', null=True)
    file_hash = models.CharField(max_length=64, unique=True)

    def clean(self):
        self.file_hash = hash_file(self.raw_data_file)
        return super().clean()


# class ExperimentDataFile(cm.BaseModel):
#     raw_data_file = models.OneToOneField(RawDataFile, on_delete=models.CASCADE, related_name="ExperimentData")
#     #machine = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True, related_name='all_data')
#     # metadata = JSONField(default=resultMetadata_schema, blank=True)
#     experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True, blank=True,
#                                    related_name='data_files')
#
#     # import_columns = models.ManyToManyField(SignalType, blank=True)
#     # parameters = JSONField(default=experimentParameters_schema, blank=True)
#     # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
#     def __str__(self):
#         return os.path.basename(self.raw_data_file.name)
#
#     class Meta:
#         verbose_name_plural = "Experiment Data Files"


# class DataRange(cm.BaseModel):
#     """
#     DataRange - each data file contains numerous ranges e.g. charge & discharge cycles. Their data might overlap. <br>
#     TODO: Write (or find) code to segment data into ranges. <br>
#     TODO: Convert this into a JSON Schema within ExperimentData - see Git issue #23 <br>
#     """
#     dataFile = models.ForeignKey(ExperimentDataFile, on_delete=models.SET_NULL, null=True, blank=True,
#                                  related_name='ranges')
#     file_offset = models.PositiveIntegerField(default=0)
#     label = models.CharField(max_length=32, null=True)
#     protocol_step = models.PositiveIntegerField()
#     step_action = models.CharField(max_length=8,
#                                    choices=[('chg', 'Charging'), ('dchg', 'Discharging'), ('rest', 'Rest'),
#                                             (None, 'Undefined')], null=True)
#     # TODO: Possibly split these arrays into a new object
#     ts_headers = ArrayField(models.CharField(max_length=32, null=True), null=True, blank=True)
#     ts_data = ArrayField(ArrayField(models.FloatField(null=True), null=True), null=True, blank=True)
#
#     # TODO: These need a schema
#     # events = JSONField(null=True, blank=True)
#     # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
#     def __str__(self):
#         return "%s/%d: %s" % (self.dataFile, self.id, self.label)
#
#     class Meta:
#         verbose_name_plural = "Data Ranges"


# When saving a data file, call this to parse the data.
# TODO, move this out of models.py
def data_pre_save(sender, instance, *args, **kwargs):
    if not instance:
        return
    if hasattr(instance, '_dirty'):
        return

    try:
        print("result_post_save: Sender: %s, Instance: %s, args: %s, kwargs: %s, base_loc: %s, Filename: %s" % (
            sender, instance, args, kwargs, instance.raw_data_file.storage.base_location, instance.raw_data_file.name))
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

#signals.post_save.connect(data_pre_save, sender=ExperimentDataFile)
