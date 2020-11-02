from django import forms
from .models import *
from common.models import UploadedFile
from django.contrib.admin.widgets import AdminDateWidget, FilteredSelectMultiple, AutocompleteSelectMultiple
from django.forms import Textarea, TextInput

# from jsoneditor.forms import JSONEditor

# $Id: ReadOnlyWidget.py 487 2009-08-12 09:01:09Z tguettler $
# $HeadURL: svn+ssh://svnserver/svn/djangotools/trunk/widgets/ReadOnlyWidget.py $

# This is http://www.djangosnippets.org/snippets/1682/
# based on http://www.djangosnippets.org/snippets/937/

# from django import forms
# from django.db import models
#
# empty_magic = object()
#
#
# class ReadOnlyWidget(forms.Widget):
#     u'''
#     Usage1: foo_field.widget=ReadOnlyWidget(mystring)
#     Usage2: ReadOnlyWidget(myint, my_display_string)
#     Usage3: ReadOnylWidget(form=myform, field_name='foo')
#     '''
#
#     def __init__(self, original_value=empty_magic, display_value=None, form=None, name=None):
#         if original_value is empty_magic:
#             assert form and name
#             field = form.fields[name]
#             original_value = form.initial.get(name, field.initial)
#             if callable(original_value):
#                 original_value = original_value()
#             if isinstance(field, forms.ChoiceField):
#                 for v, display in field.choices:
#                     if v == original_value:
#                         display_value = display
#                         break
#         else:
#             assert not (form or name)
#         if display_value is None:
#             if original_value is None:
#                 display_value = u''
#             else:
#                 display_value = original_value
#         if isinstance(original_value, models.Model):
#             original_value = original_value.pk
#         self.original_value = original_value
#         self.display_value = display_value
#
#         super(ReadOnlyWidget, self).__init__()
#
#     def render(self, name, value, attrs=None):
#         if self.display_value is not None:
#             if not isinstance(self.display_value, str):
#                 return str(self.display_value)
#             return self.display_value
#         return str(self.original_value)
#
#     def value_from_datadict(self, data, files, name):
#         return self.original_value
#

# forms.widgets.SelectMultiple
# class DataFileForm(forms.ModelForm):
#     # class Meta:
#     #     widgets = {
#     #         'parsed_data': ReadOnlyWidget,
#     #     }
#     parsed_data = forms.CharField(widget=TextInput(attrs={'readonly':'readonly'}))
#
#     # def __init__(self,*args,**kwargs):
#     #     self.base_fields['files'].queryset = UploadedFile.objects.filter(used_by=None)
#     #     super().__init__(self, *args, **kwargs)
#
#     # class Meta:
#     #     model = Experiment
#     #     exclude = ['raw_data_file']
