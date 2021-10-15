from model_bakery.recipe import Recipe, foreign_key, related

from battDB.models import (
    Batch,
    DataColumn,
    DataRange,
    Device,
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
from tests.dfndb.baker_recipes import material, parameter
from tests.management.baker_recipes import user

device_specification = Recipe(DeviceSpecification, user_owner=foreign_key(user))

device_parameter = Recipe(
    DeviceParameter,
    spec=foreign_key(device_specification),
    parameter=foreign_key(parameter),
    material=foreign_key(material),
    user_owner=foreign_key(user),
)

device_config = Recipe(DeviceConfig, user_owner=foreign_key(user))

device_config_node = Recipe(
    DeviceConfigNode,
    device=foreign_key(device_specification),
    config=foreign_key(device_config),
    user_owner=foreign_key(user),
)

batch = Recipe(
    Batch,
    specification=foreign_key(device_specification),
    manufacturer=foreign_key(org),
    user_owner=foreign_key(user),
)

device = Recipe(Device, batch=foreign_key(batch), user_owner=foreign_key(user))

parser = Recipe(Parser, user_owner=foreign_key(user))

equipment = Recipe(
    Equipment, manufacturer=foreign_key(org), user_owner=foreign_key(user)
)

experiment = Recipe(
    Experiment, config=foreign_key(device_config), user_owner=foreign_key(user)
)

edf = Recipe(ExperimentDataFile, user_owner=foreign_key(user))

uploaded_file = Recipe(UploadedFile, user_owner=foreign_key(user))

experiment_device = Recipe(
    ExperimentDevice,
    experiment=foreign_key(experiment),
    batch=foreign_key(batch),
    user_owner=foreign_key(user),
)

data_column = Recipe(
    DataColumn,
    resample_n=0,
    device=foreign_key(experiment_device),
    parameter=foreign_key(parameter),
    data_file=foreign_key(edf),
    user_owner=foreign_key(user),
)

data_range = Recipe(DataRange, dataFile=foreign_key(edf), user_owner=foreign_key(user))

signal_type = Recipe(
    SignalType,
    parameter=foreign_key(parameter),
    parser=foreign_key(parser),
    user_owner=foreign_key(user),
)
