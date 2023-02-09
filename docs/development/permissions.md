# Permissions

By default, Django allows for class-level permissions so a user or group of users can
have permission to view all experiments or to edit all devices, for example.

We use [Django Guardian](https://django-guardian.readthedocs.io/en/stable/) to enable
object-level permissions so that  users or groups of users are assigned permissions for
a particlar object e.g. a particular device or experiment.
