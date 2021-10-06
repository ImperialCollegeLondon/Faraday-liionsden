from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Group

import battDB.models as bdb


@receiver(post_save, sender=bdb.DeviceSpecification)
def set_standard_permissions(sender, instance, **kwargs):
    """Set object-level permissions according to a standard setup.
    Contributing user can modify the object if status is "private" but not
    if "public".
    """

    # Get permissions for model
    delete, change, view = (
        f"delete_{sender._meta.model_name}",
        f"change_{sender._meta.model_name}",
        f"view_{sender._meta.model_name}",
    )

    # Maintainers get all perms
    for perm in [delete, change, view]:
        assign_perm(perm, Group.objects.get(name="Maintainer"), instance)

    # Contributing user and other users perms based on obj status
    if instance.status.lower() == "private":
        for perm in [change, view]:
            assign_perm(perm, instance.user_owner, instance)

    elif instance.status.lower() == "public":
        for group in "Read only", "Contributor":
            assign_perm(view, Group.objects.get(name=group), instance)
