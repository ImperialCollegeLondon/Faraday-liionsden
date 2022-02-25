from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """Implement a custom user model to add flexibility in the future. <br>
    <b>
    Important: The AnonymousUser MUST exist and be active for object-level
    permissions to work properly. <br>
    AnonymousUser MUST ONLY belong to the "Read only" group.
    </b>
    """

    institution = models.ForeignKey(
        "common.Org", on_delete=models.CASCADE, null=True, blank=True
    )
