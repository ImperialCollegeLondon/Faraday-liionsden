from __future__ import annotations

from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse

import common.models as cm
import dfndb.models as dfn
from common.validators import (
    validate_binary_file,
    validate_pdf_file,
    validate_settings_file,
)
from parsing_engines import available_parsing_engines, parse_data_file


class DeviceSpecification(cm.BaseModelMandatoryName, cm.HasMPTT):
    """A template for creating a device or batch of devices in the system.

    <br> Specifications are structured as a tree, so that each device can be composed of
    sub-devices
    """

    parameters = models.ManyToManyField(dfn.Parameter, through="DeviceParameter")
    components = models.ManyToManyField(dfn.Component, through="DeviceComponent")
    abstract = models.BooleanField(
        default=False,
        verbose_name="Abstract Specification",
        help_text="""
        This specifies an abstract device, e.g. 'Cell' with child members
        such as 'Positive Electrode, Negative Electrode, Electrolyte etc.
        If this is set to True, then all metadata declared here must be
        overridden in child classes. An abstract specification cannot be used
        to define a physical device or batch.
        """,
    )
    complete = models.BooleanField(
        default=False,
        help_text="This device is complete - it can be used in experiments without a "
        "parent",
    )
    device_type = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to={"abstract": True},
        related_name="specifies",
        help_text="""Device type. e.g. Cell, Module, Battery Pack. An abstract
        specification cannot have a device type -  they define the device types.""",
    )

    config = models.ForeignKey(
        "DeviceConfig",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="used_in_modules",
        limit_choices_to={"config_type": "module"},
        verbose_name="Configuration",
        help_text="Leave blank unless this is a new module or pack with a certain configuration",  # noqa: E501
    )

    spec_file = models.FileField(
        upload_to="uploaded_files",
        null=True,
        blank=True,
        validators=(validate_pdf_file,),
        verbose_name="Specification sheet",
        help_text="PDF version of spec. sheet for this type of device",
    )

    def clean(self):
        if self.abstract and self.device_type is not None:
            raise ValidationError("Abstract specifications cannot have a device type")
        return super().clean()

    def get_absolute_url(self):
        return reverse("battDB:Device", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Device Specifications"


class DeviceParameter(cm.HasName):
    """Parameters on device."""

    spec = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE)
    parameter = models.ForeignKey(
        dfn.Parameter,
        on_delete=models.CASCADE,
        limit_choices_to={"parameter_type": "device"},
    )
    value = models.JSONField(default=float)
    inherit_to_children = models.BooleanField(default=False)

    @property
    def user_owner(self):
        return self.spec.user_owner

    @property
    def status(self):
        return self.spec.status

    def __str__(self):
        return str(self.parameter)

    class Meta:
        unique_together = [("spec", "parameter"), ("spec", "name")]


class DeviceComponent(cm.HasName):
    """Components of a device."""

    spec = models.ForeignKey(DeviceSpecification, on_delete=models.CASCADE)
    component = models.ForeignKey(dfn.Component, on_delete=models.CASCADE)
    inherit_to_children = models.BooleanField(default=False)

    @property
    def user_owner(self):
        return self.spec.user_owner

    @property
    def status(self):
        return self.spec.status

    def __str__(self):
        return str(self.component)

    class Meta:
        unique_together = [("spec", "component"), ("spec", "name")]


class Batch(cm.BaseModelNoName, cm.HasMPTT):
    """A physical batch of devices produced to a given specification."""

    specification = models.ForeignKey(
        DeviceSpecification,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        limit_choices_to={"abstract": False},
        help_text="Type of device in this batch",
    )
    manufacturer = models.ForeignKey(
        cm.Org,
        default=1,
        on_delete=models.SET_DEFAULT,
        null=True,
        limit_choices_to={"is_mfg_cells": True},
    )
    serialNo = models.CharField(
        max_length=60,
        blank=True,
        unique=True,
        help_text="Batch number or some other unique identifier",
    )
    batch_size = models.PositiveSmallIntegerField(default=1)
    manufacturing_protocol = models.ForeignKey(
        dfn.Method,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"type": dfn.Method.METHOD_TYPE_MANUFACTURE},
        help_text="Test protocol used in this experiment",
    )
    manufactured_on = models.DateField(default=datetime.now)

    def __str__(self):
        return "%s %s (%d of) %s" % (
            self.manufacturer,
            self.specification,
            self.batch_size,
            self.manufactured_on,
        )

    def get_absolute_url(self):
        return reverse("battDB:Batch", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"


class Device(cm.HasAttributes, cm.HasNotes):
    """Identify an individual device in a batch."""

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    seq_num = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        help_text="Sequence number within batch",
    )

    def get_used_in_exps(self):
        """Provide the experiments in which the device is used."""
        return ExperimentDevice.objects.filter(
            batch=self.batch, batch_sequence=self.seq_num
        )

    def last_measured_state_of_health(self):
        """Provide the last time the state of health of the device was checked."""
        return self.attributes.get("state_of_health") or "Not tested"

    def used_in(self):
        """String indicating the number of experiments the device is used."""
        return "%d Experiments" % self.get_used_in_exps().count()

    def serial(self):
        """Provide the serial number for the device, including batch serial."""
        try:
            return self.batch.serialNo % self.seq_num
        except TypeError:
            return self.batch.serialNo + "/" + str(self.seq_num)

    class Meta:
        unique_together = ["batch", "seq_num"]

    def clean(self):
        if self.seq_num > self.batch.batch_size:
            raise ValidationError("Batch sequence ID cannot exceed batch size!")

        # TODO: Can compute device stats here
        self.attributes["state_of_health"] = "100%"

    @property
    def user_owner(self):
        return self.batch.user_owner

    @property
    def status(self):
        return self.batch.status

    def __str__(self):
        return str(self.batch.specification) + "/" + self.serial()


