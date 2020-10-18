from django.contrib import admin
from common.admin import BaseAdmin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import *




admin.site.register([
    Experiment, TestProtocol, Equipment, EquipmentType,
    CellConfig,  ExperimentDataFile, DataRange], BaseAdmin)


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
