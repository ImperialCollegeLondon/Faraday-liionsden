from django.urls import path

from .views import (
    CompoundTableView,
    MaterialTableView,
    MaterialView,
    NewCompoundView,
    NewMaterialView,
)

app_name = "dfndb"

urlpatterns = [
    path("new_compound/", NewCompoundView.as_view(), name="New Compound"),
    path("compounds/", CompoundTableView.as_view(), name="Compounds"),
    path("materials/<int:pk>/", MaterialView.as_view(), name="Material"),
    path("new_material/", NewMaterialView.as_view(), name="New Material"),
    path("materials/", MaterialTableView.as_view(), name="Materials"),
]
