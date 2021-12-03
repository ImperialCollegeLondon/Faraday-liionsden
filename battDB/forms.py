from django import forms
from django.forms import ModelForm

from battDB.models import DeviceSpecification


class NewDeviceForm(ModelForm):
    class Meta:
        model = DeviceSpecification
        fields = ["name", "device_type", "config", "abstract", "notes", "parent"]
        help_texts = {
            "abstract": 'This is a new device type e.g. "Cell".',
            "device_type": "Must select if not specifying a new device type.",
            "parent": "Select parent device if appropriate.",
        }

    def save(self, commit=True):
        device = super(NewDeviceForm, self).save(commit=False)
        if commit:
            device.save()
        return device
