from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import ExperimentForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ExperimentsView(ListView):
    model = Experiment
    template_name = 'experiments.html'


class CreateExperimentView(LoginRequiredMixin, CreateView):
    model = Experiment
    form_class = ExperimentForm
    template_name = 'create_experiment.html'
    success_url = reverse_lazy('Experiments')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def viewdata(request):
    return HttpResponse("<h3>View data</h3>")

def uploaddata(request):
    return HttpResponse("<h3>Upload data</h3>")




