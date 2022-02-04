from django.urls import path

from battDB.forms import NewExperimentDataFileForm

from .views import (
    BatchTableView,
    BatchView,
    DeleteDeviceView,
    DeviceSpecificationTableView,
    DeviceSpecificationView,
    EquipmentTableView,
    EquipmentView,
    ExperimentTableView,
    ExperimentView,
    NewBatchView,
    NewDataFileView,
    NewDeviceView,
    NewEquipmentView,
    NewExperimentView,
    NewProtocolView,
    UpdateBatchView,
    UpdateDeviceView,
    UpdateEquipmentView,
    UpdateExperimentView,
    index,
)

app_name = "battDB"

urlpatterns = [
    path("", index, name="index"),
    path("exps/", ExperimentTableView.as_view(), name="Experiments"),
    path("exps/<int:pk>/", ExperimentView.as_view(), name="Experiment"),
    path(
        "exps/edit/<int:pk>", UpdateExperimentView.as_view(), name="Update Experiment"
    ),
    path("batches/", BatchTableView.as_view(), name="Batches"),
    path("batches/<int:pk>/", BatchView.as_view(), name="Batch"),
    path("batches/edit/<int:pk>/", UpdateBatchView.as_view(), name="Update Batch"),
    path("equipment/", EquipmentTableView.as_view(), name="Equipment list"),
    path("equipment/<int:pk>/", EquipmentView.as_view(), name="Equipment"),
    path(
        "equipment/edit/<int:pk>/",
        UpdateEquipmentView.as_view(),
        name="Update Equipment",
    ),
    path("devices/", DeviceSpecificationTableView.as_view(), name="Devices"),
    path("devices/<int:pk>/", DeviceSpecificationView.as_view(), name="Device"),
    path("devices/edit/<int:pk>/", UpdateDeviceView.as_view(), name="Update Device"),
    path("devices/delete/<int:pk>/", DeleteDeviceView.as_view(), name="Delete Device"),
    path("new_device/", NewDeviceView.as_view(), name="New Device"),
    path("new_equipment/", NewEquipmentView.as_view(), name="New Equipment"),
    path("new_batch/", NewBatchView.as_view(), name="New Batch"),
    path("new_protocol/", NewProtocolView.as_view(), name="New Protocol"),
    path("new_experiment/", NewExperimentView.as_view(), name="New Experiment"),
    path("new_edf/", NewDataFileView.as_view(), name="New File"),
]

"""The following url patterns will be added on a need basis, as new functionality 
becomes available:

path('viewData/<int:pk>', ExperimentDataView.as_view(), name='viewData'),
path('viewDataRange/<int:pk>', DataRangeView.as_view(), name='viewDataRange'),
path('process/<int:pk>', ProcessExperimentView.as_view(), name='Process'),
path('files', AllFilesView.as_view(), name='Files'),
path('ranges', AllRangesView.as_view(), name='Data Ranges'),
path(
    "exp/<slug:owner>/<slug:name>/<slug:date>",
    ExperimentView.as_view(),
    name="Experiment_slug",
),
path('exp/<slug:slug>', ExperimentView.as_view(), name='Experiment'),
path('create_exp/', CreateExperimentView.as_view(), name='add_experiment'),
url(r'^getData/', get_data),
url(r"^plotData/", plotData),
path("upload/<str:filename>", UploadFileView.as_view(), name="upload_file"),
path("api/exp/<int:pk>", ExperimentAPIView.as_view(), name="experiment_api"),
path("api/exp", ExperimentAPIListView.as_view(), name="experiment_list_api"),
path("api/dataList", DataFileListAPIView.as_view(), name="data_list_api"),
path("api/dataCreate", DataFileCreateAPIView.as_view(), name="data_create_api"),
# path('api/harvester/<slug:slug>', HarvesterAPIView.as_view(),
name='harvester_api'),
path("api/hash_list", AllFileHashesAPIView.as_view(), name="hashes_api"),
"""
