from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from jsoneditor.forms import JSONEditor


from .models import *

#admin.site.register([
#    Paper,
#    ], admin.ModelAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = (["username", "first_name", "last_name", "email", "org"])
    list_filter = (["org"])

#admin.site.register([
  #  User,
   # ], PersonAdmin)


class OrgAdmin(admin.ModelAdmin):
    list_display = (["name"])
    list_filter = (["name"])

#admin.site.register([
#    Org,
#    ], OrgAdmin)



class BaseAdmin(admin.ModelAdmin):
    list_display = (["name", "user_owner", "status","created_on"])
    list_filter = (["status", "user_owner"])
    #fieldsets = (
        #('Model Fields', {
            #'fields': ([])
        #}),
        #('Generic Object fields', {
            #'fields': ('name', 'notes', 'status', 'user_owner', 'attributes')
        #}),
    #)
    def get_changeform_initial_data(self, request):
        get_data = super().get_changeform_initial_data(request)
        get_data['user_owner'] = request.user.pk
        return get_data
  #  formfield_overrides = {
   #     JSONField:{ 'widget':JSONEditor },
    #}
        
        
class PaperAdmin(BaseAdmin):
    list_display = (["title", "DOI", "year","has_pdf"])
    list_filter = (["year", "org_owners"])

admin.site.register([
    Paper,
    ], PaperAdmin)
