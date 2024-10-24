import operator
from functools import reduce

from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Column,
    Div,
    Field,
    Fieldset,
    Layout,
    Submit,
)
from django import forms
from django.db.models import Q
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.utils.safestring import mark_safe
from guardian.shortcuts import get_objects_for_user

from battDB.models import (
    Batch,
    Device,
    DeviceComponent,
    DeviceParameter,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    ExperimentDevice,
    UploadedFile,
)
from common.forms import DataCreateForm, FormSetWithUser
from dfndb.models import Method

from .custom_layout_object import Formset


class NewDeviceForm(DataCreateForm):
    """
    Create a new type of device (device specification).
    """

    class Meta:
        model = DeviceSpecification
        fields = [
            "name",
            "device_type",
            "parent",
            "config",
            "spec_file",
            "notes",
            "parameters",
            "components",
        ]
        help_texts = {
            "device_type": "Is  this a cell or a module?",
            "parent": (
                "Leave blank unless this cell is a part of "
                "a particular module or pack"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parameters"].required = False
        self.fields["components"].required = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h1> New Device </h1>")),
            Div(
                Column("name", css_class="col-4"),
                Column("device_type", css_class="col-4"),
                Column("spec_file", css_class="col-4"),
                Column("parent", css_class="col-4"),
                Column("config", css_class="col-4"),
                Field("notes"),
                Div(
                    Fieldset(
                        "Parameters",
                        HTML("Optionally specify the parameters of this device"),
                        Formset("parameters"),
                    ),
                    css_class="card bg-light mb-3",
                ),
                Div(
                    Fieldset(
                        "Components",
                        HTML("Optionally specify the components of this device"),
                        Formset("components"),
                    ),
                    css_class="card bg-light mb-3",
                ),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row align-items-top",
            ),
        )


class DeviceParameterForm(ModelForm):
    """
    For adding parameters to devices inline.
    """

    class meta:
        model = DeviceParameter
        exclude = ()


DeviceParameterFormSet = inlineformset_factory(
    DeviceSpecification,
    DeviceParameter,
    form=DeviceParameterForm,
    fields=[
        "parameter",
        "value",
    ],
    extra=1,
    can_delete=True,
    help_texts={
        "parameter": "e.g. Form factor, cathode size, number of layers...",
        "value": None,
    },
    widgets={"value": forms.TextInput()},
)


class DeviceComponentForm(ModelForm):
    """
    For adding components to devices inline.
    """

    class meta:
        model = DeviceComponent
        exclude = ()


DeviceComponentFormSet = inlineformset_factory(
    DeviceSpecification,
    DeviceComponent,
    form=DeviceComponentForm,
    fields=["component"],
    extra=1,
    can_delete=True,
    help_texts={
        "component": mark_safe(
            "e.g. Anode, cathode, Electrolyte... "
            '<a href="/dfndb/new_component/" target="_blank"> '
            "new component &#10697;</a>"
        )
    },
)


class NewExperimentForm(DataCreateForm):
    """
    Create new experiment.
    """

    class Meta:
        model = Experiment
        fields = [
            "name",
            "date",
            "config",
            "temperature",
            "c_rate",
            "exp_type",
            "thermal",
            "notes",
            "external_link",
            "summary",
        ]
        help_texts = {
            "date": "When this experiment started",
            "config": "All devices must be of the same config, e.g. Single cell",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h1> New Experiment </h1>")),
            Div(
                Column("name", css_class="col-3"),
                Column("date", css_class="col-3"),
                Column("config", css_class="col-3"),
                Column("temperature", css_class="col-3"),
                Column("exp_type", css_class="col-3"),
                Column("c_rate", css_class="col-3"),
                Column("thermal", css_class="col-3"),
                Column("external_link", css_class="col-3"),
                Field("summary"),
                Field("notes"),
                Div(
                    Fieldset(
                        "Devices",
                        HTML(
                            "Optionally specify the device(s) used in this experiment"
                        ),
                        Formset(
                            "devices",
                        ),
                        required=False,
                    ),
                    css_class="card bg-light mb-3",
                ),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            ),
        )


class ExperimentDeviceForm(ModelForm):
    """
    For adding devices to experiments inline.
    """

    class meta:
        model = ExperimentDevice
        exclude = ()


ExperimentDeviceFormSetBase = inlineformset_factory(
    Experiment,
    ExperimentDevice,
    form=ExperimentDeviceForm,
    formset=FormSetWithUser,
    fields=["batch", "batch_sequence", "device_position"],
    extra=1,
    can_delete=True,
    help_texts={
        "batch": mark_safe(
            "The batch this device came from. "
            '<a href="/battDB/new_batch/" target="_blank"> '
            "new batch &#10697;</a>"
        )
    },
)


class ExperimentDeviceFormSet(ExperimentDeviceFormSetBase):  # type: ignore
    """
    modify ExperimentDeviceFormset to limit batch field to those the user has access to.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.user:
            # Get queryset of batches
            restricted_batches = get_objects_for_user(self.user, "view_batch", Batch)
            # Limit batch field to batches the user has access to
            self.form.base_fields["batch"].queryset = restricted_batches


class NewEquipmentForm(DataCreateForm):
    """
    Create new equipment.
    """

    class Meta:
        model = Equipment
        fields = ["name", "institution", "serialNo", "default_parser", "notes"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> New Equipment </h1>")),
                Column("name", css_class="col-6"),
                Column("institution", css_class="col-6"),
                Column("serialNo", css_class="col-6"),
                Column("default_parser", css_class="col-6"),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            )
        )


class NewBatchForm(DataCreateForm):
    """
    Create new Batch of devices.
    """

    # TODO enable preview of batch of devices before commiting to save.
    class Meta:
        model = Batch
        fields = [
            "manufacturer",
            "manufactured_on",
            "specification",
            "batch_size",
            "serialNo",
            "notes",
        ]
        help_texts = {
            "specification": mark_safe(
                'Type of device in this batch. <a href="/battDB/new_device/" '
                'target="_blank">new device spec. &#10697;</a>.'
            )
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.user:
            # Get queryset of device specifications the user has permission to view
            restricted_specs = get_objects_for_user(
                self.user, "view_devicespecification", DeviceSpecification
            )
            restricted_specs = restricted_specs.filter(abstract=False)
            self.fields["specification"].queryset = restricted_specs
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> New Batch </h1>")),
                Column("manufactured_on", css_class="col-6"),
                Column("manufacturer", css_class="col-6"),
                Column("batch_size", css_class="col-3"),
                Column("serialNo", css_class="col-3"),
                Column("specification", css_class="col-6"),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            )
        )


class NewExperimentDataFileForm(DataCreateForm):
    """
    Add a new experiment data file.
    """

    devices = forms.ModelMultipleChoiceField(
        queryset=Device.objects.get_queryset(),
    )

    time_recorded = forms.DateTimeField(widget=DateTimePickerInput(), required=False)

    class Meta:
        model = ExperimentDataFile
        fields = [
            "name",
            "machine",
            "notes",
            "settings_file",
            "binary_file",
            "devices",
            "time_recorded",
        ]
        help_texts = {
            "name": mark_safe("If left blank, the file name will be used."),
            "machine": mark_safe(
                "The machine this data file was collected on. "
                '<a href="/battDB/new_equipment/" target="_blank"> '
                "new machine &#10697;</a>"
            ),
        }

    def __init__(self, *args, **kwargs):
        mode = "Update" if "instance" in kwargs.keys() else "New"
        self.experiment = kwargs.pop("experiment", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"enctype": "multipart/form-data"}

        # Get queryset of devices in the associated experiment
        if self.experiment:
            if self.experiment.devices.count() > 0:
                batch_ids = [dev.batch_id for dev in self.experiment.devices.all()]
                batch_seqs = [
                    dev.batch_sequence for dev in self.experiment.devices.all()
                ]
                # Each device needs to have the right batch_id, batch_seq combo
                query = reduce(
                    operator.or_,
                    (
                        Q(batch_id=bid, seq_num=seq)
                        for bid, seq in zip(batch_ids, batch_seqs)
                    ),
                )
                self.fields["devices"].queryset = Device.objects.filter(query)
            else:
                self.fields["devices"].queryset = Device.objects.none()
                self.fields["devices"].help_text = mark_safe(
                    """
                    <div class="alert alert-danger" role="alert">
                    No devices have been added to this experiment yet!
                    You must associate devices with the experiemnt before you can
                    add experimental data. Go back and edit the experiment to add
                    devices from an existing batch.
                    </div>
                    """
                )

        if mode == "New":
            fieldset = Fieldset(
                "Upload file",
                Div(
                    HTML(
                        "Upload the raw data file here. Select a parser to process "
                        "the data, or leave blank to upload the file without "
                        "parsing. "
                    ),
                    HTML(
                        "<b>Find detailed information about the behaviour of "
                        "each parser <a href='/battDB/parsers/'  target='_blank'>"
                        "here</a></b>."
                    ),
                    css_class="container pb-4",
                ),
                Formset("raw_data_file"),
                required=False,
            )
        else:
            fieldset = Fieldset(
                "Upload file",
                Div(
                    HTML(
                        "Note: You cannot change the file that has already been "
                        "uploaded, only its metadata. If you want to "
                        "change the file, delete this entry and upload a new one."
                    ),
                    css_class="container pb-4",
                ),
                required=False,
            )

        self.helper.layout = Layout(
            Div(
                Div(HTML(f"<h1> {mode} experiment data </h1>")),
                Column("name", css_class="col-6"),
                Column("machine", css_class="col-6"),
                Column("devices", css_class="col-6"),
                Column("time_recorded", css_class="col-6"),
                fieldset,
                Column("settings_file", css_class="col-6"),
                Column("binary_file", css_class="col-6"),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            )
        )


class UploadedFileForm(ModelForm):
    """
    For adding files.
    """

    class meta:
        model = UploadedFile
        exclude = ()


UploadDataFileFormset = inlineformset_factory(
    ExperimentDataFile,
    UploadedFile,
    form=UploadedFileForm,
    fields=["file", "use_parser"],
    extra=1,
    can_delete=False,
    help_texts={
        "file": None,
    },
    min_num=1,
    validate_min=True,
)


class NewProtocolForm(DataCreateForm):
    """
    Create new experimental or manufacturing protocol.
    """

    # TODO enable addition of extra array elements dynamically
    # (widget currently doesn't work).
    class Meta:
        model = Method
        fields = [
            "name",
            "type",
            "description",
            "notes",
        ]
