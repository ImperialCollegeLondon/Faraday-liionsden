import os
import traceback
from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
import common.models as cm
import dfndb.models as dfn
from .migration_dummy import *
from datetime import datetime
import django.core.exceptions

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




class DeviceSpecification(cm.BaseModel, cm.HasMPTT):
    """
    A device specification.
    """
    # TYPE_CHOICES = [
    #     ("component", "Component part of a cell"),
    #     ("cell", "Single cell"),
    #     ("module", "Module containing cells"),
    #     ("battery", "Battery pack containing modules"),
    #     ("sensor", "Sensor attached to a device"),
    #     ("cycler", "Cycler Machine"),
    # ]
    parameters = models.ManyToManyField(dfn.Parameter, through='DeviceParameter')
    abstract = models.BooleanField(default=False,
                                   verbose_name="Abstract Specification",
                                   help_text="This specifies an abstract device, e.g. 'Cell' with child members such as"
                                             "'Positive Electrode, Negative Electrode, Electrolyte etc. <BR>"
                                             "If this is set to True, then all metadata declared here must be "
                                             "overridden in child classes. An abstract specification cannot be used "
                                             "to define a physical device or batch.")
    complete = models.BooleanField(default=False,
                                   help_text="This device is complete - it can be used in experiments without a parent")
    device_type = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                    limit_choices_to={'abstract': True}, related_name="specifies",
                                    help_text="Device type. e.g. Cell, Module, Battery Pack. <BR>"
                                              "An abstract specification cannot have a device type - "
                                              "they define the device types.")
   # json = JSONEditableField()

    def clean(self):
        if self.abstract and self.device_type is not None:
            raise django.core.exceptions.ValidationError("Abstract specifications cannot have a device type")
        return super(DeviceSpecification, self).clean()
    class Meta:
        # verbose_name_plural = "1. Device Specifications"
        verbose_name_plural = "Device Specifications"


class DeviceParameter(cm.HasName):
    """
    Parameters on device
    """
    spec = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE)
    parameter = models.ForeignKey(dfn.Parameter, on_delete=models.CASCADE)
    material = models.ForeignKey(dfn.Material, on_delete=models.CASCADE, blank=True, null=True)
    value = models.JSONField(blank=True, null=True)
    inherit_to_children = models.BooleanField(default=False)

    def __str__(self):
        return str(self.parameter)

    class Meta:
        unique_together = [('spec', 'parameter', 'material'), ('spec', 'name')]






class DeviceBatch(cm.BaseModelNoName, cm.HasMPTT):
    """
    Describes a batch of things produced to the same type specification
    """
    specification = models.ForeignKey(DeviceSpecification, null=True, blank=False, on_delete=models.SET_NULL,
                                      limit_choices_to={'abstract': False},
                                      help_text="Batch Specification")
    manufacturer = models.ForeignKey(cm.Org, default=1, on_delete=models.SET_DEFAULT, null=True)
    serialNo = models.CharField(max_length=60, default="", blank=True, help_text=
                                "Batch number, optionally indicate serial number format")
    batch_size = models.PositiveSmallIntegerField(default=1)
    manufactured_on = models.DateField(default=datetime.now)

    def __str__(self):
        return "%s %s (%d off) %s" % (self.manufacturer, self.specification, self.batch_size, self.manufactured_on)

    class Meta:
        verbose_name = "Device or Batch"
        verbose_name_plural = "Devices"


    # class Meta:
    #     verbose_name_plural = "Device Tree"
    # def __init__(self, *args, **kwargs):
    #     self._meta.get_field('inherit_metadata').verbose_name = "Is Specification"
    #     self._meta.get_field('inherit_metadata').default = True
    #     self._meta.get_field('inherit_metadata').help_text = "Set to True if this entry is to be used " \
    #                                                          "as a specification for other devices." \
    #                                                          "Metadata will be re-used inside child nodes" \
    #                                                          "e.g. if metadata describes electrode material " \
    #                                                          "for a pack, the cells will default to the same"
    #     super(Device, self).__init__(*args, **kwargs)


# class DeviceList(Device):
#     """
#     List view of devices
#     """
#     class Meta:
#         verbose_name_plural = "Device List"
#         proxy = True


class BatchDevice(cm.HasAttributes):
    batch = models.ForeignKey(DeviceBatch, on_delete=models.CASCADE)
    batch_index = models.PositiveSmallIntegerField(default=1)
    serialNo = models.CharField(max_length=60, default="", blank=True, help_text=
                                "Serial Number")
    class Meta:
        unique_together = ['batch', 'batch_index']


class DeviceConfig(cm.BaseModel):
    """
    A configuration of device templates to represent how devices are connected in a module, pack, or experimental set-up
    """
    devices = models.ManyToManyField(DeviceSpecification, through='DeviceConfigNode')

    class Meta:
        verbose_name_plural = "Device Configurations"


