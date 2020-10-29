from django.contrib import admin
from common.admin import BaseAdmin, ThingAdmin
from django.utils.safestring import mark_safe
import common
from django.forms import Textarea

# Register your models here.

from .models import *


# Need to override inline class to set model to Device instead of Thing
class CompositeDeviceInline(common.admin.CompositeThingInline):
    model = DeviceSpecification
    exclude = ['attributes', 'user_owner']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }

    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['user_owner'] = request.user.pk
        return get_data


class DeviceParameterInline(admin.TabularInline):
    model = DeviceParameter
    extra = 1

class DeviceSpecAdmin(BaseAdmin):
    list_display = (BaseAdmin.list_display or []) + ['inherit_metadata', 'parent', 'device_type']
    list_filter = (BaseAdmin.list_filter or []) + ['inherit_metadata', 'device_type',]
    inlines = [CompositeDeviceInline, DeviceParameterInline, ]


admin.site.register(DeviceSpecification, DeviceSpecAdmin)


class BatchDeviceInline(admin.TabularInline):
    model = BatchDevice
    extra = 1
    verbose_name_plural = "Batch Members"
    verbose_name = "member"
    exclude = ['attributes']


#class ThingAdmin(mptt.admin.MPTTModelAdmin):
class DeviceBatchAdmin(BaseAdmin):
    inlines = [BatchDeviceInline,]


admin.site.register(DeviceBatch, DeviceBatchAdmin)


class ExperimentDataInline(admin.TabularInline):
    model = ExperimentDataFile
    extra = 1
    exclude = ['attributes', 'file_hash', 'user_owner']


class ExperimentAdmin(common.admin.BaseAdmin):
    inlines = [ExperimentDataInline]

admin.site.register(Experiment, ExperimentAdmin)

# class DeviceConfigInline(admin.TabularInline):
#     model = DeviceConfigNode
#     extra = 2
#
#
# class DeviceConfigAdmin(BaseAdmin):
#     inlines = (DeviceConfigInline,)
#     # list_display = ["title", "DOI", "year", "has_pdf"]
#     # list_filter = ["year", "publisher", "authors"]


# class ModuleDeviceInline(admin.TabularInline):
#     model = ModuleDevice
#     extra = 2
# #    fk_name = "device"


# class ModuleAdmin(BaseAdmin):
    # inlines = [ModuleDeviceInline,]


#admin.site.register([DeviceConfig,], DeviceConfigAdmin)
# admin.site.register([CompositeDevice,], ModuleAdmin)

class DeviceDataInline(admin.TabularInline):
    model = DataColumn
    readonly_fields = ["serialNo"]
    extra = 0

class DataAdmin(BaseAdmin):
    inlines = [DeviceDataInline, ]
    list_display = BaseAdmin.list_display + ['get_experiment_link', 'file_exists', 'is_parsed']
    readonly_fields = BaseAdmin.readonly_fields + ['get_experiment_link', 'file_hash']

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
