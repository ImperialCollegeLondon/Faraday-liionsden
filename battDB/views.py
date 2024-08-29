import django_tables2 as tables2
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import MultiTableMixin, SingleTableMixin
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from pandas import DataFrame
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from common.views import (
    MarkAsDeletedView,
    NewDataView,
    NewDataViewInline,
    UpdateDataInlineView,
    UpdateDataView,
)
from management.custom_azure import generate_sas_token, get_blob_url

from .filters import (
    BatchFilter,
    DeviceSpecificationFilter,
    EquipmentFilter,
    ExperimentFilter,
    ParserFilter,
)
from .forms import (
    DeviceComponentFormSet,
    DeviceParameterFormSet,
    ExperimentDeviceFormSet,
    NewBatchForm,
    NewDeviceForm,
    NewEquipmentForm,
    NewExperimentDataFileForm,
    NewExperimentForm,
    NewProtocolForm,
    UploadDataFileFormset,
)
from .models import (
    Batch,
    DataRange,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    Parser,
    UploadedFile,
)
from .plots import get_html_plot
from .serializers import (
    DataFileSerializer,
    DataRangeSerializer,
    ExperimentSerializer,
    FileHashSerializer,
    GeneralSerializer,
    NewDataFileSerializer,
)
from .tables import (
    BatchTable,
    DeviceSpecificationTable,
    EquipmentTable,
    ExperimentDataTable,
    ExperimentTable,
    ParserTable,
)


def index(request):
    return redirect("/")


######################## CREATE, ADD, DELETE VIEWS #########################
class NewDeviceView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_message = "New device specification created successfully."
    failure_message = "Could not save new device. Invalid information."
    inline_formsets = {
        "parameters": DeviceParameterFormSet,
        "components": DeviceComponentFormSet,
    }


class NewExperimentView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.add_experiment"
    model = Experiment
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_message = "New experiment created successfully."
    failure_message = "Could not save new experiment. Invalid information."
    inline_formsets = {"devices": ExperimentDeviceFormSet}

    def get_context_data(self, **kwargs):
        """
        Helper function to get correct context to pass to render() in get()
        and post(). Overridden here because this formset needs to be passed
        the user object.
        """
        data = super(NewDataViewInline, self).get_context_data(**kwargs)
        if self.request.POST:
            for key, formset in self.inline_formsets.items():
                data[key] = formset(self.request.POST, self.request.FILES)
        else:
            for key, formset in self.inline_formsets.items():
                data[key] = formset(user=self.request.user)
        return data


class NewEquipmentView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_message = "New equipment created successfully."
    failure_message = "Could not save new equipment. Invalid information."


