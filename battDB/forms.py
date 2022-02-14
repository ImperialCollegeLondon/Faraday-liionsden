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
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from battDB.models import (
    Batch,
    DeviceParameter,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    ExperimentDevice,
    UploadedFile,
)
from common.forms import DataCreateForm
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
            "abstract",
            "device_type",
            "parent",
            "config",
            "spec_file",
            "notes",
            "parameters",
        ]
        help_texts = {
            "abstract": 'This is a new device type e.g. "Cell".',
            "device_type": "Must select if not specifying a new device type.",
            "parent": "Select parent device if appropriate.",
        }

    def __init__(self, *args, **kwargs):
        super(NewDeviceForm, self).__init__(*args, **kwargs)
        self.fields["parameters"].required = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h1> New Device </h1>")),
            Div(
                Column("name", css_class="col-6"),
                Column("abstract", css_class="col-6"),
                Column("device_type", css_class="col-6"),
                Column("parent", css_class="col-6"),
                Column("config", css_class="col-6"),
                Column("spec_file", css_class="col-6"),
                HTML("<hr>"),
                Fieldset(
                    "Define parameters",
                    Div(
                        HTML(
                            "Specify any device parameters below such as cathode thickness."
                        ),
                        css_class="container pb-4",
                    ),
                    Formset("parameters"),
                ),
                HTML("<hr>"),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                css_class="row align-items-end",
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
        "material",
    ],
    extra=1,
    can_delete=True,
    help_texts={
        "parameter": "e.g. Form factor, cathode thickness...",
        "value": None,
        "material": "If this parameter pertains to a specific material, otherwise leave blank.",
    },
    widgets={"value": forms.TextInput()},
)


class NewExperimentForm(DataCreateForm):
    """
    Create new experiment.
    """

    class Meta:
        model = Experiment
        fields = ["name", "date", "config", "notes"]
        help_texts = {
            "config": "All devices must be of the same config, e.g. Single cell."
        }

    def __init__(self, *args, **kwargs):
        super(NewExperimentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(HTML("<h1> New Experiment </h1>")),
            Div(
                Column("name", css_class="col-6"),
                Column("date", css_class="col-6"),
                Column("config", css_class="col-6"),
                Fieldset("Add devices", Formset("devices"), required=False),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
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


ExperimentDeviceFormSet = inlineformset_factory(
    Experiment,
    ExperimentDevice,
    form=ExperimentDeviceForm,
    fields=["batch", "batch_sequence", "device_position"],
    extra=1,
    can_delete=True,
    help_texts={
        "batch_sequence": None,
        "device_position": None,
    },
)


class NewEquipmentForm(DataCreateForm):
    """
    Create new equipment.
    """

    class Meta:
        model = Equipment
        fields = ["name", "institution", "serialNo", "default_parser", "notes"]

    def __init__(self, *args, **kwargs):
        super(NewEquipmentForm, self).__init__(*args, **kwargs)
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

    def __init__(self, *args, **kwargs):
        super(NewBatchForm, self).__init__(*args, **kwargs)
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
                css_class="row",
            )
        )


class NewExperimentDataFileForm(DataCreateForm):
    """
    Add a new experiment data file.
    """

    class Meta:
        model = ExperimentDataFile
        fields = [
            "name",
            "machine",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        super(NewExperimentDataFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"enctype": "multipart/form-data"}
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> New data file </h1>")),
                Column("name", css_class="col-6"),
                Column("machine", css_class="col-6"),
                Fieldset(
                    "Upload file",
                    Div(
                        HTML(
                            "Upload the raw data file here. Select 'parse' to process the data using your chosen parser. "
                        ),
                        HTML(
                            "<b>Find detailed information about the behaviour of each parser <a href='/battDB/parsers/'  target='_blank'>here</a></b>."
                        ),
                        css_class="container pb-4",
                    ),
                    Formset("raw_data_file"),
                    required=False,
                ),
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
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
)


class NewProtocolForm(DataCreateForm):
    """
    Create new experimental or manufacturing protocol.
    """

    # TODO enable addition of extra array elements dynamically (widget currently doesn't work).
    class Meta:
        model = Method
        fields = [
            "name",
            "type",
            "description",
            "notes",
        ]
