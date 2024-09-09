from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag()
def model_desc(obj):
    if obj.__doc__:
        return mark_safe(f"<p>{obj.__doc__}</p>")
    return ""