class NewBatchView(PermissionRequiredMixin, NewDataView):
    permission_required = "battDB.add_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_message = "New batch created successfully."
    failure_message = "Could not save new batch. Invalid information."

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display device_specifications in the dropdown
        that the user has permsission to view.
        """

        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        if not self.request.user:
            raise ValueError("User object not passed to form class.")
        return kwargs


class NewDataFileView(PermissionRequiredMixin, NewDataViewInline):
    permission_required = "battDB.change_experiment"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentDataFileForm
    success_message = "New data_file added successfully."
    failure_message = "Could not add new data file. Invalid information."
    inline_formsets = {"raw_data_file": UploadDataFileFormset}

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display devices that belong to the experiment.
        """

        kwargs = super().get_form_kwargs()
        kwargs["experiment"] = Experiment.objects.get(pk=self.kwargs.get("pk"))
        return kwargs

    def get_permission_object(self, *args, **kwargs):
        # Only allowed by users who can change current Experiment
        return Experiment.objects.get(pk=self.kwargs.get("pk"))

    def post(self, request, *args, **kwargs):
        """
        Unique post method for data files to handle a) setting user_owner and
        status of uploaded file and b) parsing pk of associated experiment.
        """
        form = self.form_class(request.POST, request.FILES)
        context = self.get_context_data()
        formset = context["raw_data_file"]
        if form.is_valid():
            # Save instance incluing setting user owner and status
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.user_owner = request.user
                # Set experiment PK based on URL
                obj.experiment = Experiment.objects.get(pk=self.kwargs.get("pk"))
                if form.is_public():
                    obj.status = "public"
                else:
                    obj.status = "private"
                self.object = form.save()

            # Save individual parameters from inline form
            if formset.is_valid():
                formset.instance = self.object
                # Handle uploaded files in formsets slightly differently to usual
                formset[0].instance.user_owner = obj.user_owner
                formset[0].instance.status = obj.status
                if formset[0].instance.use_parser:
                    formset[0].instance.parse = True
                # If the data file is already uploaded, catch error and delete EDF obj.
                try:
                    formset.save()
                    form.instance.full_clean()
                    if not self.object.ts_data and formset[0].instance.use_parser:
                        messages.error(
                            request,
                            "Could not parse file - is it a valid data file?",
                        )
                        self.object.delete()
                        return redirect("/battDB/exps/{}".format(self.kwargs.get("pk")))
                except IntegrityError:
                    messages.error(
                        request,
                        "Could not save data file - has it already been uploaded?",
                    )
                    self.object.delete()
                    return render(request, self.template_name, context)
                # Everything was fine - save and view experiment details page
                form.instance.save()
                messages.success(request, self.success_message)
                # Redirect to experiment detail view or stay on form if "add another"
                if "another" in request.POST:
                    return redirect(request.path_info)
                else:
                    return redirect("/battDB/exps/{}".format(self.kwargs.get("pk")))
            # formset not valid so delete EDF object and return to form
            self.object.delete()
        # form or formset is not valid so return to form
        messages.error(request, "Could not save data file - form not valid.")
        return render(request, self.template_name, context)


class NewProtocolView(PermissionRequiredMixin, NewDataView):
    permission_required = "dfndb.add_method"
    template_name = "create_protocol.html"
    form_class = NewProtocolForm
    success_message = "New protocol created successfully."
    failure_message = "Could not save new protocol. Invalid information."


class UpdateDeviceView(PermissionRequiredMixin, UpdateDataInlineView):
    model = DeviceSpecification
    permission_required = "battDB.change_devicespecification"
    template_name = "create_edit_generic.html"
    form_class = NewDeviceForm
    success_message = "Device specification updated successfully."
    failure_message = "Could not update Device specification. Invalid information."
    inline_formsets = {
        "parameters": DeviceParameterFormSet,
        "components": DeviceComponentFormSet,
    }


class UpdateExperimentView(PermissionRequiredMixin, UpdateDataInlineView):
    model = Experiment
    permission_required = "battDB.change_experiment"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentForm
    success_message = "Experiment updated successfully."
    failure_message = "Could not update experiment. Invalid information."
    inline_formsets = {"devices": ExperimentDeviceFormSet}


class UpdateEquipmentView(PermissionRequiredMixin, UpdateDataView):
    model = Equipment
    permission_required = "battDB.change_equipment"
    template_name = "create_edit_generic.html"
    form_class = NewEquipmentForm
    success_message = "Equipment updated successfully."
    failure_message = "Could not update Equipment. Invalid information."


