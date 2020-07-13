from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewData', views.viewdata, name='viewData'),
    path('uploadData', views.uploaddata, name='uploadData'),

]
