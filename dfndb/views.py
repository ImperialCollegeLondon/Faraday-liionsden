from django.urls import reverse_lazy
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView

from .models import Data, Parameter
from .serializers import ParameterSerializer


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

    TODO: Do we really want an API for this?
    """

    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
