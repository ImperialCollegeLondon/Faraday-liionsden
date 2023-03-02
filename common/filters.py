from django.contrib.auth import get_user_model
from django.db import models
from django_filters import CharFilter, FilterSet
from django_filters.filters import ModelChoiceFilter

User = get_user_model()


def not_anonymous_user(request):
    """
    Return a queryset of Users with the AnonymousUser explicilty removed.
    """
    if request is None:
        return User.objects.none()
    user_queryset = User.objects.exclude(username="AnonymousUser")
    return user_queryset


class BaseFilter(FilterSet):
    """
    Base class for common filter settings
    """

    # Don't show the AnonymousUser in the user_owner filter
    user_owner = ModelChoiceFilter(queryset=not_anonymous_user)

    class Meta:
        # Allow filtering on partial matches for charfield
        filter_overrides = {
            models.CharField: {
                "filter_class": CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            },
            models.TextField: {
                "filter_class": CharFilter,
                "extra": lambda f: {
                    "lookup_expr": "icontains",
                },
            },
        }
