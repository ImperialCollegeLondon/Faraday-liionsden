"""Functions to populate the databse with an initial set of parameters.

These functions are run as part of a migration and pre-populate the database with
some default parameters.
"""

PARAMETERS = [
    dict(name="Time", status="Public", symbol="t", unit=("Time", "s")),
    dict(name="Step time", status="Public", symbol="ts", unit=("Time", "s")),
    dict(name="Voltage", status="Public", symbol="V", unit=("Voltage", "V")),
    dict(name="Current", status="Public", symbol="I", unit=("Current", "mA")),
    dict(name="Current", status="Public", symbol="I", unit=("Current", "A")),
    dict(
        name="Net charge passed",
        status="Public",
        symbol="Q-Q_0",
        unit=("Charge", "mA·h"),
    ),
    dict(
        name="Net charge passed",
        status="Public",
        symbol="Q-Q_0",
        unit=("Charge", "A·h"),
    ),
    dict(name="Temperature", status="Public", symbol="T", unit=("Temperature", "C")),
    dict(
        name="Charge passed during discharge",
        status="Public",
        symbol="Q discharge",
        unit=("Charge", "mA·h"),
    ),
    dict(
        name="Net energy passed",
        status="Public",
        symbol="E",
        unit=("Energy", "W·h"),
    ),
    dict(
        name="New section changes",
        status="Public",
        symbol="Ns changes",
        unit=("Unitless", "1"),
    ),
    dict(name="Cycle number", status="Public", symbol="Cyl", unit=("Unitless", "1")),
    dict(name="Record number", status="Public", symbol="Rec", unit=("Unitless", "1")),
    dict(
        name="Cell nominal capacity",
        status="Public",
        symbol="Q",
        unit=("Charge", "A·h"),
    ),
    dict(name="Form factor", status="Public", symbol="f_f", unit=("Unitless", "1")),
    dict(name="Anode size", status="Public", symbol="A_{anode}", unit=("Area", "cm^2")),
    dict(
        name="Cathode size",
        status="Public",
        symbol="A_{cathode}",
        unit=("Area", "cm^2"),
    ),
    dict(
        name="Anode loading",
        status="Public",
        symbol="Q_{anode}",
        unit=("Areal capacity", "mA·h·cm^{-2}"),
    ),
    dict(
        name="Cathode loading",
        status="Public",
        symbol="Q_{cathode}",
        unit=("Areal capacity", "mA·h·cm^{-2}"),
    ),
    dict(
        name="Number of layers",
        status="Public",
        symbol="n_{layers}",
        unit=("Unitless", "1"),
    ),
    dict(
        name="Electrode coating",
        status="Public",
        symbol="coating",
        unit=("Unitless", "1"),
    ),
    dict(
        name="Electrolyte component",
        status="Public",
        symbol="eletrolyte",
        unit=("Unitless", "1"),
    ),
]


def populate_parameters(apps, schema_editor):
    """Adds parameters (aka signal types) to the DB

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

        if Parameter.objects.filter(
            **{f"{k}__exact": v for k, v in quant.items()}
        ).exists():
            continue

        Parameter.objects.create(**quant)


def set_initial_experiment_parameters(apps, schema_editor):
    """Set certain initial parameters to have parametery_type="experiment" as opposed
    to "device" (the default)."""

    Parameter = apps.get_model("dfndb", "Parameter")

    experimental_parameters = [
        "Time",
        "Step time",
        "Voltage",
        "Current",
        "Net charge passed",
        "Temperature",
        "Charge passed during discharge",
        "Net energy passed",
        "New section changes",
        "Cycle number",
        "Record number",
    ]

    for parameter in experimental_parameters:
        Parameter.objects.filter(name__exact=parameter).update(
            parameter_type="experiment"
        )
