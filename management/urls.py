from django.urls import path

from .views import login_request, logout_request, register_request

urlpatterns = [
    path("register/", register_request, name="registration"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
]
