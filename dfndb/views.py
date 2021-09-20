from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView

from .models import Data, Parameter, Compound
from .serializers import ParameterSerializer
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from guardian.mixins import PermissionRequiredMixin as GuardianPermissionRequiredMixin


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


class CompoundCreateView(PermissionRequiredMixin, CreateView):
    model = Compound
    fields = ['name', 'formula', 'mass', 'status']

    
    template_name = 'dfndb/create.html'
    permission_required = ('dfndb.add_compound',)

    def get_success_url(self):
        return reverse_lazy('dfndb:compound_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user_owner = self.request.user
        response = super().form_valid(form)
        return response

class CompoundDetail(GuardianPermissionRequiredMixin, DetailView):
    model = Compound
    template = 'dfndb/compound_detail.html'
    permission_required = "view_compound"