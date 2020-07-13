from django.shortcuts import render
from django.http import HttpResponse
from battDB.models import Experiment

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def viewdata(request):
    return HttpResponse("<h3>View data</h3>")

def uploaddata(request):
    return HttpResponse("<h3>Upload data</h3>")




