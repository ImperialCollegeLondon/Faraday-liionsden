from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.edit import CreateView, FormView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ExperimentFilter
from .forms import (
    ExperimentDeviceFormSet,
    NewBatchForm,
    NewDeviceForm,
    NewEquipmentForm,
    NewExperimentForm,
    NewProtocolForm,
)
from .models import DataRange, Experiment, ExperimentDataFile, UploadedFile
from .serializers import (
    DataFileSerializer,
    DataRangeSerializer,
    ExperimentSerializer,
    FileHashSerializer,
    GeneralSerializer,
    NewDataFileSerializer,
)
from .tables import ExperimentTable

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
        form = self.form_class(request.POST)
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


class NewDeviceView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_devicespecification"
    template_name = "create_device.html"
    form_class = NewDeviceForm
    success_url = "/battDB/new_device/"
    success_message = "New device specification created successfully."
    failure_message = "Could not save new device. Invalid information."


class NewEquipmentView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_equipment"
    template_name = "create_equipment.html"
    form_class = NewEquipmentForm
    success_url = "/battDB/new_equipment/"
    success_message = "New equipment created successfully."
    failure_message = "Could not save new equipment. Invalid information."


class NewBatchView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_batch"
    template_name = "create_batch.html"
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


class NewExperimentView(PermissionRequiredMixin, FormView):
    """
    Unique view for adding an experiment with inline addition of devices.
    """

    permission_required = "battDB.add_experiment"
    model = Experiment
    template_name = "create_experiment.html"
    form_class = NewExperimentForm
    success_url = "/battDB/new_experiment"
    success_message = "New experiment created successfully."
    failure_message = "Could not save new experiment. Invalid information."

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post().
        """
        data = super(NewExperimentView, self).get_context_data(**kwargs)
        if self.request.POST:
            data["devices"] = ExperimentDeviceFormSet(self.request.POST)
        else:
            data["devices"] = ExperimentDeviceFormSet()
        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = self.get_context_data()
        devices = context["devices"]
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
            # Save individual devices from inline form
            if devices.is_valid():
                devices.instance = self.object
                devices.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, context)


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


class ExperimentTableView(SingleTableMixin, FilterView):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiments_table.html"
    filterset_class = ExperimentFilter


class ExperimentView(DetailView):
    model = Experiment
    template_name = "experiment.html"


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
