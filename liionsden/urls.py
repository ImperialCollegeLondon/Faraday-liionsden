"""liionsden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from azure.core.utils import parse_connection_string
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index

urlpatterns = [
    path("", index, name="home"),
    path("battDB/", include("battDB.urls")),
    path(r"admin/", admin.site.urls),
    path("accounts/", include("management.urls")),
    path("dfndb/", include("dfndb.urls")),
]

urlpatterns += static(
    parse_connection_string(settings.AZURE_CONNECTION_STRING)["blobendpoint"],
    document_root=settings.MEDIA_ROOT,
)
