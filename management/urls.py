from django.urls import path

from .views import register_request

urlpatterns = [path("register", register_request, name="registration")]