class DeviceConfig(cm.BaseModel):
    """A configuration of device templates.

    These represent how devices are connected in a module, pack, or experimental
    set-up."""

    TYPE_CHOICES = (
        ("module", "Module"),
        ("expmt", "Experiment"),
    )
    devices = models.ManyToManyField(DeviceSpecification, through="DeviceConfigNode")
    config_type = models.CharField(
        max_length=10, default="module", choices=TYPE_CHOICES
    )

    class Meta:
        verbose_name_plural = "Device Configurations"


class DeviceConfigNode(models.Model):
    """Defines a chain of devices electrically connected together, like a netlist.

    FIXME: I would like to use 'limit_choices_to to' dynamically restrict choices based
        on 'config',to ensure that all nodes in chain are part of the same config & net,
        i.e. you cannot link to a node in a different config.
        But it's a limitation of django that limit_choices_to cannot apply dynamically
        limit_choices_to={'config':config} would result in an error.
        Maybe there is a flaw in my database design here? This might not need
        to be a ManyToMany 'through' table.
    """

    device = models.ForeignKey(
        DeviceSpecification,
        on_delete=models.CASCADE,
        limit_choices_to={"abstract": True},
        help_text="Related device specification e.g. cell or sensor.",
    )
    config = models.ForeignKey(
        DeviceConfig,
        on_delete=models.CASCADE,
        help_text="Config instance to which this node belongs",
    )
    device_position_id = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Position of device in pack e.g. 1 - identifies this device",
    )
    pos_netname = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Name of electrical signal at positive terminal e.g. cell_1_v",
    )
    neg_netname = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Name of electrical signal at negative terminal e.g. pack_-ve",
    )

    @property
    def user_owner(self):
        return self.device.user_owner

    @property
    def status(self):
        return self.device.status

    def __str__(self):
        return (
            str(self.config)
            + "/"
            + str(self.device)
            + "_"
            + str(self.device_position_id)
        )


class Parser(cm.BaseModelMandatoryName):
    """Parsers for experimental device data.

    <BR>
    TODO: In future, these could be user-defined in Python code via this interface
        (with appropriate permissions) <BR> This would require all parsing to be done
        in a sandboxed environment on a separate server (which it should anyway)

    TODO: Maybe not. It should be possible to define any format by providing a
     template specifying the contents of the file. Something along the lines of:
     https://stackoverflow.com/q/46430471/3778792 combined with some pandas magic.
    """

    FORMAT_CHOICES = available_parsing_engines()
    file_format = models.CharField(
        max_length=100,
        default=FORMAT_CHOICES[0] if len(FORMAT_CHOICES) > 0 else "none",
        choices=FORMAT_CHOICES,
        help_text="File format",
    )
    parameters = models.ManyToManyField(dfn.Parameter, through="SignalType")

    def get_absolute_url(self):
        return reverse("battDB:Parser", kwargs={"pk": self.pk})

    def get_number_parameters(self):
        return self.columns.count()


