from django.shortcuts import redirect
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from common.views import (
    MarkAsDeletedView,
    NewDataView,
    NewDataViewInline,
    UpdateDataInlineView,
    UpdateDataView,
)

from .filters import (
    BatchFilter,
    DeviceSpecificationFilter,
    EquipmentFilter,
    ExperimentFilter,
)
from .forms import (
    DeviceParameterFormSet,
    ExperimentDeviceFormSet,
    NewBatchForm,
    NewDeviceForm,
    NewEquipmentForm,
    NewExperimentDataFileForm,
    NewExperimentForm,
    NewProtocolForm,
    UploadDataFileFormset,
)
from .models import (
    Batch,
    DataRange,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    UploadedFile,
)
from .serializers import (
    DataFileSerializer,
    DataRangeSerializer,
    ExperimentSerializer,
    FileHashSerializer,
    GeneralSerializer,
    NewDataFileSerializer,
)
from .tables import (
    BatchTable,
    DeviceSpecificationTable,
    EquipmentTable,
    ExperimentTable,
)


def index(request):
    return redirect("/")


######################## CREATE, ADD, DELETE VIEWS #########################
class NewDeviceView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_url = "/battDB/new_device/"
    success_message = "New device specification created successfully."
    failure_message = "Could not save new device. Invalid information."
    inline_key = "parameters"
    formset = DeviceParameterFormSet


class NewExperimentView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_experiment"
    model = Experiment
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_url = "/battDB/new_experiment"
    success_message = "New experiment created successfully."
    failure_message = "Could not save new experiment. Invalid information."
    inline_key = "devices"
    formset = ExperimentDeviceFormSet


class NewEquipmentView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_url = "/battDB/new_equipment/"
    success_message = "New equipment created successfully."
    failure_message = "Could not save new equipment. Invalid information."


class NewBatchView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_url = "/battDB/new_batch/"
    success_message = "New batch created successfully."
    failure_message = "Could not save new batch. Invalid information."


class NewDataFileView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_experimentdatafile"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentDataFileForm
    success_url = "/battDB/new_edf/"
    success_message = "New data_file added successfully."
    failure_message = "Could not add new data file. Invalid information."
    inline_key = "raw_data_file"
    formset = UploadDataFileFormset


class NewProtocolView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_method"
    template_name = "create_protocol.html"
    form_class = NewProtocolForm
    success_url = "/battDB/new_protocol/"
    success_message = "New protocol created successfully."
    failure_message = "Could not save new protocol. Invalid information."


class UpdateDeviceView(PermissionRequiredMixin, UpdateDataInlineView):
    model = DeviceSpecification
    permission_required = "battDB.change_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_url = "/battDB/devices/"
    success_message = "Device specification updated successfully."
    failure_message = "Could not update Device specification. Invalid information."
    inline_key = "parameters"
    formset = DeviceParameterFormSet


class UpdateExperimentView(PermissionRequiredMixin, UpdateDataInlineView):
    model = Experiment
    permission_required = "battDB.change_experiment"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_url = "/battDB/exps/"
    success_message = "Experiment updated successfully."
    failure_message = "Could not update experiment. Invalid information."
    inline_key = "devices"
    formset = ExperimentDeviceFormSet


class UpdateEquipmentView(PermissionRequiredMixin, UpdateDataView):
    model = Equipment
    permission_required = "battDB.change_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_url = "/battDB/equipment/"
    success_message = "Equipment updated successfully."
    failure_message = "Could not update Equipment. Invalid information."


class UpdateBatchView(PermissionRequiredMixin, UpdateDataView):
    model = Batch
    permission_required = "battDB.change_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_url = "/battDB/batches/"
    success_message = "Batch updated successfully."
    failure_message = "Could not update batch. Invalid information."


# TODO: UpdateDataFileView


