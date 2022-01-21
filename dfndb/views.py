from django.urls import reverse_lazy
from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView

from common.views import NewDataView, NewDataViewInline

from .filters import CompoundFilter
from .forms import CompositionPartFormSet, NewCompoundForm, NewMaterialForm
from .models import Compound, Data, Parameter
from .serializers import ParameterSerializer
from .tables import CompoundTable


### CREATE/ADD VIEWS ###
class NewCompoundView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_compound"
    template_name = "create_edit_generic.html"
    form_class = NewCompoundForm
    success_url = "/dfndb/new_compound/"
    success_message = "New compound created successfully."
    failure_message = "Could not save new compound. Invalid information."


class NewMaterialView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "dfndb.add_material"
    template_name = "create_edit_generic.html"
    form_class = NewMaterialForm
    success_url = "/dfndb/new_material/"
    success_message = "New material created successfully."
    failure_message = "Could not save new material. Invalid information."
    inline_key = "composition"
    formset = CompositionPartFormSet


### SEARCH/LIST/TABLE VIEWS ###
class CompoundTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Compound
    table_class = CompoundTable
    template_name = "compounds_table.html"
    filterset_class = CompoundFilter
    export_formats = ["csv", "json"]
    permission_required = "dfndb.view_compound"


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
