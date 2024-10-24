"""Functions to populate the databse with an initial set of quantity units.

These functions are run as part of a migration and pre-populate the database with
some default quantities and units.
"""

from .models import QuantityUnit

SI_QUANTITY_UNITS = [
    dict(
        quantityName="Current",
        quantitySymbol="I",
        unitName="Amps",
        unitSymbol="A",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Voltage",
        quantitySymbol="V",
        unitName="Volts",
        unitSymbol="V",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Time",
        quantitySymbol="t",
        unitName="Seconds",
        unitSymbol="s",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Temperature",
        quantitySymbol="T",
        unitName="Kelvin",
        unitSymbol="K",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Temperature",
        quantitySymbol="T",
        unitName="Celsius",
        unitSymbol="C",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Charge",
        quantitySymbol="Q",
        unitName="Coulombs",
        unitSymbol="C",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Length",
        quantitySymbol="L",
        unitName="Metres",
        unitSymbol="m",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Mass",
        quantitySymbol="m",
        unitName="Kilogram",
        unitSymbol="kg",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Unitless",
        quantitySymbol="",
        unitName="One",
        unitSymbol="1",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Energy",
        quantitySymbol="E",
        unitName="Joules",
        unitSymbol="J",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Area",
        quantitySymbol="A",
        unitName="Metres squared",
        unitSymbol="m^2",
        is_SI_unit=True,
    ),
    dict(
        quantityName="Areal capacity",
        quantitySymbol="Q_A",
        unitName="Coulombs per meters squared",
        unitSymbol="C·m^{-2}",
        is_SI_unit=True,
    ),
]

NOT_SI_QUANTITY_UNITS = [
    dict(
        quantityName="Current",
        quantitySymbol="I",
        unitName="miliamps",
        unitSymbol="mA",
        is_SI_unit=False,
        related_scale=0.001,
    ),
    dict(
        quantityName="Charge",
        quantitySymbol="Q",
        unitName="miliamps hour",
        unitSymbol="mA·h",
        is_SI_unit=False,
        related_scale=3.6,
    ),
    dict(
        quantityName="Charge",
        quantitySymbol="Q",
        unitName="amps hour",
        unitSymbol="A·h",
        is_SI_unit=False,
        related_scale=3600,
    ),
    dict(
        quantityName="Energy",
        quantitySymbol="E",
        unitName="Watts hour",
        unitSymbol="W·h",
        is_SI_unit=False,
        related_scale=3600,
    ),
    dict(
        quantityName="Length",
        quantitySymbol="L",
        unitName="centimetres",
        unitSymbol="cm",
        is_SI_unit=False,
        related_scale=0.01,
    ),
    dict(
        quantityName="Area",
        quantitySymbol="A",
        unitName="centimetres squared",
        unitSymbol="cm^2",
        is_SI_unit=False,
        related_scale=0.0001,
    ),
    dict(
        quantityName="Areal capacity",
        quantitySymbol="Q_A",
        unitName="milliamps hour per centimetres squared",
        unitSymbol="mA·h·cm^{-2}",
        is_SI_unit=False,
        related_scale=36000,
    ),
]


def populate_si_quantities(apps, schema_editor):
    """Adds SI units to the DB

    Args:
        apps (_type_): Not used.
        schema_editor (_type_): Not used.
    """
    for quantity in SI_QUANTITY_UNITS:
        if QuantityUnit.objects.filter(
            **{f"{k}__exact": v for k, v in quantity.items()}
        ).exists():
            continue

        QuantityUnit.objects.create(**quantity)


def populate_not_si_quantities(apps, schema_editor):
    """Adds non-SI units to the DB

    Args:
        apps (_type_): Not used.
        schema_editor (_type_): Not used.
    """
    for quantity in NOT_SI_QUANTITY_UNITS:
        related_unit = QuantityUnit.objects.get(
            quantityName__exact=quantity["quantityName"], is_SI_unit__exact=True
        )
        if QuantityUnit.objects.filter(
            **{f"{k}__exact": v for k, v in quantity.items()}, related_unit=related_unit
        ).exists():
            continue

        QuantityUnit.objects.create(**quantity, related_unit=related_unit)
