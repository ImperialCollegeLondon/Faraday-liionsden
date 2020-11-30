from dataclasses import dataclass
#from yamldataclassconfig.config import YamlDataClassConfig
import platform

# Config Schema & Defaults using shiny Python3.7 dataclasses
# TODO: Most of this config is NOT YET USED
@dataclass
class HarvesterConfig():
    @dataclass
    class DBConfig:
        auth_token: str = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a"
        host: str = "127.0.0.1"
        port: int = 8000

    @dataclass
    class FolderConfig:
        experiment_id: int
        path: str
        recurse: bool = True
        file_patterns: tuple = ("*",)
        parser: str = "auto"
        columns: tuple = (("I/mA",    "Current"),
                          ("V/mV",    "Voltage"),)

    # We can extend the FolderConfig class and add fields or override them for better defaults
    @dataclass
    class MyBiologicFolderConfig(FolderConfig):
        auth_token: str = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a"  # assign files to a different user? (TODO)
        parser: str = "biologic"
        file_patterns: tuple = (".csv", ".tsv", ".mpt")
        columns: tuple = (("I/mA",    "Current"),
                          ("ECell/V",    "Voltage"),)

    database: DBConfig = DBConfig()
    machine_id: str = platform.uname()[1]
    min_file_size: int = 1024
    min_file_age: int = 60
    folders: tuple = (
        FolderConfig(path="/tmp/harvester-data", experiment_id=1),
        MyBiologicFolderConfig(path="/tmp/harvester-data-bio2", experiment_id=2),
    )