class Equipment(cm.BaseModelMandatoryName):
    """Definitions of equipment such as cycler machines."""

    institution = models.ForeignKey(
        cm.Org, default=1, on_delete=models.SET_DEFAULT, null=True
    )
    serialNo = models.CharField(
        max_length=60,
        default="",
        blank=True,
        help_text="Serial number, if any, for this piece of equipment",
    )
    default_parser = models.ForeignKey(
        Parser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Default parser for this equipment's data",
    )

    def get_absolute_url(self):
        return reverse("battDB:Equipment", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Equipment"


class Experiment(cm.BaseModel):
    """Main "Experiment" aka DataSet class.

    <br> Has many: data files (from cyclers) <br> Has many: devices (actual physical
    objects e.g. cells) <br>

    TODO: This is incomplete. What is this meant to do?
    """

    TYPE_CHOICES = (
        ("constant", "Constant current"),
        ("gitt", "GITT"),
        ("hpcc", "HPCC"),
        ("drivecycle", "Drivecycle"),
        ("other", "Other"),
    )

    THERMAL_CHOICES = (
        ("no", "No thermal management"),
        ("chamber", "Thermal chamber"),
        ("base", "Base cooled"),
        ("surface", "Surface cooled"),
        ("tab", "Tab cooled"),
        ("other", "Other"),
    )

    name = models.CharField(
        max_length=128,
        blank=False,
        default="",
        null=False,
    )

    date = models.DateField(default=datetime.now)

    config = models.ForeignKey(
        DeviceConfig,
        on_delete=models.CASCADE,
        default=1,
        related_name="used_in",
        limit_choices_to={"config_type": "expmt"},
        help_text="All devices in the same experiment must be of the same "
        "configuration, i.e. an experiment must use all single cells, "
        "or all 2s2p modules, not a mixture of both.",
    )

    temperature = models.FloatField(
        blank=True,
        null=True,
        help_text="Experiment temperature in degrees Celcius.",
    )

    c_rate = models.FloatField(
        blank=True,
        null=True,
        help_text="C-rate for this experiment.",
        verbose_name="C-rate",
    )

    exp_type = models.CharField(
        verbose_name="Experiment type",
        max_length=50,
        choices=TYPE_CHOICES,
        default="constant",
        help_text="Type of experiment carried out. If 'other', "
        "experiment type should be specified in the experiment summary.",
    )

    thermal = models.CharField(
        verbose_name="Thermal management",
        max_length=50,
        choices=THERMAL_CHOICES,
        default="no",
        help_text="Thermal management technique used in this experiment. "
        " If 'other', technique should be specified in the experiment summary.",
    )

    external_link = models.URLField(
        blank=True,
        null=True,
        help_text="Specific link to a reference for this experiment.",
    )

    summary = models.TextField(
        help_text="Summary of what was done in the experiment e.g. what was the "
        "motivation, etc.",
        validators=[MinLengthValidator(20)],
    )

    def devices_(self):
        return self.devices.count()

    def files_(self):
        return self.data_files.count()

    def viewable_files_(self):
        return self.data_files.filter(~Q(status="deleted")).count()

    def cycles_(self):
        # TODO: Count total number of cycles
        return "?"

    def __str__(self):
        return str(self.user_owner) + " " + str(self.name) + " " + str(self.date)

    def get_absolute_url(self):
        return reverse("battDB:Experiment", kwargs={"pk": self.pk})

    def clean(self):
        """Validate that the name for an experiment is unique per institution.

        Args:
            name: The name attempting to be saved.

        Raises:
            ValidationError: _description_
        """
        instances = Experiment.objects.filter(
            name=self.name,
            user_owner__institution=self.user_owner.institution,
        )
        if len(instances) > 0 and instances[0] != self:
            raise ValidationError(
                f"Name '{self.name}' is already used in your institution"
            )


class ExperimentDataFile(cm.BaseModel):
    """EDF is the class tying together data files, parsed data tables and experiments.

    <>BR> It contains all of the time-series  (ts) numerical data as a Postgres
    ArrayField(ArrayField(FloatField))) <br> Text data should be added as Events. Raw
    data files should be uploaded and referenced, where available.
    """

    ts_headers = ArrayField(
        models.CharField(max_length=32),
        blank=True,
        null=True,
        editable=False,
        help_text="Parsed data column headers",
    )
    ts_data = ArrayField(
        ArrayField(models.FloatField()),
        blank=True,
        null=True,
        editable=False,
        help_text="Parsed time-series data columns (note: this is bulky data!)",
    )
    experiment = models.ForeignKey(
        Experiment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="data_files",
    )

    devices = models.ManyToManyField(Device, related_name="data_files")

    machine = models.ForeignKey(
        Equipment,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Equipment on which this data was recorded",
    )

    protocol = models.ForeignKey(
        dfn.Method,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"type": dfn.Method.METHOD_TYPE_EXPERIMENTAL},
        help_text="Test protocol used in this experiment",
    )

    time_recorded = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Time at which the experiment data was recoreded",
    )

    settings_file = models.FileField(
        upload_to="uploaded_files",
        null=True,
        blank=True,
        validators=(validate_settings_file,),
        verbose_name="Settings file",
        help_text="Input settings file for the cycler used to produce this data (if "
        "available)",
    )

    binary_file = models.FileField(
        upload_to="uploaded_files",
        null=True,
        blank=True,
        validators=(validate_binary_file,),
        verbose_name="Binary file",
        help_text="Binary file version of this data output by the cycler (if "
        "available)",
    )

    def num_cycles(self):
        return (
            self.ranges.filter(step_action="cycle").count()
            + self.ranges.filter(step_action=["chg", "dchg"]).count() / 2.0
        )

    def num_ranges(self):
        return self.ranges.count()

    def file_rows(self):
        return self.attributes.get("total_rows", 0)

    def parsed_ranges(self):
        return self.attributes.get("parsed_ranges", [])

    def parsed_columns(self):
        return self.attributes.get("parsed_columns", [])

    def missing_columns(self):
        return self.attributes.get("missing_columns", [])

    def file_columns(self):
        return self.attributes.get("file_columns", [])

    def is_parsed(self):
        return self.file_exists() and len(self.file_columns()) > 0

    def file_exists(self):
        if hasattr(self, "raw_data_file"):
            return self.raw_data_file.exists()
        return False

    def file_hash(self):
        if self.file_exists():
            return self.raw_data_file.hash

        return "N/A"

    def create_ranges(self):
        ranges = self.attributes.get("range_config", dict())
        for name, config in ranges.items():
            rng_q = DataRange.objects.get_or_create(
                dataFile=self, label=name, user_owner=self.user_owner
            )
            rng = rng_q[0]
            rng.file_offset_start = config.get("start") or 0
            rng.file_offset_end = config.get("end") or 0
            rng.protocol_step = config.get("step") or 0
            rng.step_action = config.get("action") or 0
            rng.save()

    def clean(self):
        if self.name is None or self.name == "" or self.name == "Unnamed data set":
            try:
                self.name = str(self.raw_data_file)
            except UploadedFile.DoesNotExist:
                self.name = "Unnamed data set"

        if self.file_exists() and self.raw_data_file.parse and not self.is_parsed():
            cols = [
                c.col_name
                for c in self.raw_data_file.use_parser.columns.all().order_by("order")
            ]
            file_obj = self.raw_data_file.file
            file_format = self.raw_data_file.use_parser.file_format
            parsed_file = parse_data_file(file_obj, file_format, columns=cols)

            self.attributes["parsed_metadata"] = parsed_file["metadata"]
            self.attributes["file_columns"] = parsed_file["file_columns"]
            self.attributes["parsed_columns"] = parsed_file["parsed_columns"]
            self.attributes["parsed_header_columns"] = parsed_file[
                "parsed_header_columns"
            ]
            self.attributes["missing_columns"] = parsed_file["missing_columns"]
            self.attributes["total_rows"] = parsed_file["total_rows"]
            self.attributes["range_config"] = parsed_file["range_config"]
            self.ts_headers = self.parsed_columns()
            self.ts_data = parsed_file["data"]

    def save(self):
        super().save()

        if self.is_parsed():
            self.create_ranges()

    class Meta:
        verbose_name = "Data File"


