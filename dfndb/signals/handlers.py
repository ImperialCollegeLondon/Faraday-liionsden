from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from ..models import Compound

@receiver(post_save, sender=Compound)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the creator."""
    
    # Only creator can change     
    assign_perm("change_compound", instance.user_owner, instance)

    # TODO: If public/published, give others read permissions
    #       Otherwise don't. 