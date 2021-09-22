from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Implement a custom user model to add flexibility in the future."""
    pass
