"""Functions to populate the databse with an initial set of DeviceSpecification 
and DevciceConfig objects relating to single cells.

These functions are run as part of a migration and pre-populate the database.
"""


def populate_devices(apps, schema_editor):
    """Add DeviceSpecification and DeviceConfig objects to the DB. Both are
    for single cells as this is the default device type and most common use
    case.

    Args:
        apps (_type_): app registry with the current status of the apps in the migration
            process.
        schema_editor (_type_): Not used.
    """
    from battDB.models import DeviceConfig, DeviceSpecification
    from liionsden.settings import settings

    User = apps.get_model(settings.AUTH_USER_MODEL)

    user = User.objects.get_or_create(username="AnonymousUser")[0]
    print("XXXXX")
    print(User)
    print(user)
    print("XXXXX")

    DeviceConfig.objects.create(
        name="Single Cell",
        config_type="expmt",
        status="public",
        user_owner=user,
    )
    DeviceSpecification.objects.create(
        name="Single Cell",
        abstract=True,
        status="public",
        user_owner=user,
    )
