from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

def populate_groups(sender, **kwargs):
    # Different user roles are defined as groups
    user_roles = {'Administrator', 'User manager', 'Maintainer', 
                'Contributor', 'Read only'}
    for name in user_roles:
        Group.objects.get_or_create(name=name)