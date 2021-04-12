"""dfndb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path("data", views.DataListView.as_view(), name="data"),
    path("parameters/", views.ParametersAPIView.as_view(), name="parameters"),
]
