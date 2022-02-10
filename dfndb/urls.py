from django.urls import path

from .views import (
    CompoundTableView,
    DeleteMaterialView,
    MaterialTableView,
    MaterialView,
    NewCompoundView,
    NewMaterialView,
    UpdateCompoundView,
    UpdateMaterialView,
)

app_name = "dfndb"

urlpatterns = [
    path("new_compound/", NewCompoundView.as_view(), name="New Compound"),
    path("compounds/", CompoundTableView.as_view(), name="Compounds"),
    path(
        "compounds/edit/<int:pk>/", UpdateCompoundView.as_view(), name="Update Compound"
    ),
    path("materials/", MaterialTableView.as_view(), name="Materials"),
    path("materials/<int:pk>/", MaterialView.as_view(), name="Material"),
    path("new_material/", NewMaterialView.as_view(), name="New Material"),
    path(
        "materials/edit/<int:pk>/", UpdateMaterialView.as_view(), name="Update Material"
    ),
    path(
        "materials/delete/<int:pk>/",
        DeleteMaterialView.as_view(),
        name="Delete Material",
    ),
]