class UploadedFile(cm.HashedFile, cm.HasOwner, cm.HasStatus):  # type: ignore
    edf = models.OneToOneField(
        ExperimentDataFile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="raw_data_file",
    )
    local_path = models.CharField(max_length=1024, default="", blank=True)
    local_date = models.DateTimeField(default=datetime.now)
    parse = models.BooleanField(
        default=False, help_text="Set to True to import data on save"
    )
    use_parser = models.ForeignKey(
        Parser, null=True, blank=True, on_delete=models.SET_NULL
    )
    parsed_metadata = models.JSONField(
        editable=False,
        default=dict,
        help_text="metadata automatically extracted from the file",
    )


class ExperimentDevice(models.Model):
    """Join table: identifies devices in experiments and link them to data files."""

    experiment = models.ForeignKey(
        Experiment, on_delete=models.CASCADE, related_name="devices"
    )
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    batch_sequence = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
        ],
        help_text="sequence number of device within batch",
    )
    device_position = models.CharField(
        max_length=20,
        default="cell_01",
        help_text="Device Position ID in Experiment Config - e.g. Cell_A1 for the "
        "first cell of a series-parallel pack (leave as cell_01 for single cell experiments)",  # noqa E501
    )

    def get_serial_no(self):
        """TODO: implement id_to_serialno and serialno_to_id functions."""
        # TEMP fix to allow Experiments to be created without errors
        pass
        # raise NotImplementedError

    def clean(self):
        if hasattr(self, "batch"):
            if self.batch is not None and self.batch_sequence > self.batch.batch_size:
                raise ValidationError("Batch sequence ID cannot exceed batch size!")
            elif self.batch is not None:
                Device.objects.get_or_create(
                    batch=self.batch, seq_num=self.batch_sequence
                )

    @property
    def user_owner(self):
        return self.experiment.user_owner

    @property
    def status(self):
        return self.experiment.status

    def __str__(self):
        return self.device_position


