from django.contrib import messages
from django.shortcuts import redirect, render
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            # Do other stuff before saving here
            obj.user_owner = request.user
            if form.is_public():
                obj.status = "public"
            else:
                obj.status = "private"
            obj.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return redirect(self.success_url) if self.success_url else redirect(obj)
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # Do other stuff before saving here
            if form.is_public():
                self.object.status = "public"
            else:
                self.object.status = "private"
            self.object.save()
            messages.success(request, self.success_message)
            # Redirect to object detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return (
                    redirect(self.success_url)
                    if self.success_url
                    else redirect(self.object)
                )
        messages.error(request, self.failure_message)
        return render(request, self.template_name, {"form": form})


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
