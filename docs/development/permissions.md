# Permissions

## Private and public objects

By default, Django allows for class-level permissions so a user or group of users can
have permission to view all experiments or to edit all devices, for example.

We use [Django Guardian](https://django-guardian.readthedocs.io/en/stable/) to enable
object-level permissions so that  users or groups of users are assigned permissions for
a particlar object e.g. a particular device or experiment.

Most models can be set to `status = private` or `status = public` when an object saved
or edited. This controls whether only the `user_owner` of the object or everyone else
can view the object its details.

Most models cannot be edited by the user_owner once "public" because other users may subsequently link their objects to these objects. E.g. two users may have two different batches relating to a parent device specification. If the device specification changes unexpectedly, this could have a knock-on effect for the batches that depend on it. The models with this "standard" setup are:

**dfndb:**

- Parameter
- Data
- Method
- Component
- DataParameter (through table)
- CompositionPart (through table)

**battDB:**

- DeviceSpecification
- Batch
- Equipment
- Parser
- Device
- DeviceParameter (through table)
- SignalType (through table)

**common:**

- Reference

Other models can be edited by the `user_owner` even once public. These models are mostly those that are not likely to be relied upon by other objects, and are:

**battDB:**

- DeviceConfig
- Experiment
- ExperimentDataFile
- UploadedFile
- DataColumn
- DataRange
- DeviceConfigNode (through table)
- ExperimentDevice (through table)

Finally, some objects have unique permissions behaviour: dfndb.Compound, dfndb.QuantityUnit, common.Person and common.Org are always set as visible to all users.

## Signal handlers

When an object is saved, a [post_save
signal](https://docs.djangoproject.com/en/4.1/ref/signals/#post-save) handler contains
the logic to assign permissions to the right groups of users based on the type of
object, its user_owner and its status. These are located in `signals/handlers.py` within
each app.

## User groups

We use [Django
groups](https://docs.djangoproject.com/en/4.1/topics/auth/default/#groups) to manage
permissions. It should not be necessary to assign specific permissions to individual
users: simply add them to the necessary groups so the correct permissions are inherited
from there. The groups are:

- **Administrators** Full access to read/write/update/delete any data and users. These
  are Django "superusers" meaning that they automatically have every permission
  (checking if a superuser has a permission, whether the permission exists or not, will
  always return `True` - see [this blog post on Django permissions for further
  details](https://testdriven.io/blog/django-permissions/)). Admins can perform very
  destructive actions and not many users should be in this category.

- User managers: Access to read/write/update/delete users. They can approve (activate) new users and give them appropriate roles, as well as updating the permissions of existing users. They cannot make users, or themselves, administrators.  

- Maintainers: Have full access to the database, except for users and groups. Can read/add/change/delete any objects **including private objects** as needed, curating the existing data. They are responsible for the wellbeing and long-term sustainability of the database.

- Contributors: Can add items to the database and change the items they have added according to the rules above in **Private and public objects**. They cannot edit or delete other users’ data. They can delete their own “private” data, but it is not fully deleted, just hidden until a maintainer deletes it fully, probably via the admin site.

- Read only users: Can view all the objects marked as public.

## AnonymousUser

The AnonymousUser should belong to the *Read only* group for the public data to be browseable by users who are not logged in ([unauthenticated](https://docs.djangoproject.com/en/4.1/topics/auth/)).

To make it so that users are required to authenticate to browse the database, simply remove the AnonymousUser from the "Read only" group.

:warning: **Do NOT add the AnonymousUser to any other groups, or assign it any other individual permissions!** This would result in unauthenticated users having write permissions over the database.
