from django_filters.filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from common.filters import BaseFilter

from .models import Batch, DeviceSpecification, Equipment, Experiment, Parser


class ExperimentFilter(BaseFilter):
    date = DateFromToRangeFilter(
        widget=RangeWidget(attrs={"type": "date"}), label="Date range"
    )

    class Meta(BaseFilter.Meta):
        model = Experiment
        fields = [
            "id",
            "name",
            "status",
            "user_owner",
            "user_owner__institution",
            "exp_type",
            "temperature",
            "c_rate",
            "thermal",
            "summary",
        ]

    # Modify init slightly to add custom label(s)
    def __init__(self, *args, **kwargs):
        super(ExperimentFilter, self).__init__(*args, **kwargs)
        self.filters["user_owner__institution"].label = "Institution"


class BatchFilter(BaseFilter):
    manufactured_on = DateFromToRangeFilter(
        widget=RangeWidget(attrs={"type": "manufactured_on"}), label="Date range"
    )

    class Meta(BaseFilter.Meta):
        model = Batch
        fields = [
            "id",
            "status",
            "user_owner",
            "manufacturer",
            "manufactured_on",
            "serialNo",
            "specification",
        ]


class DeviceSpecificationFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = DeviceSpecification
        fields = [
            "id",
            "name",
            "status",
            "user_owner",
            "device_type",
        ]

    # Modify init slightly to add custom label(s)
    def __init__(self, *args, **kwargs):
        super(DeviceSpecificationFilter, self).__init__(*args, **kwargs)
        self.filters["user_owner"].label = "Added by"


class EquipmentFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Equipment
        fields = [
            "id",
            "name",
            "user_owner",
            "institution",
            "serialNo",
            "status",
        ]


class ParserFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Parser
        fields = [
            "name",
            "status",
        ]
