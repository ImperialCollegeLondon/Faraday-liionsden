from django.contrib import admin

# Register your models here.

from .models import *

# see https://github.com/nnseva/django-jsoneditor
from django.contrib.postgres.fields import JSONField
from jsoneditor.forms import JSONEditor
class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField:{ 'widget':JSONEditor },
    }

admin.site.register([
    Experiment, TestProtocol, Equipment, EquipmentType, ExperimentalApparatus,
    CellConfig, CellBatch, Cell, CellSeparator, Manufacturer
], MyAdmin)


