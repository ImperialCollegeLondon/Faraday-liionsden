from common.filters import BaseFilter

from .models import Compound, Material


class CompoundFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Compound
        fields = ["id", "name", "formula"]
