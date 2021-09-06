from django.contrib import admin

from common.admin import BaseAdmin

from . import models as cmodels

from guardian.admin import GuardedModelAdmin


class MaterialCompositionInline(admin.TabularInline):
    model = cmodels.CompositionPart
    readonly_fields = ["percentage"]
    extra = 0


class DataParameterInline(admin.TabularInline):
    model = cmodels.DataParameter
    extra = 1


class MaterialAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["type", "polymer"]
    list_filter = BaseAdmin.list_filter + ["type"]
    inlines = (MaterialCompositionInline,)


class MethodAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["type"]
    list_filter = BaseAdmin.list_filter + ["type"]


class DataAdmin(BaseAdmin):
    inlines = (DataParameterInline,)


class UnitAdmin(admin.ModelAdmin):
    list_display = ["__str__", "quantityName", "unitName", "is_SI_unit"]
    list_filter = ["is_SI_unit"]


class CompoundAdmin(GuardedModelAdmin):
    list_display = ["__str__"]


admin.site.register(cmodels.QuantityUnit, UnitAdmin)
admin.site.register(cmodels.Data, DataAdmin)
admin.site.register(cmodels.Material, MaterialAdmin)
admin.site.register(cmodels.Parameter, BaseAdmin)
admin.site.register(cmodels.Method, MethodAdmin)
admin.site.register(cmodels.Compound, CompoundAdmin)