class DataColumn(models.Model):
    """A way of adding columns to datafiles

    TODO: This is not implemented properly yet (see below) so is not made available
    in any view or in the admin site.

    """

    data_file = models.ForeignKey(ExperimentDataFile, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=40, default="Ns")

    RESAMPLE_CHOICES = (
        ("none", "Do not resample"),
        ("on_change", "Sample on change"),
        ("decimate", "Take every Nth sample"),
        ("average", "Average every Nth sample"),
        ("max", "Maximum every Nth sample"),
        ("min", "Minimum every Nth sample"),
    )
    resample = models.CharField(
        max_length=10,
        choices=RESAMPLE_CHOICES,
        default="none",
        help_text="Resampling option - TO BE IMPLEMENTED - currently has no effect",
    )
    resample_n = models.PositiveSmallIntegerField(
        default=1,
        validators=(MinValueValidator(1),),
        help_text="Resampling divisor - TO BE IMPLEMENTED",
    )

    parameter = models.ForeignKey(
        dfn.Parameter,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        help_text="Map this column to a parameter on a device",
    )
    device = models.ForeignKey(
        ExperimentDevice,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Device id for parameter mapping",
    )

    def clean(self):
        if (
            self.device is not None
            and self.device.experiment != self.data_file.experiment
        ):
            raise ValidationError(
                "Cannot use device instance from a different experiment"
            )
        if self.device is None:
            self.parameter = None
        if self.resample == "none" or self.resample == "on_change":
            self.resample_n = 1

    def experiment(self):
        return self.data_file.experiment

    @property
    def user_owner(self):
        return self.data_file.user_owner

    @property
    def status(self):
        return self.data_file.status

    class Meta:
        unique_together = [["device", "data_file"], ["column_name", "data_file"]]
        verbose_name = "Column Mapping"
        verbose_name_plural = "Data Column Mappings to Device Parameters"


class DataRange(
    cm.HasAttributes, cm.HasNotes, cm.HasCreatedModifiedDates, cm.HasOwner, cm.HasStatus
):
    """Each data range within the data file

    Each data file contains numerous ranges e.g. charge & discharge cycles. Their data
    might overlap. <br>
    Currently this model is used in ExperimentDataFile.create_ranges but creating just
    one range for the whole file according to parer_engines_base.parse_data_file
    range_config, which is fixed.
    TODO: Write (or find) code to segment data into ranges. <br>
    TODO: Convert this into a JSON Schema within ExperimentData. <br>
    TODO: Re-implement inlineform in admin for this model.
    """

    dataFile = models.ForeignKey(
        ExperimentDataFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ranges",
    )
    file_offset_start = models.PositiveIntegerField(default=0)
    file_offset_end = models.PositiveIntegerField(default=0)
    label = models.CharField(max_length=32, default="all")
    protocol_step = models.PositiveSmallIntegerField(default=0)
    step_action = models.CharField(
        max_length=8,
        choices=[
            ("chg", "Charging"),
            ("dchg", "Discharging"),
            ("cycle", "Full cycle"),
            ("rest", "Rest"),
            ("all", "Entire series"),
            ("user", "User defined"),
        ],
        default="all",
    )

    def __str__(self):
        return "%s/%d: %s" % (self.dataFile or "None", self.id or 0, self.label or "")

    class Meta:
        verbose_name_plural = "Data Ranges"
        unique_together = [["dataFile", "label"]]


class SignalType(models.Model):
    """Specification for a column in a data file representing a physical quantity."""

    parameter = models.ForeignKey(
        dfn.Parameter,
        on_delete=models.CASCADE,
        limit_choices_to={"parameter_type": "experiment"},
    )
    col_name = models.CharField(max_length=50, default="")
    order = models.PositiveSmallIntegerField(
        default=5, help_text="override column ordering"
    )
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE, related_name="columns")

    @property
    def user_owner(self):
        return self.parser.user_owner

    @property
    def status(self):
        return self.parser.status

    def __str__(self):
        return self.col_name

    class Meta:
        pass
