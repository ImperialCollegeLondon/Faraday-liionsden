from common.filters import BaseFilter

from .models import Component, Compound


class CompoundFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Compound
        fields = ["id", "name", "formula"]


class ComponentFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Component
        fields = ["id", "name", "type", "status"]
