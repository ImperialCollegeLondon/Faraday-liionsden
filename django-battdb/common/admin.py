from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register([
#    Paper,
#    ], admin.ModelAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = (["authUser", "firstName", "lastName", "email", "org"])
    list_filter = (["org"])

admin.site.register([
    Person,
    ], PersonAdmin)


class OrgAdmin(admin.ModelAdmin):
    list_display = (["name"])
    list_filter = (["name"])

admin.site.register([
    Org,
    ], OrgAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display = (["title", "DOI", "year",])
    list_filter = (["year", "org_owners"])

admin.site.register([
    Paper,
    ], PaperAdmin)


