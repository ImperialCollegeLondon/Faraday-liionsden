import django_tables2 as tables2
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import MultiTableMixin, SingleTableMixin
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
    ParserFilter,
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
    Parser,
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
    ExperimentDataTable,
    ExperimentTable,
    ParserTable,
)


def index(request):
    return redirect("/")


######################## CREATE, ADD, DELETE VIEWS #########################
class NewDeviceView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_message = "New device specification created successfully."
    failure_message = "Could not save new device. Invalid information."
    inline_key = "parameters"
    formset = DeviceParameterFormSet


class NewExperimentView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_experiment"
    model = Experiment
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_message = "New experiment created successfully."
    failure_message = "Could not save new experiment. Invalid information."
    inline_key = "devices"
    formset = ExperimentDeviceFormSet


class NewEquipmentView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_message = "New equipment created successfully."
    failure_message = "Could not save new equipment. Invalid information."


class NewBatchView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_message = "New batch created successfully."
    failure_message = "Could not save new batch. Invalid information."


class NewDataFileView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.change_experiment"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentDataFileForm
    success_message = "New data_file added successfully."
    failure_message = "Could not add new data file. Invalid information."
    inline_key = "raw_data_file"
    formset = UploadDataFileFormset

    def get_permission_object(self, *args, **kwargs):
        # Only allowed by users who can change current Experiment
        return Experiment.objects.get(pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        """
        Unique post method for data files to handle a) setting user_owner and
        status of uploaded file and b) parsing pk of associated experiment.
        """
        form = self.form_class(request.POST, request.FILES)
        context = self.get_context_data()
        parameters = context[self.inline_key]
        if form.is_valid():
            # Save instance incluing setting user owner and status
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.user_owner = request.user
                # Set experiment PK based on URL
                obj.experiment = Experiment.objects.get(pk=self.kwargs.get("pk"))
                if form.is_public():
                    obj.status = "public"
                else:
                    obj.status = "private"
                self.object = form.save()
            # Save individual parameters from inline form
            if parameters.is_valid():
                parameters.instance = self.object
                # Handle uploaded files in formsets slightly differently to usual
                parameters[0].instance.user_owner = obj.user_owner
                parameters[0].instance.status = obj.status
                if parameters[0].instance.use_parser:
                    parameters[0].instance.parse = True
                parameters.save()
                form.instance.full_clean()

            messages.success(request, self.success_message)
            return redirect("/battDB/exps/{}".format(self.kwargs.get("pk")))
        messages.error(request, self.failure_message)
        return render(request, self.template_name, context)


class NewProtocolView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_method"
    template_name = "create_protocol.html"
    form_class = NewProtocolForm
    success_message = "New protocol created successfully."
    failure_message = "Could not save new protocol. Invalid information."


class UpdateDeviceView(PermissionRequiredMixin, UpdateDataInlineView):
    model = DeviceSpecification
    permission_required = "battDB.change_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_message = "Device specification updated successfully."
    failure_message = "Could not update Device specification. Invalid information."
    inline_key = "parameters"
    formset = DeviceParameterFormSet


class UpdateExperimentView(PermissionRequiredMixin, UpdateDataInlineView):
    model = Experiment
    permission_required = "battDB.change_experiment"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_message = "Experiment updated successfully."
    failure_message = "Could not update experiment. Invalid information."
    inline_key = "devices"
    formset = ExperimentDeviceFormSet


class UpdateEquipmentView(PermissionRequiredMixin, UpdateDataView):
    model = Equipment
    permission_required = "battDB.change_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_message = "Equipment updated successfully."
    failure_message = "Could not update Equipment. Invalid information."


class UpdateBatchView(PermissionRequiredMixin, UpdateDataView):
    model = Batch
    permission_required = "battDB.change_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
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
    template_name = "delete_generic.html"
    success_message = "Data file deleted successfully."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = "deleted"
        self.object.save()
        messages.success(request, self.success_message)
        return redirect(self.object.experiment)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


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


class ParserTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Parser
    table_class = ParserTable
    template_name = "parser_table.html"
    filterset_class = ParserFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_parser"


class ExperimentView(PermissionRequiredMixin, MultiTableMixin, DetailView):
    model = Experiment
    template_name = "experiment.html"
    permission_required = "battDB.view_experiment"
    table_class = ExperimentDataTable

    def get_tables(self):
        """
        Overriding to include all columns dynamically.
        """
        data = self.get_tables_data()
        data_files = self.object.data_files.all()

        tables = []
        for data_set, data_file in zip(data, data_files):
            tables.append(
                self.table_class(
                    data_set,
                    extra_columns=[(i, tables2.Column()) for i in data_file.ts_headers],
                )
            )

        return tables

    def get_tables_data(self):
        """
        Overriding to get top 20 rows of data displayed.
        """
        data_files = self.object.data_files.all()
        data_previews = []
        for data_file in data_files:
            initial_data = data_file.ts_data[:20]
            data_headers = data_file.ts_headers
            data_preview = []
            for i in initial_data:
                data_preview.append(
                    {
                        header: round(value, 2)
                        for (header, value) in zip(data_headers, i)
                    }
                )

            data_previews.append(data_preview)
        return data_previews


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


class ParserView(PermissionRequiredMixin, DetailView):
    model = Parser
    template_name = "parser.html"
    permission_required = "battDB.view_parser"


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
