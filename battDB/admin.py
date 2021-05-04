import mptt
from django.contrib import admin
from django.utils.safestring import mark_safe

import common
from common.admin import BaseAdmin

from .models import (
    Batch,
    DataColumn,
    DataRange,
    Device,
    DeviceConfig,
    DeviceConfigNode,
    DeviceParameter,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    ExperimentDevice,
    Parser,
    SignalType,
    UploadedFile,
    reverse,
)


class DeviceParameterInline(common.admin.TabularInline):
    model = DeviceParameter
    extra = 1


class DeviceSpecInline(common.admin.CompositeBaseInLine):
    model = DeviceSpecification
    extra = 1


class DeviceSpecAdmin(common.admin.HasMPTTAdmin):
    model = DeviceSpecification
    save_as = True
    list_display = common.admin.HasMPTTAdmin.list_display + (
        "device_type",
        "abstract",
        "complete",
    )
    list_filter = (common.admin.HasMPTTAdmin.list_filter or []) + [
        "device_type",
        "abstract",
        "complete",
    ]
    inlines = [
        DeviceSpecInline,
        DeviceParameterInline,
    ]


admin.site.register(DeviceSpecification, DeviceSpecAdmin)


class DeviceInline(common.admin.TabularInline):
    model = Device
    extra = 0
    verbose_name_plural = "Batch Members"
    verbose_name = "member"
    readonly_fields = ["used_in", "last_measured_state_of_health", "attributes"]
    exclude = ["attributes"]


class BatchInline(common.admin.TabularInline):
    """ TODO: What's the use case for these sub devices?"""

    model = Batch
    extra = 0
    verbose_name = "sub-device"
    verbose_name_plural = "Sub-devices"
    exclude = ["attributes"]


# class ThingAdmin(mptt.admin.MPTTModelAdmin):
class BatchAdmin(common.admin.BaseAdmin, mptt.admin.MPTTModelAdmin):
    list_display = (
        ["__str__"]
        + ["manufacturer", "serialNo", "manufactured_on", "batch_size"]
        + BaseAdmin.list_display_extra
    )
    list_filter = BaseAdmin.list_filter + ["manufacturer", "batch_size"]
    save_as = True
    inlines = [
        BatchInline,
        DeviceInline,
    ]


admin.site.register(Batch, BatchAdmin)


class ExperimentDataInline(common.admin.TabularInline):
    model = ExperimentDataFile
    extra = 0
    exclude = ["attributes", "file_hash", "user_owner"]


class ExperimentDeviceInline(common.admin.TabularInline):
    model = ExperimentDevice
    extra = 1
    readonly_fields = ["getSerialNo"]


class ExperimentAdmin(common.admin.BaseAdmin):
    readonly_fields = ["data_files_list"] + BaseAdmin.readonly_fields
    list_display = (
        ["__str__"] + ["devices_", "files_", "cycles_"] + BaseAdmin.list_display_extra
    )
    inlines = [
        ExperimentDeviceInline,
    ]
    save_as = True

    def data_files_list(self, obj):
        links_str = ""
        for file in obj.data_files.all():
            links_str = links_str + '<a href="{}">{}</a>, '.format(
                reverse("admin:battDB_experimentdatafile_change", args=(file.pk,)),
                str(file),
            )
        return mark_safe(links_str)

    data_files_list.short_description = "Data Files"


admin.site.register(Experiment, ExperimentAdmin)


class DeviceConfigInline(common.admin.TabularInline):
    model = DeviceConfigNode
    extra = 2


class DeviceConfigAdmin(BaseAdmin):
    save_as = True
    inlines = (DeviceConfigInline,)


admin.site.register(
    [
        DeviceConfig,
    ],
    DeviceConfigAdmin,
)


class DeviceDataInline(common.admin.TabularInline):
    model = DataColumn
    extra = 0


