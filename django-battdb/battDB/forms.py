from django import forms
from .models import Experiment
from django.contrib.admin.widgets import AdminDateWidget
from jsoneditor.forms import JSONEditor

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'date']
#       widgets = {'date':AdminDateWidget(), 'parameters':JSONEditor()}

