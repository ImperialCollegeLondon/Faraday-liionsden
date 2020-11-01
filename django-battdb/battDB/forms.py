from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget, FilteredSelectMultiple
# from jsoneditor.forms import JSONEditor


class ExperimentForm(forms.ModelForm):
   data_files = forms.ModelMultipleChoiceField(widget=FilteredSelectMultiple(verbose_name="Data files", is_stacked=False),
                                               queryset = ExperimentDataFile.objects.all())
   class Meta:
       model = Experiment
       exclude = []


