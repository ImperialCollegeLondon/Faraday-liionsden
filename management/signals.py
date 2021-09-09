from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

def populate_groups(sender, **kwargs):
    # Different user roles are defined as groups
    user_roles = ['Administrator', 'User manager', 'Maintainer', 
                'Contributor', 'Read only']
    for name in user_roles:
        Group.objects.get_or_create(name=name)

    # Assign permissions for each role
    all_perms = Permission.objects.all()
    # TODO: Probably a more elegant way to do this but for now
    #       we do each role one by one
    data_apps = ['battDB', 'common', 'dfndb']
    admin_apps = ['admin', 'auth', 'authtoken', 'guardian', 
                'management', 'sessions']
    
    # Admins
    Group.objects.get(name='Administrator').permissions.add(*all_perms)
    # User managers
    # TODO: Will need some thinking about 
    # Maintainers
    maintainer_perms = [i for i in all_perms 
                        if i.content_type.app_label in data_apps]
    Group.objects.get(name='Maintainer').permissions.add(*maintainer_perms)
    # Contributors
    contrib_perms = [i for i in maintainer_perms 
                    if i.codename.split('_')[0] in ['view', 'add', 'change']]
    Group.objects.get(name='Contributor').permissions.add(*contrib_perms)               
    # Read only users
    read_perms = [i for i in maintainer_perms 
                    if i.codename.split('_')[0] in ['view']]
    Group.objects.get(name='Read only').permissions.add(*read_perms) 
     

    # TODO: Check that no groups have unexpected permissions?