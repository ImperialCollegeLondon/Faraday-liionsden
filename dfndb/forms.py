from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Column,
    Div,
    Field,
    Fieldset,
    Layout,
    Row,
    Submit,
)
from django.forms import ModelForm, inlineformset_factory

from battDB.custom_layout_object import Formset
from common.forms import DataCreateForm
from dfndb.models import CompositionPart, Compound, Material


class NewCompoundForm(DataCreateForm):
    """
    Create a new compound.
    """

    class Meta:
        model = Compound
        fields = ["name", "formula", "mass"]

    def __init__(self, *args, **kwargs):
        super(NewCompoundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> Compound </h1>")),
                Column("name", css_class="col-4"),
                Column("formula", css_class="col-4"),
                Column("mass", css_class="col-4"),
                ButtonHolder(Submit("submit", "save")),
                css_class="row",
            )
        )


class NewMaterialForm(DataCreateForm):
    """
    Create a new material.
    """

    class Meta:
        model = Material
        fields = ["name", "type", "polymer", "notes"]

    def __init__(self, *args, **kwargs):
        super(NewMaterialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(HTML("<h1> Material </h1>")),
                Column("name", css_class="col-4"),
                Column("type", css_class="col-4"),
                Column("polymer", css_class="col-4"),
                Fieldset(
                    "Composition",
                    Div(
                        HTML(
                            "Optionally specify the amount of each compound in this material. Amounts are relative and unitless."
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
    For adding compounds to materials.
    """

    class meta:
        model = CompositionPart
        exclude = ()


CompositionPartFormSet = inlineformset_factory(
    Material,
    CompositionPart,
    form=CompositionPartForm,
    fields=["compound", "amount"],
    extra=1,
    can_delete=True,
    help_texts={"compound": None, "device_position": None},
)
