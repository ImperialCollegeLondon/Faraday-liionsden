
from .config import HarvesterConfig as hc

CONFIG: hc = hc(
    database=hc.DBConfig(auth_token="52f1021a6e32e4202acab1c5c19f0067cc1ce38a"),
    folders=(
        hc.FolderConfig(path="/tmp/harvester-data", experiment_id=1, recursive=False),
        hc.MyBiologicFolderConfig(path="/tmp/harvester-data/biologic", experiment_id=2, file_patterns=(".txt")),
    )
)