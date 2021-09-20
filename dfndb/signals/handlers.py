from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from ..models import Compound
from django.contrib.auth.models import Group

@receiver(post_save, sender=Compound)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the creator."""
    
    # Only creator can change     
    assign_perm("change_compound", instance.user_owner, instance)
    # Maintainers can do everything 
    for perm in ["delete_compound", "change_compound", "view_compound"]:
        assign_perm(perm,
            Group.objects.get(name='Maintainer'),
            instance
            )

    # If published, give others read permissions otherwise don't. 
    if instance.status.lower() == 'private':
        assign_perm("view_compound", instance.user_owner, instance)
    elif instance.status.lower() == 'published': 
        for group in ["Read only", "Contributor"]:
            assign_perm(
                "view_compound",
                Group.objects.get(name=group),
                instance
                )
