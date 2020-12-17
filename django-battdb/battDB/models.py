import os
import traceback
from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

import common.models as cm
import dfndb.models as dfn

from .migration_dummy import *
from datetime import datetime
import django.core.exceptions

from rest_framework.authtoken.models import Token

from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from galvanalyser.harvester.parsers.maccor_parser import MaccorXLSParser
from galvanalyser.harvester.parsers.parser import Parser
import pandas.errors
from .utils import parse_data_file, get_parser
import json

from django.db.models.signals import post_delete
from common.utils import file_cleanup

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
    A device specification is a template for creating a devcice or batch of devices in the system. <BR>
    Specifications are structured as a tree, so that each device can be composed of sub- devices
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
    A device or batch of devices is a physical, tangible thing produced to a given specification.
    """
    specification = models.ForeignKey(DeviceSpecification, null=True, blank=False, on_delete=models.SET_NULL,
                                      limit_choices_to={'abstract': False},
                                      help_text="Batch Specification")
    manufacturer = models.ForeignKey(cm.Org, default=1, on_delete=models.SET_DEFAULT, null=True)
    serialNo = models.CharField(max_length=60, default="%d", blank=True, help_text=
                                "Batch number, optionally indicate serial number format")
    batch_size = models.PositiveSmallIntegerField(default=1)
    manufacturing_protocol = models.ForeignKey(dfn.Method, on_delete=models.SET_NULL, null=True, blank=True,
                                               limit_choices_to={'type': dfn.Method.METHOD_TYPE_MANUFACTURE},
                                               help_text="Test protocol used in this experiment")
    manufactured_on = models.DateField(default=datetime.now)

    def __str__(self):
        return "%s %s (%d off) %s" % (self.manufacturer, self.specification, self.batch_size, self.manufactured_on)

    class Meta:
        verbose_name = "Device or Batch"
        verbose_name_plural = "Devices"

    # FIXME: Cannot bulk_create with seq_num
    # def clean(self):
    #     BatchDevice.objects.bulk_create

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


class BatchDevice(cm.HasAttributes, cm.HasNotes):
    batch = models.ForeignKey(DeviceBatch, on_delete=models.CASCADE)
    seq_num = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), ], help_text=
                                               "Sequence number within batch")

    def get_used_in_exps(self):
        return ExperimentDevice.objects.filter(deviceBatch=self.batch, batch_seq=self.seq_num)

    def last_measured_SoH(self):
        return self.attributes.get('state_of_health') or "Not tested"

    def used_in(self):
        return "%d Experiments" % self.get_used_in_exps().count()

    def serial(self):
        try:
            return self.batch.serialNo % self.seq_num
        except TypeError:
            return self.batch.serialNo + "/" + str(self.seq_num)

    class Meta:
        unique_together = ['batch', 'seq_num']

    def clean(self):
        if self.seq_num > self.batch.batch_size:
            raise ValidationError("Batch sequence ID cannot exceed batch size!")
        # TODO: Can compute device stats here
        self.attributes['state_of_health'] = "100%"
        #self.attributes['used_in_exps'] = self.get_used_in_exps()

    def __str__(self):
        return str(self.batch.specification) + "/" + self.serial()


class DeviceConfig(cm.BaseModel):
    """
    A configuration of device templates to represent how devices are connected in a module, pack, or experimental set-up
    """
    TYPE_CHOICES=(
        ("module", "Module"),
        ("expmt", "Experiment"),
    )
    devices = models.ManyToManyField(DeviceSpecification, through='DeviceConfigNode')
    config_type = models.CharField(max_length=10, default="module", choices=TYPE_CHOICES)

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
    device = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE, limit_choices_to={'abstract': True},
                               help_text="Related device specification e.g. cell or sensor.")
    config = models.ForeignKey(DeviceConfig, on_delete=models.CASCADE,
                               help_text="Config instance to which this node belongs")
    device_position_id = models.CharField(max_length=20, null=True, blank=True,
                                          help_text="Position of device in pack e.g. 1 - identifies this device")
    pos_netname = models.CharField(max_length=20, null=True, blank=True,
                                   help_text="Name of electrical signal at positive terminal e.g. cell_1_v")
    neg_netname = models.CharField(max_length=20, null=True, blank=True,
                                   help_text="Name of electrical signal at negative terminal e.g. pack_-ve")

    def __str__(self):
        return str(self.config) + "/" + str(self.device) + "_" + str(self.device_position_id)




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



class Parser(cm.BaseModelMandatoryName):
    """
    Parsers for experimental device data. <BR>
    TODO: In future, these could be user-defined in Python code via this interface (with appropriate permissions) <BR>
     This would require all parsing to be done in a sandboxed environment on a separate server (which it should anyway)
    """
    # module = models.FileField(max_length=100, default="", blank=True,
    #                           help_text="Python module to run this parser")
    FORMAT_CHOICES = [("none", "None"), ("auto", "Auto-detect"),
                      ("csv", "Generic CSV/TSV"),
                      ("biologic", "Biologic CSV/TSV/MPT"),
                      ("maccor", "Maccor XLS/XLSX"),
                      ("ivium", "Ivium TXT"),
                      ("novonix", "Novonix TXT"),
                      ]
    file_format = models.CharField(max_length=20, default="auto",
                                   choices=FORMAT_CHOICES,
                                   help_text="File format override, or use 'auto' to attempt detection")
    parameters = models.ManyToManyField(dfn.Parameter, through="SignalType")



class Equipment(cm.BaseModel):
    """
    Definitions of equipment such as cycler machines
    """
    specification = models.ForeignKey(DeviceSpecification, null=True, blank=False, on_delete=models.SET_NULL,
                                      limit_choices_to={'abstract': False},
                                      help_text="Batch Specification")
    manufacturer = models.ForeignKey(cm.Org, default=1, on_delete=models.SET_DEFAULT, null=True)
    serialNo = models.CharField(max_length=60, default="", blank=True, help_text=
                                "Batch number, optionally indicate serial number format")
    default_parser = models.ForeignKey(Parser, null=True, blank=True, on_delete=models.SET_NULL,
                                       help_text="Default parser for this equipment's data")

    class Meta:
        verbose_name_plural="Equipment"


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
    config = models.ForeignKey(DeviceConfig, on_delete=models.SET_NULL, null=True, blank=True, related_name='used_in',
                               limit_choices_to={'config_type': 'expmt'},
                               help_text="All devices in the same experiment must be of the same configuration, "
                                         "i.e. an experiment must use all single cells, or all 2s2p modules, "
                                         "not a mixture of both.")

    protocol = models.TextField(null=True, blank=True,
                                help_text="Test protocol used in this experiment")

    # parameters = JSONField(default=experimentParameters_schema, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)


    def devices_(self):
        return self.devices.count()

    def files_(self):
        return self.data_files.count()

    def cycles_(self):
        # TODO: Count total number of cycles
        return "?"

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


class ExperimentDataFile(cm.BaseModel):
    """
        ExperimentDataFile (EDF) is the class tying data files, parsed data tables, and experiments together. <>BR>
        It contains all of the time-series numerical data as a Postgres ArrayField(ArrayField(FloatField))) <br>
        Text data should be added as Events.
        Raw data files should be uploaded and referenced, where available.
    """
    ts_headers = ArrayField(models.CharField(max_length=32), blank=True, null=True, editable=False,
                            help_text="Parsed data column headers")
    ts_data = ArrayField(ArrayField(models.FloatField()), blank=True, null=True, editable=False,
                         help_text="Parsed time-series data columns (note: this is bulky data!)")
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name="data_files")

    machine = models.ForeignKey(Equipment, null=True, blank=True, on_delete=models.SET_NULL,
                                help_text="Equipment on which this data was recorded")

    devices = models.ManyToManyField(DeviceBatch, through='ExperimentDevice', related_name="used_in")

    protocol = models.ForeignKey(dfn.Method, on_delete=models.SET_NULL, null=True, blank=True,
                                 limit_choices_to={'type': dfn.Method.METHOD_TYPE_EXPERIMENTAL},
                                 help_text="Test protocol used in this experiment")

    #import_columns = models.ManyToManyField(dfn.Parameter, blank=True)
    # parameters = JSONField(default=experimentParameters_schema, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)

    def num_cycles(self):
        return self.ranges.filter(step_action='cycle').count() + \
               self.ranges.filter(step_action=['chg', 'dchg']).count()/2.0

    def num_ranges(self):
        return self.ranges.count()

    def file_rows(self):
        return self.attributes.get('file_rows') or 0

    def parsed_ranges(self):
        return self.attributes.get('parsed_ranges') or []

    def parsed_columns(self):
        return self.attributes.get('parsed_columns') or []

    def missing_columns(self):
        return self.attributes.get('missing_columns') or []

    def file_columns(self):
        return self.attributes.get('file_columns') or []

    def is_parsed(self):
        return self.parse and len(self.file_columns()) > 0
    is_parsed.boolean = True

    def file_exists(self):
        if hasattr(self, 'raw_data_file'):
            return self.raw_data_file.exists()
        return False
    file_exists.boolean = True

    def file_hash(self):
        if self.raw_data_file is not None:
            return self.raw_data_file.hash
        # else
        return "N/A"

    def create_ranges(self):
        ranges = self.attributes.get('range_config') or dict()
        for name, config in ranges.items():
            rng_q = DataRange.objects.get_or_create(dataFile=self, label=name)
            rng = rng_q[0]
            rng.file_offset_start = config.get('start') or 0
            rng.file_offset_end = config.get('end') or 0
            rng.protocol_step = config.get('step') or 0
            rng.step_action = config.get('action') or 0
            rng.save()

    def clean(self):
        if self.name is None or self.name == "":
            try:
                self.name = str(self.raw_data_file)
            except UploadedFile.DoesNotExist:
                self.name = "Unnamed data set"
        if self.file_exists() and self.raw_data_file.parse:
            cols = [c.col_name for c in self.use_parser.columns.all().order_by('order')]
            parser = parse_data_file(self, columns=cols)
            gen = parser.get_data_generator_for_columns(self.parsed_columns(), 10)
            self.ts_headers = self.parsed_columns()
            self.ts_data = list(gen)
            if self.is_parsed():
                self.create_ranges()
            del parser

        super().clean()

    class Meta:
        # verbose_name_plural = "4. Data Files"
        # verbose_name_plural = "Data Files"
        verbose_name = "Data File"
        #unique_together = ['raw_data_file', 'experiment']


class UploadedFile(cm.HashedFile):
    local_path = models.CharField(max_length=1024, default="", blank=True)
    local_date = models.DateTimeField(default=datetime.now)
    parse = models.BooleanField(default=False, help_text="Set to True to import data on save")
    use_parser = models.ForeignKey(Parser, null=True, blank=True, on_delete=models.SET_NULL)
    parsed_metadata = models.JSONField(editable=False, default=dict,
                                       help_text="metadata automatically extracted from the file")

class ExperimentDevice(models.Model):
    """
    3-way join table, identifies devices in experiments, link devices to data files
    """
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name="devices")
    # FIXME: DeviceBatch  / batch_id could be a foreignKey to DeviceBatch!
    #  but maybe this way is actually better (avoids accidental data loss at the cost of potential inconsistency)
    deviceBatch = models.ForeignKey(DeviceBatch, on_delete=models.CASCADE)
    batch_seq = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),], help_text=
                                                 "sequence number of device within batch")
    device_pos = models.CharField(max_length=20, default="cell_xx", help_text=
                                  "Device Position ID in Experiment Config - e.g. Cell_A1 for the first cell of"
                                  "a series-parallel pack")
    data_file = models.ForeignKey(ExperimentDataFile, null=True, blank=True, on_delete=models.SET_NULL)

    # TODO: implement id_to_serialno and serialno_to_id functions
    def getSerialNo(self):
        return "FIXME"

    def clean(self):
        if self.deviceBatch is not None and self.batch_seq > self.deviceBatch.batch_size:
            raise ValidationError("Batch sequence ID cannot exceed batch size!")
        elif self.deviceBatch is not None:
            batchDev = BatchDevice.objects.get_or_create(batch=self.deviceBatch, seq_num=self.batch_seq)

    def __str__(self):
        return self.device_pos

    class Meta:
        unique_together = [['device_pos', 'data_file'],  # cannot have the same device position ID twice in a data file
                           # cannot use the same device twice in a data file
                           ['experiment', 'deviceBatch', 'batch_seq', 'data_file']]




class DataColumn(models.Model):
    data_file = models.ForeignKey(ExperimentDataFile, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=40, default='Ns')
    RESAMPLE_CHOICES = (
        ('none', 'Do not resample'),
        ('on_change', 'Sample on change'),
        ('decimate', 'Take every Nth sample'),
        ('average', 'Average every Nth sample'),
        ('max',     'Maximum every Nth sample'),
        ('min',     'Minimum every Nth sample'),
    )
    resample = models.CharField(max_length=10, choices=RESAMPLE_CHOICES, default="none", help_text=
                                "Resampling option - TO BE IMPLEMENTED - currently has no effect")
    resample_n = models.PositiveSmallIntegerField(default=1, validators=(MinValueValidator(1),), help_text=
                                                  "Resampling divisor - TO BE IMPLEMENTED")

    parameter = models.ForeignKey(dfn.Parameter, null=True, on_delete=models.SET_NULL, blank=True, help_text=
                                  "Map this column to a parameter on a device")
    device = models.ForeignKey(ExperimentDevice, null=True, blank=True, on_delete=models.SET_NULL, help_text=
                               "Device id for parameter mapping")

    def clean(self):
        if self.device is not None and self.device.experiment != self.data_file.experiment:
            raise ValidationError("Cannot use device instance from a different experiment")
        if self.device is None:
            self.parameter = None
        if self.resample == "none" or self.resample == "on_change":
            self.resample_n = 1

    def experiment(self):
        return self.data_file.exeriment()

    class Meta:
        unique_together = [['device', 'data_file'], ['column_name', 'data_file']]
        verbose_name = "Column Mapping"
        verbose_name_plural = "Data Column Mappings to Device Parameters"


class DataRange(cm.HasAttributes, cm.HasNotes, cm.HasCreatedModifiedDates):
    """
    DataRange - each data file contains numerous ranges e.g. charge & discharge cycles. Their data might overlap. <br>
    TODO: Write (or find) code to segment data into ranges. <br>
    TODO: Convert this into a JSON Schema within ExperimentData - see Git issue #23 <br>
    """
    dataFile = models.ForeignKey(ExperimentDataFile, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='ranges')
    file_offset_start = models.PositiveIntegerField(default=0)
    file_offset_end = models.PositiveIntegerField(default=0)
    label = models.CharField(max_length=32, default="all")
    protocol_step = models.PositiveSmallIntegerField(default=0)
    step_action = models.CharField(max_length=8,
                                   choices=[('chg', 'Charging'), ('dchg', 'Discharging'),
                                            ('cycle', 'Full cycle'), ('rest', 'Rest'),
                                            ('all', 'Entire series'),
                                            ('user', 'User defined')], default='all')


    # TODO: These need a schema
    # events = JSONField(null=True, blank=True)
    # analysis = JSONField(default=experimentAnalysis_schema, blank=True)
    def __str__(self):
        return "%s/%d: %s" % (self.dataFile or "None", self.id or 0, self.label or "")

    class Meta:
        verbose_name_plural = "Data Ranges"
        unique_together = [['dataFile', 'label']]


class Harvester(cm.BaseModelMandatoryName):
    """
    "Harvester" clients are programs which run on a scientist's computer or cycler machine,
    and monitor a folder for new data files.<BR>
    Any new data files picked up are automatically uploaded to this system using a REST API. <BR>
    Each Harvester client needs its own username and authentication token to use the API
    """
  #  upload_to_folder = models.ForeignKey(FileFolder, on_delete=models.CASCADE, default=0)
    attach_to_experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True, blank=True)
    equipment_type = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    file_types = models.CharField(max_length=20, default="*.csv",
                                  help_text="File type pattern to monitor")
    parser_config = models.ForeignKey(Parser, null=True, on_delete=models.SET_NULL)
    local_folder = models.CharField(max_length=500, default=".")
    # parser = models.CharField(max_length=20, default="csv",
    #                           choices=Parser.FORMAT_CHOICES,
    #                           help_text="Default parser to use")

    class Meta:
        unique_together = ['name', 'user_owner']


class SignalType(models.Model):
    parameter = models.ForeignKey(dfn.Parameter, on_delete=models.CASCADE)
    col_name = models.CharField(max_length=50, default="")
    order = models.PositiveSmallIntegerField(default=5,
                                             help_text="override column ordering")
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return self.col_name

# from django.dispatch import Signal
# from django.db.models import signals
#
# signals.post_save.connect(data_pre_save, sender=ExperimentDataFile)


# FIXME: This doesn't seem to be working. Files remain on disk after UploadedFile object is deleted
# Although we probably won't be deleting files anyway.
post_delete.connect(file_cleanup, sender=UploadedFile, dispatch_uid="gallery.image.file_cleanup")

