from django.urls import path

from . import views

app_name = 'dfndb'

urlpatterns = [
    path('create_compound/', views.CompoundCreateView.as_view(), name='create_compound'),
    path('<int:pk>/compound_detail/', views.CompoundDetail.as_view(), name='compound_detail')
]