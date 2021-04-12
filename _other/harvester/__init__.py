
from .config import HarvesterConfig as hc


# Minimal config - any of the values in HarvesterConfig can be overridden here
CONFIG: hc = hc(
    database=hc.DBConfig(auth_token="52f1021a6e32e4202acab1c5c19f0067cc1ce38a",
                         #host="ns3122207.ip-54-38-195.eu", port=10802),
                         host="localhost", port=8000),
    folders=(
        hc.FolderConfig(path="/tmp/harvester-data", experiment_id=1, recursive=False),
        hc.MyBiologicFolderConfig(path="/tmp/harvester-data/biologic", experiment_id=2, file_patterns=(".txt")),
    ),
    experiment_id=8,
    machine_id=1
)
