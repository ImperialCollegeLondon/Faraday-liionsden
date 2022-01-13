import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Column,
    Div,
    Field,
    Fieldset,
    Layout,
    Row,
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
    ExperimentDevice,
)
from dfndb.models import Method

from .custom_layout_object import Formset


class DataCreateForm(ModelForm):
    """
    Generic form for creating new data. Includes option to make public or
    private and will include option to only show allowed objects in dropdown
    for logged in user.
    """

    # TODO modify init to only populate dropdowns with entries the user has
    # the permissions to view. https://stackoverflow.com/q/51939175

    make_public = forms.BooleanField(
        required=False, help_text="You cannot change this entry once it is public!"
    )

    def is_public(self):
        return self.data.get("make_public", False)


class NewDeviceForm(ModelForm):
    """
    Create a new type of device (device specification).
    """

    # TODO Allow upload of child devices in the same form.
    # See https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery
    class Meta:
        model = DeviceSpecification
        exclude = ["status"]
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
            Div(
                Column("name", css_class="col-6"),
                Column("abstract", css_class="col-6"),
                Column("device_type", css_class="col-6"),
                Column("parent", css_class="col-6"),
                Column("config", css_class="col-6"),
                Column("spec_file", css_class="col-6"),
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
                Field("notes"),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                css_class="row",
            )
        )

    make_public = forms.BooleanField(
        required=False, help_text="You cannot change this entry once it is public!"
    )

    def is_public(self):
        return self.data.get("make_public", False)


class NewEquipmentForm(DataCreateForm):
    """
    Create new equipment.
    """

    class Meta:
        model = Equipment
        fields = ["name", "institution", "serialNo", "default_parser", "notes"]


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


class NewExperimentForm(ModelForm):
    """
    Create new experiment.
    """

    class Meta:
        model = Experiment
        exclude = ["status"]
        help_texts = {
            "config": "All devices must be of the same config, e.g. Single cell."
        }

    def __init__(self, *args, **kwargs):
        super(NewExperimentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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
            )
        )

    make_public = forms.BooleanField(
        required=False, help_text="You cannot change this entry once it is public!"
    )

    def is_public(self):
        return self.data.get("make_public", False)


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
)
