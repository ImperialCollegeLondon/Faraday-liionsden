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
    extra = 0
    verbose_name_plural = "Batch Members"
    verbose_name = "member"
    readonly_fields = ['used_in', 'last_measured_SoH', 'attributes']
    exclude = ['attributes']

class DeviceBatchInline(common.admin.TabularInline):
    model = DeviceBatch
    extra = 0
    verbose_name = "sub-device"
    verbose_name_plural = "Sub-devices"
    exclude = ['attributes']


#class ThingAdmin(mptt.admin.MPTTModelAdmin):
class DeviceBatchAdmin(common.admin.BaseAdmin, mptt.admin.MPTTModelAdmin):
    list_display = ["__str__"] + ['manufacturer', 'serialNo', 'manufactured_on', 'batch_size'] + BaseAdmin.list_display_extra
    list_filter = BaseAdmin.list_filter + ['manufacturer', 'batch_size']
    inlines = [DeviceBatchInline, BatchDeviceInline,]


admin.site.register(DeviceBatch, DeviceBatchAdmin)


class ExperimentDataInline(common.admin.TabularInline):
    model = ExperimentDataFile
    extra = 0
    exclude = ['attributes', 'file_hash', 'user_owner']


class ExperimentDeviceInline(common.admin.TabularInline):
    model = ExperimentDevice
    extra = 1
    readonly_fields = ["getSerialNo"]


class ExperimentAdmin(common.admin.BaseAdmin):
    readonly_fields = ['data_files_list'] + BaseAdmin.readonly_fields
    list_display = ['__str__'] + ['devices_', 'files_', 'cycles_'] + BaseAdmin.list_display_extra
    inlines = [ExperimentDeviceInline, ]
#    form = ExperimentForm

    def data_files_list(self, obj):
        links_str = ""
        for file in obj.data_files.all():
            links_str = links_str + '<a href="{}">{}</a>, '.format(
                reverse("admin:battDB_experimentdatafile_change", args=(file.pk,)),str(file))
        return mark_safe(links_str)
    data_files_list.short_description = "Data Files"


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
    extra = 0




class DataRangeInline(common.admin.TabularInline):
    model = DataRange
    extra = 0

class DataAdmin(BaseAdmin):
    """
    FIXME: This class exhibits an n+1 query antipattern. For each row returned, 2 additional queries are fired.
     This should be done with a JOIN instead.
    """
    inlines = [DeviceDataInline, DataRangeInline, ]
    list_display = ['__str__', 'user_owner', 'get_file_link', 'get_experiment_link', 'use_parser', 'file_data', 'parsed_data', 'created_on', 'status']
    list_filter = ['experiment'] + BaseAdmin.list_filter
    readonly_fields = BaseAdmin.readonly_fields + ['is_parsed', 'get_experiment_link', 'file_hash',
                                                   'file_columns', 'num_ranges']
    # form=DataFileForm

    def size(self, obj):
        return obj.raw_data_file.size()
    size.short_description = "Raw Size"

    def file_data(self, obj):
        return "%dx%d" % (obj.file_rows(), len(obj.file_columns()))
    file_data.short_description = "File RxC"

    def parsed_data(self, obj):
        return "%dx%d" % (obj.parsed_rows(), len(obj.parsed_columns()))
    parsed_data.short_description="Parsed"

    def get_experiment_link(self, obj):
        if hasattr(obj,'experiment') and obj.experiment is not None:
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:battDB_experiment_change", args=(obj.experiment.pk,)),
                str(obj.experiment)
            ))
        else:
            return "N/A"
    get_experiment_link.short_description="Experiment"

    def get_file_link(self, obj):
        if hasattr(obj, 'raw_data_file') and obj.raw_data_file is not None:
            return mark_safe(u'''
            <button type="button"> <a href="%s">\u2193%s</a> </button>
            ''' % (obj.raw_data_file.file.url, obj.raw_data_file.size()))
        else:
            return "N/A"
    get_file_link.short_description = "View RAW"


admin.site.register([ExperimentDataFile], DataAdmin)


admin.site.register([Equipment, Harvester], BaseAdmin)

# class DataParserAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register([DataParser, ], DataParserAdmin)


class FolderAdmin(mptt.admin.DraggableMPTTAdmin, BaseAdmin):
    pass

admin.site.register(FileFolder, FolderAdmin)


class ParserSignalInline(common.admin.TabularInline):
    model = SignalType
    extra = 1
    ordering = ('order',)

class ParserAdmin(BaseAdmin):
    inlines = (ParserSignalInline,)

admin.site.register(Parser, ParserAdmin)