class DataFileInline(admin.StackedInline):
    readonly_fields = ["size", "local_date", "exists", "hash"]
    max_num = 1
    model = UploadedFile
    verbose_name_plural = "File Upload"


class DataRangeInline(common.admin.TabularInline):
    model = DataRange
    extra = 0
    exclude = ["attributes"]
    readonly_fields = ["size", "columns", "get_graph_link"]

    def size(self, obj):
        if obj.ts_data is not None and obj.ts_data[0] is not None:
            return "%dx%d" % (len(obj.ts_data), len(obj.ts_data[0]))
        else:
            return "N/A"

    size.short_description = "Rows x Cols"

    def get_graph_link(self, obj):
        if obj.ts_data is not None:
            return mark_safe(
                u"""
            <button type="button"> <a href="%s">%s</a> </button>
            """
                % ("/foo", "PLOT")
            )
        else:
            return "N/A"

    get_graph_link.short_description = "Graph"

    def columns(self, obj):
        return str(obj.ts_headers)


class DataAdmin(BaseAdmin):
    """
    FIXME: This class exhibits an n+1 query antipattern. For each row returned,
        2 additional queries are fired.
        This should be done with a JOIN instead.
    """

    inlines = [
        DataFileInline,
        DeviceDataInline,
        DataRangeInline,
    ]
    list_display = [
        "__str__",
        "user_owner",
        "get_file_link",
        "get_experiment_link",
        "file_data",
        "parsed_data",
        "created_on",
        "status",
    ]
    list_filter = ["experiment"] + BaseAdmin.list_filter
    readonly_fields = BaseAdmin.readonly_fields + [
        "is_parsed",
        "get_experiment_link",
        "file_hash",
        "file_columns",
        "num_ranges",
    ]

    def file_data(self, obj):
        return "%dx%d" % (obj.file_rows(), len(obj.file_columns()))

    file_data.short_description = "File RxC"

    def parsed_data(self, obj):
        parsed = len(obj.parsed_columns())
        missing = len(obj.missing_columns())
        return "%d/%d: %s" % (parsed, parsed + missing, obj.parsed_columns())

    parsed_data.short_description = "Imported Cols"

    # FIXME: This now breaks because parser is a string.
    def show_parser(self, obj):
        if hasattr(obj, "use_parser") and obj.use_parser is not None:
            return mark_safe(
                '<a href="{}">{}</a>'.format(
                    reverse("admin:battDB_parser_change", args=(obj.use_parser.pk,)),
                    str(obj.use_parser),
                )
            )
        else:
            return "N/A"

    show_parser.short_description = "Parser Config"

    def get_experiment_link(self, obj):
        if hasattr(obj, "experiment") and obj.experiment is not None:
            return mark_safe(
                '<a href="{}">{}</a>'.format(
                    reverse(
                        "admin:battDB_experiment_change", args=(obj.experiment.pk,)
                    ),
                    str(obj.experiment),
                )
            )
        else:
            return "N/A"

    get_experiment_link.short_description = "Experiment"

    def get_file_link(self, obj):
        if hasattr(obj, "raw_data_file") and obj.raw_data_file is not None:
            return mark_safe(
                u"""
            <button type="button"> <a href="%s">\u2193%s</a> </button>
            """
                % (obj.raw_data_file.file.url, obj.raw_data_file.size())
            )
        else:
            return "N/A"

    get_file_link.short_description = "View RAW"


admin.site.register([ExperimentDataFile], DataAdmin)


admin.site.register(
    [
        Equipment,
    ],
    BaseAdmin,
)


class FolderAdmin(mptt.admin.DraggableMPTTAdmin, BaseAdmin):
    pass


class ParserSignalInline(common.admin.TabularInline):
    model = SignalType
    extra = 1
    ordering = ("order",)


class ParserAdmin(BaseAdmin):
    inlines = (ParserSignalInline,)
    save_as = True


admin.site.register(Parser, ParserAdmin)
