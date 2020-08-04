from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register([
    Experiment, TestProtocol, Equipment, EquipmentType, ExperimentalApparatus,
    CellConfig, CellBatch, Cell, CellSeparator, Manufacturer
])
