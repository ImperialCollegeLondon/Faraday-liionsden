from django import forms
from django.forms import ModelForm

from battDB.models import DeviceSpecification


class NewDeviceForm(ModelForm):
    class Meta:
        model = DeviceSpecification
        fields = ["name", "device_type", "config"]

    def save(self, commit=True):
        device = super(NewDeviceForm, self).save(commit=False)
        if commit:
            device.save()
        return device
