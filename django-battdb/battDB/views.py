from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.urls import reverse_lazy
from .models import *
from .forms import ExperimentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ProcessFormView
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from .serializers import *
import matplotlib.pyplot as plt
import mpld3
import numpy as np
import pandas as pd

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView, GenericAPIView

np.random.seed(9615)


# Create your views here.


class ExperimentsView(ListView):
    model = Experiment
    template_name = 'generic_list.html'


class AllFilesView(ListView):
    model = ExperimentDataFile
    template_name = 'generic_list.html'


class AllRangesView(ListView):
    model = DataRange
    template_name = 'generic_list.html'


class ExperimentView(DetailView):
    model = Experiment
    template_name = 'experiment.html'

    # def get_object(self):  # simple unique ID e.g. /exp/94
    # if('pk' in self.kwargs):
    #        return get_object_or_404(ExperimentDataFile, experiment=self.kwargs['pk'])
    # else:  # wanted to have slugs like /exp/PolymerElectrolyteComposition-bloggs-2020-08-22 but this doesn't seem to work..
    #    return get_object_or_404(
    #     ExperimentDataFile,
    #     #slug=self.kwargs['slug']
    #     #slug=str(self.kwargs['name']) + "/" + str(self.kwargs['owner']) + "/" + str(self.kwargs['date'])
    #     name=self.kwargs['name'],
    #     owner=self.kwargs['owner'],
    #     date=self.kwargs['date']
    #    )


# not used - using ExperimentDataFile.post_save instead
# class ProcessExperimentView(LoginRequiredMixin, DetailView, ProcessFormView):
#    model = Experiment
#    template_name='experiment.html'

# https://mpld3.github.io/examples/interactive_legend.html

max_points = 1024


class ExperimentDataView(DetailView):
    model = ExperimentDataFile
    template_name = 'experimentData.html'

    def get_context_data(self, **kwargs):
        context = super(ExperimentDataView, self).get_context_data(**kwargs)
        columns = context['object'].data['columns']
        select_columns = ['Time', 'Ecell/V', 'I/mA']
        df1 = pd.DataFrame(context['object'].data['rows'], columns=columns)
        df = df1[select_columns]
        # df.set_index('Time')
        # fig,ax1=plt.subplots(figsize=(16,9))
        # ax2=ax1.twinx()
        # ax2.patch.set_alpha(0.0)
        # df.plot(x='Time', y='I/mA', color='red' ,ax=ax2)
        # df.plot(x='Time', y='Ecell/V', kind='line', color='blue', ax=ax1)
        labels = list(df.columns.values)

        plot_x = ('Time', 'Time/s')
        plot_y1 = ('Ecell/V', 'Cell Voltage/V')
        plot_y2 = ('I/mA', 'I/mA')

        fig, ax1 = plt.subplots(figsize=(20, 10))
        color1 = 'tab:red'
        color2 = 'tab:blue'
        ax1.set_xlabel(plot_x[1])
        ax1.set_ylabel(plot_y1[1], color=color1)
        ax1.plot(df[plot_x[0]], df[plot_y1[0]], color=color1)
        ax1.tick_params(axis='y', labelcolor=color1)
        # ax1.set_aspect('auto', adjustable='datalim')

        ax2 = ax1.twinx()
        ax2.patch.set_alpha(0.0)
        ax2.set_ylabel(plot_y2[1], color=color2)
        ax2.plot(df[plot_x[0]], df[plot_y2[0]], color=color2)
        ax2.tick_params(axis='y', labelcolor=color2)

        # for key, val in df.iteritems():
        #    if key not in ["Ecell/V", "I/mA"]:
        #       continue
        #    l, = ax1.plot(val.index, val.values, label=key)
        #    ax1.fill_between(val.index,
        #        val.values * .5, val.values * 1.5,
        #        color=l.get_color(), alpha=.4)

        # define interactive legend

        handles, labels = ax1.get_legend_handles_labels()  # return lines and labels
        # interactive_legend = mpld3.plugins.InteractiveLegendPlugin(zip(handles,
        #                 ax1.collections),
        #                 labels,
        #                 alpha_unsel=0.5,
        #                 alpha_over=1.5, 
        #                 start_visible=True)
        # mpld3.plugins.connect(fig, interactive_legend)

        ax1.set_title(str(context['object']), size=20)

        # define interactive tooltip
        # labels = [self.format_string.format(label=view.label)]
        # tooltip = mpld3.plugins.LineHTMLTooltip(labels,
        #                                  voffset=self.voffset, hoffset=self.hoffset,
        #                                  css=self.css)
        # mpld3.plugins.connect(fig, tooltip)

        # fig.tight_layout()
        # plt.show()

        g = mpld3.fig_to_html(fig, template_type="simple")
        context['cols'] = columns
        context['mplot'] = g
        pd.set_option('display.max_columns', 50)
        pd.set_option('display.width', 1000)
        context['dataHead'] = str(df1)
        return context


class ExperimentDataProcessView(UpdateView):
    model = ExperimentDataFile
    template_name = 'generic_object.html'


# https://stackoverflow.com/questions/18232851/django-passing-variables-to-templates-from-class-based-views
class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the url conf.
    """

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class DataRangeView(DetailView):
    model = DataRange
    template_name = 'dataRange.html'

    def get_context_data(self, **kwargs):
        context = super(DataRangeView, self).get_context_data(**kwargs)
        fig, ax = plt.subplots(figsize=(16, 9))
        plt.plot(context['object'].ts_data)
        g = mpld3.fig_to_html(fig, template_type="simple")
        context['mplot'] = g
        return context


class CreateExperimentView(LoginRequiredMixin, CreateView):
    model = Experiment
    form_class = ExperimentForm
    template_name = 'create_experiment.html'
    success_url = reverse_lazy('Experiments')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def index(request):
    return redirect('/exps')
    # return HttpResponse("<h1>Hello, world.</h1>")


# def viewdata(request):
#    return HttpResponse("<h3>View data</h3>")

# def uploaddata(request):
#    return HttpResponse("<h3>Upload data</h3>")

# def get_data(request):
#    data = DataRange.objects.all()
#    if request.method == 'GET':
#        serializer = DataSerializer(data, many=True)
#    return JsonResponse(serializer.data, safe=False)

def plotData(request):
    # generate df
    N = 100
    df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                      columns=['a', 'b', 'c', 'd', 'e'], )

    # plot line + confidence interval
    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3)

    for key, val in df.iteritems():
        l, = ax.plot(val.index, val.values, label=key)
        ax.fill_between(val.index,
                        val.values * .5, val.values * 1.5,
                        color=l.get_color(), alpha=.4)

    # define interactive legend

    handles, labels = ax.get_legend_handles_labels()  # return lines and labels
    interactive_legend = mpld3.plugins.InteractiveLegendPlugin(zip(handles,
                                                                   ax.collections),
                                                               labels,
                                                               alpha_unsel=0.5,
                                                               alpha_over=1.5,
                                                               start_visible=True)
    mpld3.plugins.connect(fig, interactive_legend)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Interactive legend', size=20)
    # fig,ax=plt.subplots(figsize=(16,9))
    # plt.plot([1,2,3,4]*4096)
    g = mpld3.fig_to_html(fig, template_type="simple")
    return HttpResponse(g)


class UploadFileView(GenericAPIView):
    queryset = RawDataFile.objects.all()
    parser_class = (FileUploadParser,)
    serializer_class = DataFileSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, format=None):
        if 'raw_data_file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['raw_data_file']
        obj = RawDataFile()
        obj.raw_data_file.save(f.name, f, save=True)
        obj.user_owner = request.user
        obj.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def options(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
