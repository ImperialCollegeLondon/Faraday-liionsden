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

from common.forms import DataCreateForm
from dfndb.models import Compound


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
                Field("notes"),
                ButtonHolder(Submit("submit", "save")),
                css_class="row",
            )
        )
