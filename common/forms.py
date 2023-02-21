from django import forms
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet


class ModifiedFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(ModifiedFormSet, self).__init__(*args, **kwargs)


class DataCreateForm(ModelForm):
    """
    Generic form for creating new data. Includes option to make public or
    private.
    """

    make_public = forms.BooleanField(
        required=False, help_text="You cannot change this entry once it is public."
    )

    def is_public(self):
        return self.data.get("make_public", False)
