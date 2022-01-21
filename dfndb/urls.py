from django.urls import path

from .views import NewCompoundView, NewMaterialView

app_name = "dfndb"

urlpatterns = [
    path("new_compound/", NewCompoundView.as_view(), name="New Compound"),
    path("new_material/", NewMaterialView.as_view(), name="New material"),
]
