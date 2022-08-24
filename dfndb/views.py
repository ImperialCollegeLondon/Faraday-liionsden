from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView

from common.views import (
    MarkAsDeletedView,
    NewDataView,
    NewDataViewInline,
    UpdateDataInlineView,
    UpdateDataView,
)

from .filters import ComponentFilter, CompoundFilter
from .forms import CompositionPartFormSet, NewComponentForm, NewCompoundForm
from .models import Component, Compound, Data, Parameter
from .serializers import ParameterSerializer
from .tables import ComponentTable, CompoundTable

# flake8: noqa E266

######################## CREATE, ADD, DELETE VIEWS #########################
class NewCompoundView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_compound"
    template_name = "create_edit_generic.html"
    form_class = NewCompoundForm
    success_url = "/dfndb/compounds/"
    success_message = "New compound created successfully."
    failure_message = "Could not save new compound. Invalid information."


class NewComponentView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "dfndb.add_component"
    template_name = "create_edit_generic.html"
    form_class = NewComponentForm
    success_message = "New component created successfully."
    failure_message = "Could not save new component. Invalid information."
    inline_formsets = {"composition": CompositionPartFormSet}


class DeleteComponentView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Component
    permission_required = "dfndb.change_component"
    success_url = "/dfndb/components/"
    template_name = "delete_generic.html"
    success_message = "Component deleted successfully."


#################### DETAIL, LIST, TABLE VIEWS #########################
class CompoundTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Compound
    table_class = CompoundTable
    template_name = "compounds_table.html"
    filterset_class = CompoundFilter
    export_formats = ["csv", "json"]
    permission_required = "dfndb.view_compound"


class ComponentTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = Component
    table_class = ComponentTable
    template_name = "components_table.html"
    filterset_class = ComponentFilter
    export_formats = ["csv", "json"]
    permission_required = "dfndb.view_component"


class ComponentView(PermissionRequiredMixin, DetailView):
    model = Component
    template_name = "component.html"
    permission_required = "dfndb.view_component"


class UpdateComponentView(PermissionRequiredMixin, UpdateDataInlineView):
    model = Component
    permission_required = "dfndb.change_component"
    template_name = "create_edit_generic.html"
    form_class = NewComponentForm
    success_url = "/dfndb/components/"
    sucess_message = "Component updated successfully."
    failure_message = "Could not update component. Invalid information."
    inline_formsets = {"composition": CompositionPartFormSet}


class UpdateCompoundView(PermissionRequiredMixin, UpdateDataView):
    model = Compound
    permission_required = "dfndb.change_compound"
    template_name = "create_edit_generic.html"
    form_class = NewCompoundForm
    success_url = "/dfndb/compounds/"
    sucess_message = "Compound updated successfully."
    failure_message = "Could not update compound. Invalid information."
    inline_key = "composition"
    formset = CompositionPartFormSet


class DataListView(ListView):
    """View of available data.

    TODO: Not working, for now. Removed from urls.
    """

    model = Data
    page_title = "Data list"
    create_url = reverse_lazy("dfndb:cdata")
    create_label = "Create new Data"


class ParametersAPIView(ListCreateAPIView):
    """API for getting and creating parameters.

    TODO: Removed from URLS. Do we really want an API for this?
    """

    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
