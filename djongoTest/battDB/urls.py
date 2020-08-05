from django.urls import path

from . import views
from .views import ExperimentsView, CreateExperimentView

urlpatterns = [
    path('', views.index, name='index'),
    path('viewData', views.viewdata, name='viewData'),
    path('uploadData', views.uploaddata, name='uploadData'),
    path('exp', ExperimentsView.as_view(), name='Experiments'),
    path('create_exp/', CreateExperimentView.as_view(), name='add_experiment') # new
]
