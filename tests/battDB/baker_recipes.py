from model_bakery.recipe import Recipe, foreign_key, seq

from battDB.models import (
    Batch,
    DataColumn,
    DataRange,
    Device,
    DeviceComponent,
    DeviceConfig,
    DeviceConfigNode,
    DeviceParameter,
    DeviceSpecification,
    Equipment,
    Experiment,
    ExperimentDataFile,
    ExperimentDevice,
    Parser,
    SignalType,
    UploadedFile,
)
from tests.common.baker_recipes import org
from tests.dfndb.baker_recipes import component, parameter
from tests.management.baker_recipes import user

device_specification = Recipe(
    DeviceSpecification,
    user_owner=foreign_key(user),
    name=seq("Device Specification"),  # Ensure uniqueness
)

device_parameter = Recipe(
    DeviceParameter,
    spec=foreign_key(device_specification),
    parameter=foreign_key(parameter),
)

device_component = Recipe(
    DeviceComponent,
    spec=foreign_key(device_specification),
    component=foreign_key(component),
)


device_config = Recipe(DeviceConfig, user_owner=foreign_key(user))

device_config_node = Recipe(
    DeviceConfigNode,
    device=foreign_key(device_specification),
    config=foreign_key(device_config),
)

batch = Recipe(
    Batch,
    specification=foreign_key(device_specification),
    manufacturer=foreign_key(org),
    user_owner=foreign_key(user),
    serialNo=seq("abc123"),  # Ensure uniqueness
)

device = Recipe(Device, batch=foreign_key(batch))

parser = Recipe(Parser, user_owner=foreign_key(user))

equipment = Recipe(
    Equipment,
    institution=foreign_key(org),
    user_owner=foreign_key(user),
    name=seq("Equipment"),  # Ensure uniqueness
)

experiment = Recipe(
    Experiment,
    config=foreign_key(device_config),
    user_owner=foreign_key(user),
    name=seq("Experiment"),  # Ensure uniqueness
)

edf = Recipe(ExperimentDataFile, user_owner=foreign_key(user))

uploaded_file = Recipe(UploadedFile, user_owner=foreign_key(user))

experiment_device = Recipe(
    ExperimentDevice, experiment=foreign_key(experiment), batch=foreign_key(batch)
)

data_column = Recipe(
    DataColumn,
    resample_n=0,
    device=foreign_key(experiment_device),
    parameter=foreign_key(parameter),
    data_file=foreign_key(edf),
)

data_range = Recipe(DataRange, dataFile=foreign_key(edf), user_owner=foreign_key(user))

signal_type = Recipe(
    SignalType, parameter=foreign_key(parameter), parser=foreign_key(parser)
)
