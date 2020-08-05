from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('viewData', views.viewdata, name='viewData'),
    path('uploadData', views.uploaddata, name='uploadData'),
    path('exps', ExperimentsView.as_view(), name='Experiments'),
    path('exp/<slug:owner>/<slug:name>/<slug:date>', ExperimentView.as_view(), name='Experiment'),
    #path('exp/<slug:slug>', ExperimentView.as_view(), name='Experiment'),
    path('exp/<int:pk>', ExperimentView.as_view(), name='Experiment'),
    path('create_exp/', CreateExperimentView.as_view(), name='add_experiment') # new
]
