from django.contrib import admin
from common.admin import BaseAdmin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import *


admin.site.register([
      Experiment, #Equipment, EquipmentType,
      Device, Cell
      ], BaseAdmin)


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
