from django.contrib import admin
from common.admin import BaseAdmin

# Register your models here.

from .models import *




admin.site.register([
    Experiment, TestProtocol, Equipment, EquipmentType, ExperimentalApparatus, SignalType,
    CellConfig, CellBatch, Cell, CellType, ExperimentDataFile, DataRange, RawDataFile], BaseAdmin)


#class DataAdmin(MyAdmin):
#    readonly_fields = ["data"]
#
#admin.site.register([ExperimentData], DataAdmin)
