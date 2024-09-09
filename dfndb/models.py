import numpy as np
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django_better_admin_arrayfield.models.fields import ArrayField
from molmass import Formula

import common.models as cm

from .validators import validate_formula


class Compound(models.Model):
    """Chemical Compound or Element, e.g. Lithium, Graphite."""

    name = models.CharField(
        max_length=100,
        help_text="Full name for the element or compound.",
        unique=True,
    )
    formula = models.CharField(
        max_length=20,
        help_text="Chemical formula",
        unique=True,
        validators=[validate_formula],
    )

    @property
    def mass(self):
        return Formula(self.formula).mass

    def __str__(self):
        return f"{self.name} ({self.formula})"


class Component(cm.BaseModelMandatoryName):
    """A component used as part of an electrochemical cell specification, e.g. NMC622.

    Make use of the 'notes' field for additional explanation
    """

    composition = models.ManyToManyField(
        Compound,
        through="CompositionPart",
        help_text="eg. NMC 622 would have 3 Compounds: Nickel 6, Manganese 2, Cobalt 2",
    )
    MATERIAL_TYPE_CHOICES = [
        (1, "Anode"),
        (2, "Cathode"),
        (3, "Electrolyte"),
        (4, "Separator"),
    ]
    type = models.PositiveSmallIntegerField(choices=MATERIAL_TYPE_CHOICES)

    def __str__(self):
        return self.name or ""

    def get_absolute_url(self):
        return reverse("dfndb:Component", kwargs={"pk": self.pk})


class CompositionPart(models.Model):
    """Compound amounts for use in components."""

    compound = models.ForeignKey(
        Compound, on_delete=models.CASCADE, related_name="components"
    )
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])

    def get_percentage(self):
        total = CompositionPart.objects.filter(component=self.component).aggregate(
            Sum("amount")
        )["amount__sum"]
        return np.round((float(self.amount or 0) * 100 / total), decimals=2)

    def percentage(self):
        return f"{self.get_percentage():3.3f}%"

    @property
    def user_owner(self):
        return self.component.user_owner

    @property
    def status(self):
        return self.component.status

    def __str__(self):
        return "%s%d" % (self.compound.formula, self.amount)

    class Meta:
        unique_together = ("compound", "amount", "component")


class Method(cm.BaseModel):
    """Description of experimental / modelling method types."""

    METHOD_TYPE_MODELLING = 1000
    METHOD_TYPE_EXPERIMENTAL = 2000
    METHOD_TYPE_MANUFACTURE = 3000
    METHOD_TYPE_CHOICES = [
        (METHOD_TYPE_EXPERIMENTAL, "Experimental"),
        (METHOD_TYPE_MODELLING, "Modelling"),
        (METHOD_TYPE_MANUFACTURE, "Manufacture"),
    ]
    type = models.IntegerField(
        choices=METHOD_TYPE_CHOICES, default=METHOD_TYPE_MODELLING
    )

    description = ArrayField(
        models.CharField(
            blank=True, help_text="Method description in PyBaMM format", max_length=2000
        )
    )


class QuantityUnit(models.Model):
    """Quantity Units e.g. Volts, Amps, Watts."""

    quantityName = models.CharField(
        max_length=100, help_text="Readable name e.g. 'Charge'"
    )
    quantitySymbol = models.CharField(
        max_length=40, help_text="e.g. 'Q', Will be decoded as LaTeX"
    )
    unitName = models.CharField(max_length=40, blank=True, help_text="e.g. 'Coulombs'")
    unitSymbol = models.CharField(max_length=40, help_text="e.g. 'C'")
    is_SI_unit = models.BooleanField(default=False)
    related_unit = models.ForeignKey(
        "QuantityUnit",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"is_SI_unit": True},
        help_text="If this unit is NOT an SI unit, it should relate to one",
    )
    related_scale = models.FloatField(
        blank=True, null=True, help_text="Scaling of this unit from the SI unit"
    )

    def __str__(self):
        return f"{self.quantityName} ({self.quantitySymbol}) / {self.unitSymbol}"

    class Meta:
        unique_together = ("quantityName", "unitSymbol")


class Parameter(cm.BaseModel):
    """Experiment or simulation parameters.

    E.g. electrode thickness, electrolyte concentration etc. Use the notes field to
    explain what this parameter is for. Use the JSON field to add machine-readable
    metadata.
    """

    TYPE_CHOICES = (
        ("device", "Device"),
        ("experiment", "Experiment"),
    )

    symbol = models.CharField(
        max_length=40, help_text="Parameter symbol. Will be decoded as LaTeX"
    )
    unit = models.ForeignKey(QuantityUnit, on_delete=models.RESTRICT)
    parameter_type = models.CharField(
        max_length=40,
        choices=TYPE_CHOICES,
        default="device",
        help_text=(
            "Whether this parameter defines a device or is measured in an experiment"
        ),
    )

    class Meta:
        unique_together = ("symbol", "unit")

    def __str__(self):
        return f"{self.name}: {self.symbol} / {self.unit.unitSymbol}"


class Data(cm.BaseModel):
    """Experiment or simulation data.

    This model represents a source of data parameters, typically a paper. All
    parameters described in data source are packed together here.
    """

    reference = models.ForeignKey(
        cm.Reference, on_delete=models.CASCADE, null=True, blank=True
    )
    parameter = models.ManyToManyField(Parameter, through="DataParameter")

    class Meta:
        verbose_name_plural = "Data"  # don't pluralise to "Datas"


class DataParameter(models.Model):
    """Parameters on data."""

    PARAM_TYPE_NONE = 10
    PARAM_TYPE_INPUT = 20
    PARAM_TYPE_OUTPUT = 30

    PARAM_TYPE = (
        (PARAM_TYPE_NONE, "None"),
        (PARAM_TYPE_INPUT, "Input"),
        (PARAM_TYPE_OUTPUT, "Output"),
    )

    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=PARAM_TYPE, default=PARAM_TYPE_NONE)
    component = models.ForeignKey(
        Component, on_delete=models.CASCADE, blank=True, null=True
    )
    value = models.JSONField(blank=True, null=True)

    @property
    def user_owner(self):
        return self.parameter.user_owner

    @property
    def status(self):
        return self.parameter.status

    def __str__(self):
        return str(self.parameter)

    class Meta:
        unique_together = ("data", "parameter", "component")
