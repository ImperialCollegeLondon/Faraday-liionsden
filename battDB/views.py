from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.edit import FormView
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import NewDeviceForm, NewEquipmentForm
from .models import DataRange, Experiment, ExperimentDataFile, UploadedFile
from .serializers import (
    DataFileSerializer,
    DataRangeSerializer,
    ExperimentSerializer,
    FileHashSerializer,
    GeneralSerializer,
    NewDataFileSerializer,
)


class AllExperimentsView(ListView):
    model = Experiment
    template_name = "generic_list.html"


class ExperimentView(DetailView):
    model = Experiment
    template_name = "experiment.html"


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
    template_name = "upload_device.html"
    form_class = NewDeviceForm
    success_url = "/battDB/new_device/"
    success_message = "New device specification created successfully."
    failure_message = "Could not save new device. Invalid information."


class NewEquipmentView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_equipment"
    template_name = "upload_equipment.html"
    form_class = NewEquipmentForm
    success_url = "/battDB/new_equipment/"
    success_message = "New equipment created successfully."
    failure_message = "Could not save new equipment. Invalid information."


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """A view that renders a template.

    This view will also pass into the context any keyword arguments passed by the url
    conf.

    https://stackoverflow.com/questions/18232851/
     django-passing-variables-to-templates-from-class-based-views
    """

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


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
