"""Functions to populate the databse with an initial set of parsers.

These functions are run as part of a migration and pre-populate the database with
some default parsers.
"""


def populate_parsers(apps, schema_editor):
    """Adds parsers to the DB

    Args:
        apps (_type_): app registry with the current status of the apps in the migration
            process.
        schema_editor (_type_): Not used.
    """
    from liionsden.settings import settings
    from parsing_engines import available_parsing_engines, get_parsing_engine

    QuantityUnit = apps.get_model("dfndb", "QuantityUnit")
    Parameter = apps.get_model("dfndb", "Parameter")
    Parser = apps.get_model("battDB", "Parser")
    SignalType = apps.get_model("battDB", "SignalType")
    User = apps.get_model(settings.AUTH_USER_MODEL)

    user = User.objects.get_or_create(username="AnonymousUser")[0]
    engines = [engine for engine in available_parsing_engines()]

    for name, file_format in engines:
        if Parser.objects.filter(
            name__exact=name, file_format__exact=file_format, user_owner__exact=user
        ).exists():
            continue

        parser = Parser.objects.create(
            name=name, file_format=file_format, user_owner=user, status="Public"
        )

        engine = get_parsing_engine(name)

        for i, (col_name, param_info) in enumerate(engine.mandatory_columns.items()):
            unit = QuantityUnit.objects.get(
                quantityName__exact=param_info["unit"][0],
                unitSymbol__exact=param_info["unit"][1],
            )
            param = Parameter.objects.get(
                symbol__exact=param_info["symbol"],
                unit__exact=unit,
            )
            SignalType.objects.create(
                parameter=param, col_name=col_name, order=i + 1, parser=parser
            )
