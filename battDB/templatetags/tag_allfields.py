# https://stackoverflow.com/questions/2217478/django-templates-loop-through-and-print-all-available-properties-of-an-object

from django import template

register = template.Library()


@register.filter
def get_fields(obj):
    out = []
    for field in obj._meta.fields:
        if field.is_relation:
            out.append((field.name, (getattr(obj, field.name))))
        else:
            out.append((field.name, field.value_to_string(obj)))
    return out
