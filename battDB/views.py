from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView, UpdateView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.tables import Table
from django_tables2.views import SingleTableMixin
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

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
    NewExperimentForm,
    NewProtocolForm,
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
    BatchDevicesTable,
    BatchTable,
    DeviceSpecificationTable,
    EquipmentTable,
    ExperimentTable,
)

### CREATE/ADD VIEWS ###


class NewDataView(FormView):
    """
    Template for view for creating new entries of various models.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            # Do other stuff before saving here
            obj.user_owner = request.user
            if form.is_public():
                obj.status = "public"
            else:
                obj.status = "private"
            obj.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


class NewDataViewInline(FormView):
    """
    Template for view for creating entries that includes an inline
    form for e.g. adding child objects, related objects etc.
    """

    success_message = "New data added successfully."
    failure_message = "Cannot add data. Invalid information."
    inline_key = None  # Key for which an inline form is needed
    formset = None  # Formset specifying the fields in the inline form

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(NewDataViewInline, self).get_context_data(**kwargs)
        if self.request.POST:
            data[self.inline_key] = self.formset(self.request.POST)
        else:
            data[self.inline_key] = self.formset()
        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = self.get_context_data()
        parameters = context[self.inline_key]
        if form.is_valid():
            # Save experiment incluing setting user owner and status
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.user_owner = request.user
                if form.is_public():
                    obj.status = "public"
                else:
                    obj.status = "private"
                self.object = form.save()
            # Save individual parameters from inline form
            if parameters.is_valid():
                parameters.instance = self.object
                parameters.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, context)


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
    """
    Unique view for adding an experiment with inline addition of devices.
    """

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


class NewProtocolView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_method"
    template_name = "create_protocol.html"
    form_class = NewProtocolForm
    success_url = "/battDB/new_protocol/"
    success_message = "New protocol created successfully."
    failure_message = "Could not save new protocol. Invalid information."


class UpdateBatchView(UpdateView):
    model = Batch
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_url = "/battDB/batches/"
    success_message = "Batch updated successfully."
    failure_message = "Could not update batch. Invalid information."

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = self.get_object()
            # Do other stuff before saving here
            # TODO think about logic for making public
            if form.is_public():
                obj.status = "public"
            else:
                obj.status = "private"
            obj.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


def index(request):
    return redirect("/")


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


### SEARCH/LIST/TABLE VIEWS ###
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
