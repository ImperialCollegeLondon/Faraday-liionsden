# https://blog.confirm.ch/accessing-models-verbose-names-django-templates/
from django import template

register = template.Library()


@register.simple_tag
def model_name(value):
    """
    Django template filter which returns the verbose name of a model.
    """
    if hasattr(value, "model"):
        value = value.model

    return value._meta.verbose_name.title()


@register.simple_tag
def model_name_plural(value):
    """
    Django template filter which returns the plural verbose name of a model.
    """
    if hasattr(value, "model"):
        value = value.model

    return value._meta.verbose_name_plural.title()


@register.simple_tag
def field_name(value, field):
    """
    Django template filter which returns the verbose name of an object's,
    model's or related manager's field.
    """
    if hasattr(value, "model"):
        value = value.model

    return value._meta.get_field(field).verbose_name.title()
