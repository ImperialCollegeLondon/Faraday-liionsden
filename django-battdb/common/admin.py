from django.contrib import admin
from django.contrib.postgres.fields import JSONField
#from jsoneditor.forms import JSONEditor

from .models import *


# admin.site.register([
#    Paper,
#    ], admin.ModelAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = (["username", "first_name", "last_name", "email", "org"])
    list_filter = (["org"])


# admin.site.register([
#  User,
# ], PersonAdmin)


class BaseAdmin(admin.ModelAdmin):
    list_display = (["name", "user_owner", "status", "created_on", "modified_on"])
    list_filter = (["status"])
    readonly_fields = ['created_on', 'modified_on']

    # can't group fields, because it hides all other fields.
    # fieldsets = (
    # ('Model Fields', {
    # 'fields': ([])
    # }),
    # ('Generic Object fields', {
    # 'fields': ('name', 'notes', 'status', 'user_owner', 'attributes')
    # }),
    # )
    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['user_owner'] = request.user.pk
        return get_data


#  formfield_overrides = {
#     JSONField:{ 'widget':JSONEditor },
# }


class OrgAdmin(admin.ModelAdmin):
    list_display = (["name", "manager", "website", "is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"])
    list_filter = (["is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"])


admin.site.register([
   Org,
   ], OrgAdmin)


class PaperAuthorInline(admin.TabularInline):
    model = PaperAuthor
    extra = 2


class PaperAdmin(BaseAdmin):
    inlines = (PaperAuthorInline,)
    list_display = (["title", "DOI", "year", "has_pdf"])
    list_filter = (["year", "publisher", "authors"])
    readonly_fields = ['created_on', 'tag']


admin.site.register([
    Paper,
], PaperAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = (["name", "user", "org"])
    list_filter = (["org"])


admin.site.register([
    Person,
], PersonAdmin)
