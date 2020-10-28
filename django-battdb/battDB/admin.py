from django.contrib import admin
from common.admin import BaseAdmin, ThingAdmin
from django.utils.safestring import mark_safe
import common
from django.forms import Textarea

# Register your models here.

from .models import *


# Need to override inline class to set model to Device instead of Thing
class CompositeDeviceInline(common.admin.CompositeThingInline):
    model = Device
    exclude = ['attributes']
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


class BatchDeviceInline(admin.TabularInline):
    model = BatchDevice
    extra = 1
    verbose_name_plural = "Batch Members"
    verbose_name = "member"
    exclude = ['attributes']


class DeviceListAdmin(BaseAdmin):
    list_display = (BaseAdmin.list_display or []) + ['inherit_metadata', 'parent', 'devType']
    list_filter = (BaseAdmin.list_filter or []) + ['inherit_metadata', 'devType',]


#class ThingAdmin(mptt.admin.MPTTModelAdmin):
class DeviceAdmin(common.admin.ThingAdmin, DeviceListAdmin):
    inlines = [CompositeDeviceInline,BatchDeviceInline,]


admin.site.register(Device, DeviceAdmin)



admin.site.register(DeviceList, DeviceListAdmin)


admin.site.register(Experiment, ThingAdmin)

class DeviceConfigInline(admin.TabularInline):
    model = DeviceConfigNode
    extra = 2


class DeviceConfigAdmin(BaseAdmin):
    inlines = (DeviceConfigInline,)
    # list_display = ["title", "DOI", "year", "has_pdf"]
    # list_filter = ["year", "publisher", "authors"]


# class ModuleDeviceInline(admin.TabularInline):
#     model = ModuleDevice
#     extra = 2
# #    fk_name = "device"


# class ModuleAdmin(BaseAdmin):
    # inlines = [ModuleDeviceInline,]


admin.site.register([DeviceConfig,], DeviceConfigAdmin)
# admin.site.register([CompositeDevice,], ModuleAdmin)


class DataAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ['get_experiment_link']
    readonly_fields = BaseAdmin.readonly_fields + ['get_experiment_link', 'file_hash']

    def get_experiment_link(self, obj):
        if hasattr(obj,'experiment'):
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:auth_user_change", args=(obj.experiment.pk,)),
                str(obj.experiment)
            ))
        else:
            return "N/A"
    get_experiment_link.short_description="Experiment"

admin.site.register([RawDataFile], DataAdmin)
