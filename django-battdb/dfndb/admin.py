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


class DataAdmin(BaseAdmin):
    inlines = (DataParameterInline,)


admin.site.register(Data, DataAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register([Method, Parameter], BaseAdmin)
admin.site.register([Compound, QuantityUnit], admin.ModelAdmin)
