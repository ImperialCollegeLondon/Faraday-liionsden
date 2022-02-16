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
        unitName="Culombs",
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
        unitName="kilogram",
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
]


def populate_si_quantities(apps, schema_editor):
    """Adds SI units to the DB

    Args:
        apps (_type_): Not used.
        schema_editor (_type_): Not used.
    """
    for quantity in SI_QUANTITY_UNITS:
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
        QuantityUnit.objects.create(**quantity, related_unit=related_unit)
