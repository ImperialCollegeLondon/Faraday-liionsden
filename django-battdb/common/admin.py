from django.contrib import admin
from django.contrib.postgres.fields import JSONField
# from jsoneditor.forms import JSONEditor

from .models import *
import mptt
import django.forms

from django.contrib.auth.models import Permission, ContentType

class PermissionsAdmin(admin.ModelAdmin):
    list_filter = ['content_type']

admin.site.register(Permission, PermissionsAdmin)
admin.site.register(ContentType)

admin.site.site_header = 'The Faraday Institution - Liionsden Electrochemistry Database'
admin.site.site_title = 'Liionsden Admin'
admin.site.index_title = 'Liionsden Admin'

# admin.site.register([
#    Paper,
#    ], admin.ModelAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = (["username", "first_name", "last_name", "email", "org"])
    list_filter = (["org"])


# admin.site.register([
#  User,
# ], PersonAdmin)

class ChangeformMixin():
    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['user_owner'] = request.user.pk
        return get_data


class BaseAdmin(ChangeformMixin, admin.ModelAdmin):
    list_display = (["__str__", "user_owner", "status", "created_on", "modified_on"])
    list_filter = (["status"])
    readonly_fields = ['created_on', 'modified_on', 'slug']
    generic_fields = {'name', 'notes', 'status', 'user_owner', 'attributes'}

    formfield_overrides = {
        models.TextField: {'widget': django.forms.Textarea(
                           attrs={'rows': 3,
                                  'cols': 40,
                                  'style': 'height: 3em;'})},
        models.JSONField: {'widget': django.forms.Textarea(
            attrs={'rows': 3,
                   'cols': 40,
                   'style': 'height: 3em;'})},
    }

    # this works, but it messes up field ordering due to conversion to sets
    # def get_fieldsets(self, request, obj=None):
    #     fs = super(BaseAdmin, self).get_fieldsets(request, obj)
    #     all_fields = set(fs[0][1]['fields'])
    #     new_fields = all_fields - BaseAdmin.generic_fields
    #     # reconstruct fieldsets
    #     fs = (('Generic Base Fields', {
    #         'fields': BaseAdmin.generic_fields
    #     }), ('Model Fields', {
    #         'fields': new_fields
    #     }), )
    #     return fs




class OrgAdmin(admin.ModelAdmin):
    list_display = (["name", "manager", "website", "is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"])
    list_filter = (["is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"])


admin.site.register([
    Org,
], OrgAdmin)


class PaperAdmin(BaseAdmin):
    list_display = ["title", "DOI", "year", "has_pdf"]
    list_filter = ["year", "publisher", "authors"]


admin.site.register([
    Paper,
], PaperAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ["longName", "shortName", "user", "org"]
    list_filter = ["org"]
    readonly_fields = ["user_firstname"]


admin.site.register([
    Person,
], PersonAdmin)


class TabularInLine(ChangeformMixin, admin.TabularInline):
    pass

class CompositeBaseInLine(TabularInLine):
    fk_name = "parent"
    verbose_name_plural = "Composition"
    extra = 1
    show_change_link = True
    verbose_name_plural = "Child Objects"
    formfield_overrides = {
        models.TextField: {'widget': django.forms.Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }

    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['user_owner'] = request.user.pk
        return get_data


class HasMPTTAdmin(mptt.admin.DraggableMPTTAdmin, BaseAdmin):
    inlines = [CompositeBaseInLine,]

#admin.site.register(Thing, ThingAdmin)