class DeleteDeviceView(PermissionRequiredMixin, MarkAsDeletedView):
    model = DeviceSpecification
    permission_required = "battDB.change_devicespecification"
    success_url = "/battDB/devices/"
    template_name = "delete_generic.html"
    success_message = "Device Specification deleted successfully."


class DeleteExperimentView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Experiment
    permission_required = "battDB.change_experiment"
    success_url = "/battDB/exps/"
    template_name = "delete_generic.html"
    success_message = "Experiment deleted successfully."


class DeleteEquipmentView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Equipment
    permission_required = "battDB.change_equipment"
    success_url = "/battDB/equipment/"
    template_name = "delete_generic.html"
    success_message = "Equipment deleted successfully."


class DeleteBatchView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Batch
    permission_required = "battDB.change_batch"
    success_url = "/battDB/batches/"
    template_name = "delete_generic.html"
    success_message = "Batch deleted successfully."


class DeleteDataFileView(PermissionRequiredMixin, MarkAsDeletedView):
    model = ExperimentDataFile
    permission_required = "battDB.change_experimentdatafile"
    success_url = "/battDB/exps/"
    template_name = "delete_generic.html"
    success_message = "Data file deleted successfully."


#################### DETAIL, LIST, TABLE VIEWS #########################
class ExperimentTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiments_table.html"
    filterset_class = ExperimentFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_experiment"


class BatchTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Batch
    table_class = BatchTable
    template_name = "batches_table.html"
    filterset_class = BatchFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_batch"


class DeviceSpecificationTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = DeviceSpecification
    table_class = DeviceSpecificationTable
    template_name = "device_specifications_table.html"
    filterset_class = DeviceSpecificationFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_devicespecification"


class EquipmentTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = Equipment
    table_class = EquipmentTable
    template_name = "equipment_table.html"
    filterset_class = EquipmentFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_equipment"


class ExperimentView(PermissionRequiredMixin, DetailView):
    model = Experiment
    template_name = "experiment.html"
    permission_required = "battDB.view_experiment"


class DeviceSpecificationView(PermissionRequiredMixin, DetailView):
    model = DeviceSpecification
    template_name = "device_specification.html"
    permission_required = "battDB.view_devicespecification"


class BatchView(PermissionRequiredMixin, DetailView):
    model = Batch
    template_name = "batch.html"
    permission_required = "battDB.view_batch"


class EquipmentView(PermissionRequiredMixin, DetailView):
    model = Equipment
    template_name = "equipment.html"
    permission_required = "battDB.view_equipment"


### API VIEWS ###
class ExperimentAPIView(APIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentAPIListView(ListAPIView):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()


class DataRangeAPIView(ListAPIView):
    serializer_class = DataRangeSerializer
    queryset = DataRange.objects.all()


class AllFileHashesAPIView(ListAPIView):
    """Returns hashes and sizes of all files belonging to current user."""

    model = UploadedFile
    serializer_class = FileHashSerializer

    def get_queryset(self):
        return UploadedFile.objects.all()  # filter(user_owner=self.request.user)


class DataFileListAPIView(ListAPIView):
    serializer_class = DataFileSerializer

    def get_queryset(self):
        return ExperimentDataFile.objects.filter(
            user_owner=self.request.user, experiment=self.request.GET.get("exp")
        )


class DataFileCreateAPIView(CreateAPIView):
    serializer_class = NewDataFileSerializer


class GeneralViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        model = self.kwargs.get("model")
        return model.objects.filter(user_owner=self.request.user)

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.kwargs.get("model")
        return GeneralSerializer


class UploadFileView(GenericAPIView):
    queryset = UploadedFile.objects.all()
    parser_classes = (FileUploadParser,)
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, filename, **kwargs):
        if "file" not in request.data:
            raise ParseError("Empty content")

        f = request.data["file"]
        obj = UploadedFile()
        obj.file.save(filename, f, save=True)
        obj.user_owner = request.user
        obj.clean()
        obj.save()
        response_data = FileHashSerializer(obj).data
        return Response(response_data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
