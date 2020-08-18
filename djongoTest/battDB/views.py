from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import *
from .forms import ExperimentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ProcessFormView
from galvanalyser.harvester.parsers.biologic_parser import BiologicCSVnTSVParser
from .serializers import DataSerializer

# Create your views here.


class ExperimentsView(ListView):
    model = Experiment
    template_name = 'experiments.html'

class ExperimentView(ListView):
    model = Experiment
    template_name='experiment.html'
    
    def get_object(self):  # simple unique ID e.g. /exp/94
       if('pk' in self.kwargs):
            return get_object_or_404(Experiment, pk=self.kwargs['pk'])
       else:  # wanted to have slugs like /exp/PolymerElectrolyteComposition-bloggs-2020-08-22 but this doesn't seem to work..
           return get_object_or_404(
            Experiment,
            #slug=self.kwargs['slug']
            #slug=str(self.kwargs['name']) + "/" + str(self.kwargs['owner']) + "/" + str(self.kwargs['date'])
            name=self.kwargs['name'],
            owner=self.kwargs['owner'],
            date=self.kwargs['date']
           )

# not used - using ExperimentDataFile.post_save instead
class ProcessExperimentView(LoginRequiredMixin, DetailView, ProcessFormView):
    model = Experiment
    template_name='experiment.html'

# TODO: Make a proper view with graphs n stuff
class ExperimentDataView(DetailView):
    model = ExperimentDataFile
    template_name='experimentData.html'


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
    #return HttpResponse("<h1>Hello, world.</h1>")

def viewdata(request):
    return HttpResponse("<h3>View data</h3>")

def uploaddata(request):
    return HttpResponse("<h3>Upload data</h3>")

def get_data(request):
    data = DataRange.objects.all()
    if request.method == 'GET':
        serializer = DataSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