class DeviceConfigNode(models.Model):
    """
    Self-referential model - defines a chain of devices electrically connected together, like a netlist
    FIXME: I would like to use 'limit_choices_to to' dynamically restrict choices based on 'config',
           to ensure that all nodes in chain are part of the same config & net,
           i.e. you cannot link to a node in a different config.
           But it's a limitation of django that limit_choices_to cannot apply dynamically
           limit_choices_to={'config':config} would result in an error.
           Maybe there is a flaw in my database design here? This might not need to be a ManyToMany 'through' table.
    """
    device = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE, limit_choices_to={'abstract': False},
                               help_text="Related device specification e.g. cell or sensor. Must have is_template=True")
    config = models.ForeignKey(DeviceConfig, on_delete=models.CASCADE,
                               help_text="Config instance to which this node belongs")
    device_position_id = models.CharField(max_length=20, null=True, blank=True,
                                          help_text="Position of device in pack e.g. 1 - identifies this device")
    next = models.ForeignKey('DeviceConfigNode', null=True, blank=True, on_delete=models.SET_NULL,
                             help_text="Connected node in chain. Must be part of the same config."
                                       "In a series pack, this would be the negative terminal of the next cell")
    device_terminal_name = models.CharField(max_length=10, null=True, blank=True, help_text=
                                            "Name of device port or terminal. e.g. 'Anode'")
    net_name = models.CharField(max_length=20, null=True, blank=True,
                                help_text="Name of electrical signal e.g. cell_1_v")

    def __str__(self):
        return str(self.config) + "/" + str(self.net_name) + str(self.device_terminal_name)




# class CompositeDevice(Device):
#     """
#     Composite device comprising multiple sub-devices
#     """
#     moduleConfig = models.ForeignKey(DeviceConfig, null=True, blank=True, on_delete=models.SET_NULL,
#                                      help_text="Module config link", related_name="used_by_modules")
#
#     deviceList = models.ManyToManyField(Device, through='ModuleDevice', related_name="my_module")
#     MODULE_TYPE_CHOICES = [
#         (Device.DEVICE_TYPE_MODULE, "Module"),
#         (Device.DEVICE_TYPE_PACK, "Pack"),
#         (Device.DEVICE_TYPE_APPARATUS, "Apparatus"),
#     ]
#
#     def __init__(self, *args, **kwargs):
#         self._meta.get_field('devType').default = Device.DEVICE_TYPE_MODULE
#         self._meta.get_field('devType').choices = self.MODULE_TYPE_CHOICES
#
#
# class ModuleDevice(models.Model):
#     module = models.ForeignKey(CompositeDevice, on_delete=models.CASCADE, related_name="device_members")
#     device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="modules")
#     device_position_id = models.CharField(max_length=20, null=True, blank=True,
#                                           help_text="Position of device in pack e.g. 1 - identifies this device")

# class EquipmentType(cm.BaseModel):
#     # validate: my manufacturer is an org with mfg_equip=True
#     pass


# EquipmentType._meta.get_field('attributes').default = equipmentType_schema


# class Equipment(cm.Thing):
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


# class DataParser(models.Model):
#     pass

# class Equipment(cm.BaseModel):
#     specification = models.ForeignKey(DeviceSpecification, null=True, blank=False, on_delete=models.SET_NULL,
#                                       limit_choices_to={'abstract': False},
#                                       help_text="Batch Specification")
#     manufacturer = models.ForeignKey(cm.Org, default=1, on_delete=models.SET_DEFAULT, null=True)
#     serialNo = models.CharField(max_length=60, default="", blank=True, help_text=
#                                 "Batch number, optionally indicate serial number format")


class Experiment(cm.BaseModel):
    """
    Main "Experiment" aka DataSet class. <br>
    Has many: data files (from cyclers) <br>
    Has many: devices (actual physical objects e.g. cells) <br>
    """
    date = models.DateField(default=datetime.now)
    # apparatus = models.ForeignKey(ExperimentalApparatus, on_delete=models.SET_NULL,  null=True, blank=True)
    # device = models.ForeignKey(DeviceSpecification, related_name='used_in', null=True, blank=True,
    #                            on_delete=models.SET_NULL,
    #                            limit_choices_to={'abstract': False, 'complete': True})
    #config = models.ForeignKey(DeviceConfig, on_delete=models.SET_NULL, null=True, blank=True, related_name='used_in')
    protocol = models.ForeignKey(dfn.Method, on_delete=models.SET_NULL, null=True, blank=True,
                                 limit_choices_to={'type': dfn.Method.METHOD_TYPE_EXPERIMENTAL})
    data_files = models.ManyToManyField(cm.UploadedFile, through="ExperimentDataFile")

    # parameters = JSONField(default=experimentParameters_schema, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
        return str(self.user_owner) + " " + str(self.name) + " " + str(self.date)


    def get_absolute_url(self):
        # return reverse('Experiment', kwargs={'slug': self.slug})
        return reverse('Experiment', kwargs={'pk': self.pk})
    # class Meta:
    # constraints = [
    # models.UniqueConstraint(fields=['owner', 'name', 'date'], name='unique_slugname')
    # ]

    # def __init__(self, *args, **kwargs):
    #     self._meta.get_field('parent').limit_choices_to = {"inherit_metadata": True,
    #                                                        "devType": "module"}
    #     super(Experiment, self).__init__(*args, **kwargs)
    # class Meta:
    #     verbose_name_plural = "Experiments"
    #     verbose_name = "dataset"


