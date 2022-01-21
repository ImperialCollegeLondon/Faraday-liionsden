from django.urls import path

from .views import CompoundTableView, NewCompoundView, NewMaterialView

app_name = "dfndb"

urlpatterns = [
    path("new_compound/", NewCompoundView.as_view(), name="New Compound"),
    path("compounds/", CompoundTableView.as_view(), name="Compounds"),
    path("new_material/", NewMaterialView.as_view(), name="New material"),
]
