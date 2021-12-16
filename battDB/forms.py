import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
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


class NewDeviceForm(DataCreateForm):
    """
    Create a new type of device (device specification).
    """

    # TODO Allow upload of child devices in the same form.
    # See https://shouts.dev/add-or-remove-input-fields-dynamically-using-jquery
    class Meta:
        model = DeviceSpecification
        fields = ["name", "device_type", "config", "abstract", "notes", "parent"]
        help_texts = {
            "abstract": 'This is a new device type e.g. "Cell".',
            "device_type": "Must select if not specifying a new device type.",
            "parent": "Select parent device if appropriate.",
        }


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
    Create new experimental or manufacturing protocol.
    """

    # TODO enable addition of extra array elements dynamically (widget currently doesn't work).
    class Meta:
        model = Experiment
        exclude = ["user_owner"]

    def __init__(self, *args, **kwargs):
        super(NewExperimentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Div(
                Field("name"),
                Field("date"),
                Field("config"),
                Fieldset("Add devices", Formset("devices")),
                Field("notes"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
            )
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
)
