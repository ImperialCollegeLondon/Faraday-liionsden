from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Group

import battDB.models as bdb


# Models in the decorators below follow "standard" permission setup
@receiver(post_save, sender=bdb.DeviceSpecification)
@receiver(post_save, sender=bdb.Batch)
@receiver(post_save, sender=bdb.Equipment)
def set_permissions_standard(sender, instance, **kwargs):
    """Set object-level permissions according to a standard setup: The contributing
    user can modify the object if status is "private" but not if "public".
    """
    # Get permissions for model
    delete, change, view = _get_perm_codenames(sender)

    # Maintainers get all perms
    for perm in [delete, change, view]:
        assign_perm(perm, Group.objects.get(name="Maintainer"), instance)

    # Permissions based on obj status
    if instance.status.lower() == "private":
        # If there is a user_owner, individual permissions can be assigned
        if hasattr(instance, "user_owner") and instance.user_owner is not None:
            for perm in [change, view]:
                assign_perm(perm, instance.user_owner, instance)

    elif instance.status.lower() == "public":
        for group in ["Read only", "Contributor"]:
            assign_perm(view, Group.objects.get(name=group), instance)


# Models in the decorators below follow a less strict permissions setup
@receiver(post_save, sender=bdb.DeviceConfig)
@receiver(post_save, sender=bdb.Experiment)
@receiver(post_save, sender=bdb.ExperimentDataFile)
def set_permissions_modifiable(sender, instance, **kwargs):
    """Set object-level permissions according to a less strict setup: The contributing
    user can modify the object if status is "private" or "public".
    """
    # Get permissions for model
    delete, change, view = _get_perm_codenames(sender)

    # Maintainers get all perms
    for perm in [delete, change, view]:
        assign_perm(perm, Group.objects.get(name="Maintainer"), instance)

    # If there is a user_owner, individual permissions can be assigned
    if hasattr(instance, "user_owner") and instance.user_owner is not None:
        for perm in [change, view]:
            assign_perm(perm, instance.user_owner, instance)

    # Other users perms based on obj status
    if instance.status.lower() == "public":
        for group in ["Read only", "Contributor"]:
            assign_perm(view, Group.objects.get(name=group), instance)


def _get_perm_codenames(model):
    """Helper function to get delete, change and view permission codenames for a
    given model.
    """
    return (
        f"delete_{model._meta.model_name}",
        f"change_{model._meta.model_name}",
        f"view_{model._meta.model_name}",
    )
