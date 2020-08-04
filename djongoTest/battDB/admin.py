from django.contrib import admin

# Register your models here.

from djongo.models import CheckConstraint, Q
from djongo import models
from pymongo.read_concern import ReadConcern
from .models import Experiment, Equipment


# see https://github.com/nnseva/django-jsoneditor
from djongo.models import JSONField
from jsoneditor.forms import JSONEditor
class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField:{ 'widget':JSONEditor },
    }

admin.site.register([Experiment, Equipment], MyAdmin)
