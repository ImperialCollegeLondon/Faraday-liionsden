from dataclasses import dataclass
import platform

# Config Schema & Defaults using shiny Python3.7 dataclasses
# TODO: Most of this config is NOT YET USED


@dataclass
class HarvesterConfig():
    # THESE ARE JUST THE DEFAULT VALUES - see __init__.py for the actual config

    @dataclass
    class DBConfig:
        auth_token: str  # This random number is like a cookie which both identifies and authenticates a user and can easily be changed on the website
        host: str = "127.0.0.1"
        port: int = 8000

    @dataclass
    class FolderConfig:
        path: str                      # local path on system, e.g. "C:\CyclerData\Maccor"
        experiment_id: int             # Experiment ID in the database to associate files with (TODO)
        recursive: bool = False        # Traverse sub-directories
        polling: bool = False          # When running on a network share, we might have to specify polling=True (TODO)
        file_patterns: tuple = ("*",)  # List of file extensions / patterns to look for (TODO)
        parser: str = "autodetect"     # use a specific parser (TODO) choices will be: autodetect, biologic, ivium, maccor, neware..
        columns: tuple = (("I/mA",    "Current"),  # List of columns in ('file header', 'human-readable name') format (TODO)
                          ("V/mV",    "Voltage"),)
        auth_token: str = ""           # put an auth token here to assign files to a different user (TODO)

    # We can extend the FolderConfig class and add fields or override them for better defaults
    @dataclass
    class MyBiologicFolderConfig(FolderConfig):
        parser: str = "biologic"                                      # specify a default parser (TODO)
        file_patterns: tuple = (".csv", ".tsv", ".mpt")               # specify file extensions per-folder (TODO)
        columns: tuple = (("I/mA",    "Current"),
                          ("ECell/V",    "Voltage"),)

    database: DBConfig
    local_filelist_cache = "filelist_cache.yaml" # use a YAML file to cache local filenames so that we don't have to hash them all every time
    experiment_id: int = -1                 # specify the ID of an experiment in the database
    machine_id: str = platform.uname()[1]
    file_patterns: tuple = (".csv", ".tsv", ".mpt", ".txt")  # specify file extensions (lower case)
    min_file_size: int = 1024                # ignore files smaller than this many Bytes
    min_file_age: int = 60                   # ignore files younger than this many seconds
    folders: tuple = (                       # monitor these folders, must specify path and experiment id, may override any other default above
        # FolderConfig(path="/tmp/harvester-data", experiment_id=1),  # specify actual config in __init__.py
        # MyBiologicFolderConfig(path="/tmp/harvester-data-bio2", experiment_id=2),
    )

    def get_folder_config(self, path: str):
        return

