from django.contrib.auth import get_user_model
from model_bakery import baker

from battDB.models import Batch, DeviceSpecification, Equipment, Experiment

User = get_user_model()

users = [
    {
        "username": "michael",
        "password": "pbkdf2_sha256$320000$SpAMLvONkpuAzdtWd9xrId$rByL+fcujnTiHfdtNnr6A2i0OBgXGJZo1SCoOp9BbmQ=",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": False,
        "is_active": True,
    },
    {
        "username": "victor",
        "password": "pbkdf2_sha256$320000$SpAMLvONkpuAzdtWd9xrId$rByL+fcujnTiHfdtNnr6A2i0OBgXGJZo1SCoOp9BbmQ=",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": False,
        "is_active": True,
    },
]


for user in users:
    if not User.objects.filter(username=user["username"]).exists():
        u, created = User.objects.get_or_create(**user)
        if created:
            print("created user: {}...".format(user["username"]))
