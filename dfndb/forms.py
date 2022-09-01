from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Column,
    Div,
    Field,
    Fieldset,
    Layout,
    Submit,
)
from django.forms import ModelForm, inlineformset_factory
from django.utils.safestring import mark_safe

from battDB.custom_layout_object import Formset
from common.forms import DataCreateForm
from dfndb.models import Component, CompositionPart, Compound


class NewCompoundForm(DataCreateForm):
    """
    Create a new compound.
    """

    class Meta:
        model = Compound
        fields = ["name", "formula", "mass"]
        help_texts = {
            "formula": "Chemical formula. This will be used to calculate the mass.",
            "mass": (
                "Only fill in if the formula should not be used to automatically "
                " calculate the mass. Otherwise, leave as 0."
            ),
        }

    def __init__(self, *args, **kwargs):
        super(NewCompoundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> Compound </h1>")),
                Div(
                    HTML(
                        """
                        Compounds should be specified in their discharged state
                        (if relevant) and are always public (visible to all users).
                        """
                    ),
                    css_class="container py-2",
                ),
                Column("name", css_class="col-4"),
                Column("formula", css_class="col-4"),
                Column("mass", css_class="col-4"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            )
        )


class NewComponentForm(DataCreateForm):
    """
    Create a new component.
    """

    class Meta:
        model = Component
        fields = ["name", "type", "polymer", "notes"]

    def __init__(self, *args, **kwargs):
        super(NewComponentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> Component </h1>")),
                Column("name", css_class="col-4"),
                Column("type", css_class="col-4"),
                Column("polymer", css_class="col-4"),
                Fieldset(
                    "Composition",
                    Div(
                        HTML(
                            "Optionally specify the amount of each compound in this "
                            "component. Amounts are relative and unitless."
                        )
                    ),
                    Formset("composition"),
                ),
                HTML("<br>"),
                Field("make_public"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", "save")),
                HTML("<br>"),
                HTML("<br>"),
                ButtonHolder(Submit("another", "save and add another")),
                css_class="row",
            )
        )


class CompositionPartForm(ModelForm):
    """
    For adding compounds to components.
    """

    class meta:
        model = CompositionPart
        exclude = ()


CompositionPartFormSet = inlineformset_factory(
    Component,
    CompositionPart,
    form=CompositionPartForm,
    fields=["compound", "amount"],
    extra=1,
    can_delete=True,
    help_texts={
        "compound": mark_safe(
            '<a href="/dfndb/new_compound/" target="_blank"> '
            "new compound &#10697;</a>"
        )
    },
)
