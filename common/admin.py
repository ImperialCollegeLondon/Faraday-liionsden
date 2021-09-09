import django.forms
import mptt
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.db import models

from . import models as cmodels

admin.site.site_header = "The Faraday Institution - Liionsden Electrochemistry Database"
admin.site.site_title = "Liionsden Admin"
admin.site.index_title = "Liionsden Admin"

class CustomUserAdmin(UserAdmin):
    """# A slightly more restrictive user admin page."""
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set() 
        
        # Prevent changing permissions without using groups
        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }
        # Prevent changing users own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

admin.site.register(User, CustomUserAdmin)

class ChangeFormMixin:
    """Customize the form used in the admin site when editing/adding objects."""

    def get_changeform_initial_data(self, request):
        get_data = super(ChangeFormMixin, self).get_changeform_initial_data(request)
        get_data["user_owner"] = request.user.pk
        return get_data

    show_change_link = True
    formfield_overrides = {
        models.TextField: {
            "widget": django.forms.Textarea(
                attrs={"rows": 3, "cols": 20, "style": "height: 3em;"}
            )
        },
        models.CharField: {
            "widget": django.forms.widgets.Input(
                attrs={
                    "cols": 20,
                }
            )
        },
        models.JSONField: {
            "widget": django.forms.Textarea(
                attrs={"rows": 3, "cols": 40, "style": "height: 3em;"}
            )
        },
    }


class BaseAdmin(ChangeFormMixin, admin.ModelAdmin):
    list_display_extra = ["user_owner", "status", "created_on", "modified_on"]
    list_display = ["__str__"] + list_display_extra
    list_filter = ["user_owner", "status"]
    readonly_fields = ["created_on", "modified_on", "slug"]
    generic_fields = {"name", "notes", "status", "user_owner", "attributes"}


class TabularInline(ChangeFormMixin, admin.TabularInline):
    pass


class CompositeBaseInLine(TabularInline):
    fk_name = "parent"
    extra = 1
    verbose_name_plural = "Child Objects"


class HasMPTTAdmin(mptt.admin.DraggableMPTTAdmin, BaseAdmin):
    inlines = [
        CompositeBaseInLine,
    ]
    readonly_fields = BaseAdmin.readonly_fields + ["metadata"]


class OrgAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "manager",
        "website",
        "is_research",
        "is_publisher",
        "is_mfg_cells",
        "is_mfg_equip",
    ]
    list_filter = ["is_research", "is_publisher", "is_mfg_cells", "is_mfg_equip"]


admin.site.register(
    [
        cmodels.Org,
    ],
    OrgAdmin,
)


class PaperAdmin(BaseAdmin):
    list_display = ["title", "DOI", "year", "has_pdf"]
    list_filter = ["year", "publisher", "authors"]


admin.site.register(
    [
        cmodels.Paper,
    ],
    PaperAdmin,
)


class PersonAdmin(admin.ModelAdmin):
    list_display = ["longName", "shortName", "user", "org"]
    list_filter = ["org"]
    readonly_fields = ["user_firstname"]


admin.site.register(
    [
        cmodels.Person,
    ],
    PersonAdmin,
)
