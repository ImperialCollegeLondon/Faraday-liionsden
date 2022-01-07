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

device_specs = [
    {
        "name": "cell",
        "abstract": True,
        "status": "public",
        "user_owner": User.objects.get(username=users[0]["username"]),
    },
    {
        "name": "cathode",
        "abstract": True,
        "status": "public",
        "user_owner": User.objects.get(username=users[0]["username"]),
    },
    {
        "name": "anode",
        "abstract": True,
        "status": "public",
        "user_owner": User.objects.get(username=users[1]["username"]),
    },
    {
        "name": "NMC-111",
        "abstract": False,
        "device_type": "cell",
        "status": "public",
        "user_owner": User.objects.get(username=users[1]["username"]),
    },
]

baker.make_recipe("tests.management.user", **users[0])
