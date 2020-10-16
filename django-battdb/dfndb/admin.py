from django.contrib import admin

# Register your models here.

from .models import *
from common.admin import BaseAdmin


class MaterialCompositionInline(admin.TabularInline):
    model = CompositionPart
    extra = 2


class DataParameterInline(admin.TabularInline):
    model = DataParameter
    extra = 2


class MaterialAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ['type', 'polymer']
    list_filter = BaseAdmin.list_filter + ['type']
    inlines = (MaterialCompositionInline,)


class MethodAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ['type']
    list_filter = BaseAdmin.list_filter + ['type']


class DataAdmin(BaseAdmin):
    inlines = (DataParameterInline,)


class UnitAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'quantityName', 'unitName', 'is_SI_unit']
    list_filter = ['is_SI_unit']


class CompoundAdmin(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(QuantityUnit, UnitAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Parameter, BaseAdmin)
admin.site.register(Method, MethodAdmin)
admin.site.register(Compound, CompoundAdmin)
