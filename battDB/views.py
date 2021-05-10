import matplotlib.pyplot as plt
import mpld3
import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataRange, Experiment, ExperimentDataFile, UploadedFile
from .serializers import (
    DataFileSerializer,
    DataRangeSerializer,
    ExperimentSerializer,
    FileHashSerializer,
    GeneralSerializer,
    NewDataFileSerializer,
)

np.random.seed(9615)


class AllExperimentsView(ListView):
    model = Experiment
    template_name = "generic_list.html"


class ExperimentView(DetailView):
    model = Experiment
    template_name = "experiment.html"


max_points = 1024


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
    return redirect("/exps")


def plotData(request):
    """Example of plotting data with mpld3.

    TODO: Remove in the future
    """
    # generate df
    N = 100
    df = pd.DataFrame(
        (0.1 * (np.random.random((N, 5)) - 0.5)).cumsum(0),
        columns=["a", "b", "c", "d", "e"],
    )

    # plot line + confidence interval
    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)

    for key, val in df.iteritems():
        (l,) = ax.plot(val.index, val.values, label=key)
        ax.fill_between(
            val.index,
            val.values * 0.5,
            val.values * 1.5,
            color=l.get_color(),
            alpha=0.4,
        )

    # define interactive legend
    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    interactive_legend = mpld3.plugins.InteractiveLegendPlugin(
        zip(handles, ax.collections),
        labels,
        alpha_unsel=0.5,
        alpha_over=1.5,
        start_visible=True,
    )
    mpld3.plugins.connect(fig, interactive_legend)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Interactive legend", size=20)
    g = mpld3.fig_to_html(fig, template_type="simple")
    return HttpResponse(g)


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
