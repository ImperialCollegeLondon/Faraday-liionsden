from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView

from .models import *
from .serializers import *

# Create your views here.


class DataListView(ListView):
    model = Data
    # template_name = 'lazycrud/object_list.html'

    page_title = "Data list"
    # fields = '__all__'
    create_url = reverse_lazy("dfndb:cdata")
    create_label = "Create new Data"


def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")


class ParametersAPIView(ListCreateAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
