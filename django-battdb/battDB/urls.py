from django.urls import path
from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    # path('viewData/<int:pk>', ExperimentDataView.as_view(), name='viewData'),
    # path('viewDataRange/<int:pk>', DataRangeView.as_view(), name='viewDataRange'),
    #path('process/<int:pk>', ProcessExperimentView.as_view(), name='Process'),
    path('exps', ExperimentsView.as_view(), name='Experiments'),
    # path('files', AllFilesView.as_view(), name='Files'),
    # path('ranges', AllRangesView.as_view(), name='Data Ranges'),
    path('exp/<slug:owner>/<slug:name>/<slug:date>', ExperimentView.as_view(), name='Experiment_slug'),
    #path('exp/<slug:slug>', ExperimentView.as_view(), name='Experiment'),
    path('exp/<int:pk>', ExperimentView.as_view(), name='Experiment'),
    #path('create_exp/', CreateExperimentView.as_view(), name='add_experiment'),
    #url(r'^getData/', get_data),
    url(r'^plotData/', plotData),
    path('upload/<str:filename>', UploadFileView.as_view(), name='upload_file'),
    path('api/exp/<int:pk>', ExperimentAPIView.as_view(), name='experiment_api'),
    path('api/exp', ExperimentAPIListView.as_view()),
    path('api/data', GeneralViewSet.as_view(actions={'get': 'list'}), name='data_api'),
    path('api/harvester/<slug:slug>', HarvesterAPIView.as_view(), name='harvester_api'),
    path('api/hash_list', AllFileHashesAPIView.as_view(), name='hashes_api'),
]
