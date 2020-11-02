from django import forms
from .models import *
from common.models import UploadedFile
from django.contrib.admin.widgets import AdminDateWidget, FilteredSelectMultiple, AutocompleteSelectMultiple


# from jsoneditor.forms import JSONEditor

# forms.widgets.SelectMultiple
class DataFileForm(forms.ModelForm):
    files = forms.ModelChoiceField(
        widget=forms.Select(),
        queryset=UploadedFile.objects.filter(used_by=None))

    # def __init__(self,*args,**kwargs):
    #     self.base_fields['files'].queryset = UploadedFile.objects.filter(used_by=None)
    #     super().__init__(self, *args, **kwargs)

    class Meta:
        model = Experiment
        exclude = ['raw_data_file']