class ExperimentDataFile(cm.BaseModelNoName):
    """
        # FIXME: DataFile currently duplicates data. <br>
        # It is stored for posterity in the format in which it was uploaded. <br>
        # It is stored again as JSON within this class <br>
        # Each defined "range" is pulled out and stored again as an ArrayField. <br>
        # As yet unclear to me which is the best approach.
    """

    raw_data_file = models.ForeignKey(cm.UploadedFile, null=True, blank=False, on_delete=models.SET_NULL,
                                      related_name="used_by")

    mappings = models.ManyToManyField(DeviceBatch, through='DataColumn', blank=True, related_name='data_files')
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True, blank=True)
    parsed_data = models.JSONField(editable=False, default=dict)
    #cycler_machine = models.ForeignKey(DeviceBatch, null=True, on_delete=models.SET_NULL)

    #import_columns = models.ManyToManyField(dfn.Parameter, blank=True)
    # parameters = JSONField(default=experimentParameters_schema, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)

    def num_cycles(self):
        return 0

    def columns(self):
        return []

    def is_parsed(self):
        return self.num_cycles() > 0
    is_parsed.boolean = True

    def file_exists(self):
        if self.raw_data_file is not None:
            return self.raw_data_file.exists()
        return False
    file_exists.boolean = True

    def file_hash(self):
        return self.raw_data_file.file_hash()



    def __str__(self):
        return str(self.raw_data_file)

    class Meta:
        # verbose_name_plural = "4. Data Files"
        # verbose_name_plural = "Data Files"
        verbose_name = "Data File"
        unique_together = ['raw_data_file', 'experiment']


class DataColumn(models.Model):
    data = models.ForeignKey(ExperimentDataFile, on_delete=models.CASCADE)
    parameter = models.ForeignKey(dfn.Parameter, null=True, on_delete=models.SET_NULL,
                                  default=4)
    column_name = models.CharField(max_length=20)
    device = models.ForeignKey(DeviceBatch, on_delete=models.CASCADE)
    batch_id = models.PositiveSmallIntegerField(default=0)

    def serialNo(self):
        return "bork"

    def experiment(self):
        return self.data.exeriment()

    class Meta:
        unique_together = ['device', 'data', 'batch_id']
        verbose_name = "Column Mapping"
        verbose_name_plural = "Data Column Mappings to Device Parameters"


class DataRange(cm.HasAttributes, cm.HasName, cm.HasNotes, cm.HasCreatedModifiedDates):
    """
    DataRange - each data file contains numerous ranges e.g. charge & discharge cycles. Their data might overlap. <br>
    TODO: Write (or find) code to segment data into ranges. <br>
    TODO: Convert this into a JSON Schema within ExperimentData - see Git issue #23 <br>
    """
    dataFile = models.ForeignKey(ExperimentDataFile, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='ranges')
    file_offset = models.PositiveIntegerField(default=0)
    label = models.CharField(max_length=32, null=True)
    protocol_step = models.PositiveIntegerField()
    step_action = models.CharField(max_length=8,
                                   choices=[('chg', 'Charging'), ('dchg', 'Discharging'), ('rest', 'Rest'),
                                            (None, 'Undefined')], null=True)
    # TODO: Possibly split these arrays into a new object
    ts_headers = ArrayField(models.CharField(max_length=32, null=True), null=True, blank=True)
    ts_data = ArrayField(ArrayField(models.FloatField(null=True), null=True), null=True, blank=True)

    # TODO: These need a schema
    # events = JSONField(null=True, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
        return "%s/%d: %s" % (self.dataFile, self.id, self.label)

    class Meta:
        verbose_name_plural = "Data Ranges"


# When saving a data file, call this to parse the data.
# TODO, move this out of models.py
def data_pre_save(sender, instance, *args, **kwargs):
    if not instance:
        return
    if hasattr(instance, '_dirty'):
        print("moo")
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

signals.post_save.connect(data_pre_save, sender=ExperimentDataFile)


