from django import forms
from django.forms import ModelForm

from battDB.models import Batch, DeviceSpecification, Equipment


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
