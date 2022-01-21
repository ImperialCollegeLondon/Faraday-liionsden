from django.urls import path

from .views import NewCompoundView

app_name = "dfndb"

urlpatterns = [path("new_compound/", NewCompoundView.as_view(), name="New Compound")]
