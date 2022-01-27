from django.db import models
from django_filters import CharFilter, FilterSet


class BaseFilter(FilterSet):
    """
    Base class for common filter settings
    """

    class Meta:
        # Allow filtering on partial matches for charfield
        filter_overrides = {
            models.CharField: {
                "filter_class": CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            }
        }
