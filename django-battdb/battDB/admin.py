from django.contrib import admin
from common.admin import BaseAdmin
from django.utils.safestring import mark_safe
import common
from django.forms import Textarea
import mptt
from .forms import *

# Register your models here.

from .models import *



class DeviceParameterInline(common.admin.TabularInline):
    model = DeviceParameter
    extra = 1


class DeviceSpecInline(common.admin.CompositeBaseInLine):
    model = DeviceSpecification
    extra = 1

class DeviceSpecAdmin(common.admin.HasMPTTAdmin):
    model = DeviceSpecification
    list_display = common.admin.HasMPTTAdmin.list_display + ('device_type', 'abstract', 'complete')
    list_filter = (common.admin.HasMPTTAdmin.list_filter or []) + ['device_type', 'abstract', 'complete']
    #readonly_fields = (common.admin.HasMPTTAdmin.readonly_fields or []) + ['inherit_metadata']
    inlines = [DeviceSpecInline, DeviceParameterInline, ]


admin.site.register(DeviceSpecification, DeviceSpecAdmin)


class BatchDeviceInline(common.admin.TabularInline):
    model = BatchDevice
    extra = 1
    verbose_name_plural = "Batch Members"
    verbose_name = "member"
    exclude = ['attributes']

class DeviceBatchInline(common.admin.TabularInline):
    model = DeviceBatch
    extra = 0
    verbose_name = "member"
    exclude = ['attributes']


#class ThingAdmin(mptt.admin.MPTTModelAdmin):
class DeviceBatchAdmin(common.admin.BaseAdmin, mptt.admin.MPTTModelAdmin):
    list_display = BaseAdmin.list_display + ['manufacturer', 'serialNo', 'manufactured_on', 'batch_size']
    list_filter = BaseAdmin.list_filter + ['manufacturer', 'batch_size']
    inlines = [DeviceBatchInline, BatchDeviceInline,]


admin.site.register(DeviceBatch, DeviceBatchAdmin)


class ExperimentDataInline(common.admin.TabularInline):
    model = ExperimentDataFile
    extra = 0
    exclude = ['attributes', 'file_hash', 'user_owner']


class ExperimentDevicesInline(common.admin.TabularInline):
    model = DataColumn
    extra = 1
    # exclude = ['attributes', 'file_hash', 'user_owner']

class ExperimentAdmin(common.admin.BaseAdmin):
#    readonly_fields = BaseAdmin.readonly_fields + ['data_files']
    exclude = ['data_files']
    inlines = [ExperimentDataInline, ]
#    form = ExperimentForm


admin.site.register(Experiment, ExperimentAdmin)


class DeviceConfigInline(common.admin.TabularInline):
    model = DeviceConfigNode
    extra = 2


class DeviceConfigAdmin(BaseAdmin):
    inlines = (DeviceConfigInline,)


admin.site.register([DeviceConfig,], DeviceConfigAdmin)

# class ModuleDeviceInline(admin.TabularInline):
#     model = ModuleDevice
#     extra = 2
# #    fk_name = "device"


# class ModuleAdmin(BaseAdmin):
    # inlines = [ModuleDeviceInline,]

# admin.site.register([CompositeDevice,], ModuleAdmin)

# class DataFileAdmin(admin.TabularInline):
#     model = common.models.UploadedFile
#     readonly_fields = ["hash"]
#     extra = 0

class DeviceDataInline(common.admin.TabularInline):
    model = DataColumn
    readonly_fields = ["serialNo"]
    extra = 0

class DataRangeInline(common.admin.TabularInline):
    model = DataRange
    extra = 0

class DataAdmin(BaseAdmin):
    inlines = [DeviceDataInline, DataRangeInline, ]
    list_display = BaseAdmin.list_display + ['get_experiment_link', 'file_exists', 'is_parsed']
    readonly_fields = BaseAdmin.readonly_fields + ['parsed_data', 'get_experiment_link', 'file_hash', 'columns']
    #form=DataFileForm

    def get_experiment_link(self, obj):
        if hasattr(obj,'experiment') and obj.experiment is not None:
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:battDB_experiment_change", args=(obj.experiment.pk,)),
                str(obj.experiment)
            ))
        else:
            return "N/A"
    get_experiment_link.short_description="Experiment"




admin.site.register([ExperimentDataFile], DataAdmin)


admin.site.register([Equipment, DataParser], BaseAdmin)

