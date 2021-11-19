from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """Implement a custom user model to add flexibility in the future."""

    institution = models.ForeignKey(
        "common.Org", on_delete=models.CASCADE, null=True, blank=True
    )
