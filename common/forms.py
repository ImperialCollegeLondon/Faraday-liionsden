from django import forms
from django.forms import ModelForm


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
