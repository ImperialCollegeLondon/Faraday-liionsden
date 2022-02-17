from django.urls import path

from .views import (
    ComponentTableView,
    ComponentView,
    CompoundTableView,
    DeleteComponentView,
    NewComponentView,
    NewCompoundView,
    UpdateComponentView,
    UpdateCompoundView,
)

app_name = "dfndb"

urlpatterns = [
    path("new_compound/", NewCompoundView.as_view(), name="New Compound"),
    path("compounds/", CompoundTableView.as_view(), name="Compounds"),
    path(
        "compounds/edit/<int:pk>/", UpdateCompoundView.as_view(), name="Update Compound"
    ),
    path("components/", ComponentTableView.as_view(), name="Components"),
    path("components/<int:pk>/", ComponentView.as_view(), name="Component"),
    path("new_component/", NewComponentView.as_view(), name="New Component"),
    path(
        "components/edit/<int:pk>/",
        UpdateComponentView.as_view(),
        name="Update Component",
    ),
    path(
        "components/delete/<int:pk>/",
        DeleteComponentView.as_view(),
        name="Delete Component",
    ),
]