class UpdateBatchView(PermissionRequiredMixin, UpdateDataView):
    model = Batch
    permission_required = "battDB.change_batch"
    template_name = "create_edit_generic.html"
    form_class = NewBatchForm
    success_message = "Batch updated successfully."
    failure_message = "Could not update batch. Invalid information."

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display device_specifications in the dropdown
        that the user has permsission to view.
        """

        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class UpdateDataFileView(PermissionRequiredMixin, UpdateDataInlineView):
    model = ExperimentDataFile
    permission_required = "battDB.change_experimentdatafile"
    template_name = "create_edit_generic.html"
    form_class = NewExperimentDataFileForm
    success_message = "Data file updated successfully."
    failure_message = "Could not update data file. Invalid information."
    inline_formsets = {"raw_data_file": UploadDataFileFormset}

    def get_form_kwargs(self):
        """
        Passes the request object to the form class.
        This is necessary to only display devices that belong to the experiment.
        """

        kwargs = super().get_form_kwargs()
        kwargs["experiment"] = Experiment.objects.get(pk=self.object.experiment.id)
        return kwargs

    def post(self, request, *args, **kwargs):
        """
        Unique post method for data files to handle a) setting user_owner and
        status of uploaded file and b) parsing pk of associated experiment.
        """
        self.object = self.get_object()
        form = self.form_class(
            request.POST,
            request.FILES,
            instance=self.object,
        )
        context = self.get_context_data()
        if form.is_valid():
            obj = form.save(commit=False)
            # Save instance incluing setting user owner and status
            if form.is_public():
                obj.status = "public"
            else:
                obj.status = "private"
            obj.save()
            form.save_m2m()
            messages.success(request, self.success_message)
            # Redirect to experiment detail view or stay on form if "add another"
            if "another" in request.POST:
                return redirect(request.path_info)
            else:
                return redirect(f"/battDB/exps/{self.object.experiment.id}")
        messages.error(request, "Could not update information - form not valid.")
        return render(request, self.template_name, context)


class DeleteDeviceView(PermissionRequiredMixin, MarkAsDeletedView):
    model = DeviceSpecification
    permission_required = "battDB.change_devicespecification"
    success_url = "/battDB/devices/"
    template_name = "delete_generic.html"
    success_message = "Device Specification deleted successfully."


class DeleteExperimentView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Experiment
    permission_required = "battDB.change_experiment"
    success_url = "/battDB/exps/"
    template_name = "delete_generic.html"
    success_message = "Experiment deleted successfully."


class DeleteEquipmentView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Equipment
    permission_required = "battDB.change_equipment"
    success_url = "/battDB/equipment/"
    template_name = "delete_generic.html"
    success_message = "Equipment deleted successfully."


class DeleteBatchView(PermissionRequiredMixin, MarkAsDeletedView):
    model = Batch
    permission_required = "battDB.change_batch"
    success_url = "/battDB/batches/"
    template_name = "delete_generic.html"
    success_message = "Batch deleted successfully."


class DeleteDataFileView(PermissionRequiredMixin, MarkAsDeletedView):
    model = ExperimentDataFile
    permission_required = "battDB.change_experimentdatafile"
    template_name = "delete_generic.html"
    success_message = "Data file deleted successfully."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = "deleted"
        self.object.save()
        messages.success(request, self.success_message)
        return redirect(self.object.experiment)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#################### DETAIL, LIST, TABLE VIEWS #########################
class ExperimentTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = Experiment
    table_class = ExperimentTable
    template_name = "experiments_table.html"
    filterset_class = ExperimentFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_experiment"


class BatchTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Batch
    table_class = BatchTable
    template_name = "batches_table.html"
    filterset_class = BatchFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_batch"


class DeviceSpecificationTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = DeviceSpecification
    table_class = DeviceSpecificationTable
    template_name = "device_specifications_table.html"
    filterset_class = DeviceSpecificationFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_devicespecification"


class EquipmentTableView(
    SingleTableMixin, ExportMixin, PermissionListMixin, FilterView
):
    model = Equipment
    table_class = EquipmentTable
    template_name = "equipment_table.html"
    filterset_class = EquipmentFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_equipment"


class ParserTableView(SingleTableMixin, ExportMixin, PermissionListMixin, FilterView):
    model = Parser
    table_class = ParserTable
    template_name = "parser_table.html"
    filterset_class = ParserFilter
    export_formats = ["csv", "json"]
    permission_required = "battDB.view_parser"


class ExperimentView(PermissionRequiredMixin, MultiTableMixin, DetailView):
    model = Experiment
    template_name = "experiment.html"
    permission_required = "battDB.view_experiment"
    table_class = ExperimentDataTable

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context.update({"plots": self.get_plots()})
        return self.render_to_response(context)

    def get_parsed_col_names(self, edf, parameter_names):
        """
        Given a list of parameter names, returns a list of the parsed column
        headers. If any parameters have not been parsed, returns an empty list.
        Args:
            edf (ExperimentDataFile): The data file to check
            parameter_names (list): list of parameter names
        Returns:
            list: list of parsed column headers (column names)
        """
        # get all the columns that can be parsed by the parser used
        all_cols = edf.raw_data_file.use_parser.columns.get_queryset()
        # of those, get the columns that match the parameter names given
        cols = all_cols.filter(parameter__name__in=parameter_names)
        # check that all of those columns have been parsed (are in ts_headers)
        all_parsed = all(i.col_name in edf.ts_headers for i in cols)

        if (len(cols) == len(parameter_names)) and all_parsed:
            return [i.col_name for i in cols]
        else:
            return []

    def get_plots(self):
        """
        For each of the data files associated with the experiment, generate a list of
        plots using the get_html_plot function.
        For now, it generates two plots if the necessary columns have been parsed:
        - Voltage vs. Current against Time
        - Voltage vs. Temparature against Time
        Returns a list of these lists. If there is no table data, returns an empty list.
        """
        experiment_plots = []
        for data_file, table in self.get_tables_data().items():
            if table:
                edf = self.object.data_files.get(name=data_file)
                df = DataFrame(table)
                # generate the plots
                plots = []
                parsed_cols = self.get_parsed_col_names(
                    edf, ["Time", "Voltage", "Current"]
                )
                if parsed_cols:
                    plots.append(
                        get_html_plot(
                            df,
                            x_col=parsed_cols[0],
                            y_cols=parsed_cols[1:],
                        )
                    )
                parsed_cols = self.get_parsed_col_names(
                    edf, ["Time", "Voltage", "Temperature"]
                )
                if parsed_cols:
                    plots.append(
                        get_html_plot(
                            df,
                            x_col=parsed_cols[0],
                            y_cols=parsed_cols[1:],
                        )
                    )
                experiment_plots.append(plots)
            else:
                experiment_plots.append([])
        return experiment_plots

    def get_tables(self):
        """
        Overriding from django_tables2.views.MultiTableMixin to include all columns
        dynamically. This is necessary to ensure that all columns are included in the
        table. The data files are used to determine which columns are available.
        Returns: list of tables
        """
        data = self.get_tables_data()
        data_files = self.object.data_files.all()
        tables = []
        # Iterate over the data dictionaries and create a table for each
        for data_set, data_file in zip(data, data_files):
            if data[data_set]:
                tables.append(
                    self.table_class(
                        data_set,
                        extra_columns=[
                            (i, tables2.Column()) for i in data_file.ts_headers
                        ],
                    )
                )
            else:
                tables.append(self.table_class(data=[{"None": "None"}]))

        return tables

    def get_tables_data(self, n_rows: int = 0, decimal_places: int = 2):
        """
        Overriding from django_tables2.views.MultiTableMixin to optionally get top n
        rows of data. Values are displayed to a chosen number of decimal_places for easy
        viewing.
        Args:
            n_rows: Number of rows to return. If 0, return all rows.
            decimal_places: Number of decimal places to display.
        Returns:
            Dictionary of lists. Each list contains a dictionary for each row of data.
        """
        data_files = self.object.data_files.all()
        data_previews = {}
        for data_file in data_files:
            if data_file.file_exists() and data_file.raw_data_file.parse:
                # Get the headers and data
                data_headers = data_file.ts_headers
                data = data_file.ts_data[:n_rows] if n_rows else data_file.ts_data
                data_preview = []
                for row in data:
                    data_preview.append(
                        {
                            header: round(value, decimal_places)
                            for (header, value) in zip(data_headers, row)
                        }
                    )
                data_previews[data_file.name] = data_preview
            else:
                data_previews[data_file.name] = None
        return data_previews


class DeviceSpecificationView(PermissionRequiredMixin, DetailView):
    model = DeviceSpecification
    template_name = "device_specification.html"
    permission_required = "battDB.view_devicespecification"


class BatchView(PermissionRequiredMixin, DetailView):
    model = Batch
    template_name = "batch.html"
    permission_required = "battDB.view_batch"


class EquipmentView(PermissionRequiredMixin, DetailView):
    model = Equipment
    template_name = "equipment.html"
    permission_required = "battDB.view_equipment"


class ParserView(PermissionRequiredMixin, DetailView):
    model = Parser
    template_name = "parser.html"
    permission_required = "battDB.view_parser"


class DownloadRawDataFileView(PermissionRequiredMixin, DetailView):
    model = ExperimentDataFile
    permission_required = "battDB.view_experimentdatafile"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        blob_name = self.object.raw_data_file.file.name
        blob_url = get_blob_url(self.object.raw_data_file.file)
        sas_token = generate_sas_token(blob_name)
        return redirect(f"{blob_url}?{sas_token}")


class DownloadBinaryFileView(PermissionRequiredMixin, DetailView):
    model = ExperimentDataFile
    permission_required = "battDB.view_experimentdatafile"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        blob_name = self.object.binary_file.name
        blob_url = get_blob_url(self.object.binary_file)
        sas_token = generate_sas_token(blob_name)
        return redirect(f"{blob_url}?{sas_token}")


class DownloadSettingsFileView(PermissionRequiredMixin, DetailView):
    model = ExperimentDataFile
    permission_required = "battDB.view_experimentdatafile"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        blob_name = self.object.settings_file.name
        blob_url = get_blob_url(self.object.settings_file)
        sas_token = generate_sas_token(blob_name)
        return redirect(f"{blob_url}?{sas_token}")


class DownloadSpecFileView(PermissionRequiredMixin, DetailView):
    model = DeviceSpecification
    permission_required = "battDB.view_devicespecification"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        blob_name = self.object.spec_file.name
        blob_url = get_blob_url(self.object.spec_file)
        sas_token = generate_sas_token(blob_name)
        return redirect(f"{blob_url}?{sas_token}")


### API VIEWS ###
class ExperimentAPIView(APIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentAPIListView(ListAPIView):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()


class DataRangeAPIView(ListAPIView):
    serializer_class = DataRangeSerializer
    queryset = DataRange.objects.all()


class AllFileHashesAPIView(ListAPIView):
    """Returns hashes and sizes of all files belonging to current user."""

    model = UploadedFile
    serializer_class = FileHashSerializer

    def get_queryset(self):
        return UploadedFile.objects.all()  # filter(user_owner=self.request.user)


class DataFileListAPIView(ListAPIView):
    serializer_class = DataFileSerializer

    def get_queryset(self):
        return ExperimentDataFile.objects.filter(
            user_owner=self.request.user, experiment=self.request.GET.get("exp")
        )


class DataFileCreateAPIView(CreateAPIView):
    serializer_class = NewDataFileSerializer


class GeneralViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        model = self.kwargs.get("model")
        return model.objects.filter(user_owner=self.request.user)

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.kwargs.get("model")
        return GeneralSerializer


class UploadFileView(GenericAPIView):
    queryset = UploadedFile.objects.all()
    parser_classes = (FileUploadParser,)
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, filename, **kwargs):
        if "file" not in request.data:
            raise ParseError("Empty content")

        f = request.data["file"]
        obj = UploadedFile()
        obj.file.save(filename, f, save=True)
        obj.user_owner = request.user
        obj.clean()
        obj.save()
        response_data = FileHashSerializer(obj).data
        return Response(response_data, status=status.HTTP_201_CREATED)

    def options(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
