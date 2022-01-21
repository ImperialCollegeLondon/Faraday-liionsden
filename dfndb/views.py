from django.urls import reverse_lazy
from django.views.generic import ListView
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView

from common.views import NewDataView, NewDataViewInline

from .forms import NewCompoundForm
from .models import Data, Parameter
from .serializers import ParameterSerializer


class NewCompoundView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_compound"
    template_name = "create_edit_generic.html"
    form_class = NewCompoundForm
    success_url = "/dfndb/new_compound/"
    success_message = "New compound created successfully."
    failure_message = "Could not save new compound. Invalid information."


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
