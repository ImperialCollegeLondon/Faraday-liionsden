from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm, remove_perm

import dfndb.models as dfn


@receiver(post_save, sender=dfn.Parameter)
@receiver(post_save, sender=dfn.Data)
@receiver(post_save, sender=dfn.Method)
@receiver(post_save, sender=dfn.Component)
@receiver(post_save, sender=dfn.DataParameter)
@receiver(post_save, sender=dfn.CompositionPart)
def set_permissions(sender, instance, **kwargs):
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
        for perm in [change, view]:
            assign_perm(perm, instance.user_owner, instance)
        for group in ["Read only", "Contributor"]:
            remove_perm(view, Group.objects.get(name=group), instance)

    elif instance.status.lower() == "public":
        remove_perm(change, instance.user_owner, instance)
        for group in ["Read only", "Contributor"]:
            assign_perm(view, Group.objects.get(name=group), instance)

    elif instance.status.lower() == "deleted":
        for group in ["Read only", "Contributor"]:
            remove_perm(view, Group.objects.get(name=group), instance)
        for perm in [change, view]:
            remove_perm(perm, instance.user_owner, instance)

    else:
        raise ValueError("Object status must be private, public or deleted.")


@receiver(post_save, sender=dfn.Compound)
@receiver(post_save, sender=dfn.QuantityUnit)
def set_visible_to_all(sender, instance, **kwargs):
    """Set object-level permissions according to a setup suitable for very generic
    objects with no status or owner: The saved model is visible to all authenticated
    users and editable by maintainers.
    """
    # Get permissions for model
    delete, change, view = _get_perm_codenames(sender)

    # Maintainers get all perms
    for perm in [delete, change, view]:
        assign_perm(perm, Group.objects.get(name="Maintainer"), instance)

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
