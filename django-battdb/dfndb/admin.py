from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register([
    Paper,Compound,CompositionPart, Material, Method, QuantityUnit, Parameter, Data
    ], admin.ModelAdmin)
