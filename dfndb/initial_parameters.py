"""Functions to populate the databse with an initial set of parameters.

These functions are run as part of a migration and pre-populate the database with
some default parameters.
"""
PARAMETERS = [
    dict(name="Time", status="Public", symbol="t", unit=("Time", "s")),
    dict(name="Voltage", status="Public", symbol="V", unit=("Voltage", "V")),
    dict(name="Current", status="Public", symbol="I", unit=("Current", "mA")),
    dict(
        name="Net charge passed",
        status="Public",
        symbol="Q-Q_0",
        unit=("Charge", "mA·h"),
    ),
    dict(name="Temperature", status="Public", symbol="T", unit=("Temperature", "C")),
    dict(
        name="Charge passed during discharge",
        status="Public",
        symbol="Q discharge",
        unit=("Charge", "mA·h"),
    ),
    dict(
        name="New section changes",
        status="Public",
        symbol="Ns changes",
        unit=("Unitless", "1"),
    ),
    dict(name="Cycle number", status="Public", symbol="Cyl", unit=("Unitless", "1")),
]


def populate_parameters(apps, schema_editor):
    """Adds parameters (aka sygnal types) to the DB

    Args:
        apps (_type_): app registry with the current status of the apps in the migration
            process.
        schema_editor (_type_): Not used.
    """
    from liionsden.settings import settings

    QuantityUnit = apps.get_model("dfndb", "QuantityUnit")
    Parameter = apps.get_model("dfndb", "Parameter")
    User = apps.get_model(settings.AUTH_USER_MODEL)

    user = User.objects.get_or_create(username="AnonymousUser")[0]

    for quantity in PARAMETERS:
        quant = quantity.copy()
        quant["unit"] = QuantityUnit.objects.get(
            quantityName__exact=quantity["unit"][0],
            unitSymbol__exact=quantity["unit"][1],
        )
        quant["user_owner"] = user
        Parameter.objects.create(**quant)
