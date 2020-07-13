from django.contrib import admin

# Register your models here.

from djongo.models import CheckConstraint, Q
from djongo import models
from pymongo.read_concern import ReadConcern
from .models import Experiment, Equipment

admin.site.register([Experiment, Equipment])
