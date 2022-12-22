from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from common.admin import BaseAdmin

from . import models as cmodels


class ComponentCompositionInline(admin.TabularInline):
    model = cmodels.CompositionPart
    readonly_fields = ["percentage"]
    extra = 0


class DataParameterInline(admin.TabularInline):
    model = cmodels.DataParameter
    extra = 1


class ComponentAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["type"]
    list_filter = BaseAdmin.list_filter + ["type"]
    inlines = (ComponentCompositionInline,)


class MethodAdmin(BaseAdmin, DynamicArrayMixin):
    list_display = BaseAdmin.list_display + ["type"]
    list_filter = BaseAdmin.list_filter + ["type"]


class DataAdmin(BaseAdmin):
    inlines = (DataParameterInline,)


class UnitAdmin(admin.ModelAdmin):
    list_display = ["__str__", "quantityName", "unitName", "is_SI_unit"]
    list_filter = ["is_SI_unit"]


class CompoundAdmin(admin.ModelAdmin):
    list_display = ["__str__"]


class ParameterAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["parameter_type"]
    list_filter = BaseAdmin.list_filter + ["parameter_type"]


admin.site.register(cmodels.QuantityUnit, UnitAdmin)
admin.site.register(cmodels.Data, DataAdmin)
admin.site.register(cmodels.Component, ComponentAdmin)
admin.site.register(cmodels.Parameter, ParameterAdmin)
admin.site.register(cmodels.Method, MethodAdmin)
admin.site.register(cmodels.Compound, CompoundAdmin)
