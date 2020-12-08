#!/usr/bin/env python3
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent, EVENT_TYPE_MODIFIED, EVENT_TYPE_CREATED, EVENT_TYPE_MOVED
import os
import sys
import requests
import json
from threading import Thread
import logging
from dataclasses import dataclass, asdict
from harvester import CONFIG
from harvester.utils import hash_file, has_handle

# schema for info about files in local filesystem
@dataclass
class FileObj:
    upload_id: int = None
    fhash: str = ""
    path: str = ""
    size: int = 0
    ignored: bool = False
    state: str = "default"

@dataclass
class DatafileRecord:
    upload_id: int
    experiment_id: int = -1
    edf_id: int = -1
    status: str = "draft"
    notes: str = "Uploaded by harvester API"
    parser: str = "autodetect"
    machine: str = CONFIG.machine_id


class HarvesterAPI:

    def __init__(self, site, auth_token):
        self.token = auth_token
        self.base_url = site
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_hashes(self):
        url = self.base_url + "/api/hash_list"
        self.logger.debug(f"Get hashes: {url}")
        headers = {'Authorization': 'Token ' + self.token, "Content-Type": "text/JSON"}
        response = requests.get(url, headers=headers)
        # return python dict
        return json.loads(response.text)

    def upload_file(self, pathname):
        (dirname, filename) = os.path.split(pathname)
        url = self.base_url + "/battDB/upload/" + filename

        headers = {'Authorization': 'Token ' + self.token, "Content-Type": "application/octet-stream"}
        # "Content-Disposition": "attachment; filename=foo"}
        response = requests.put(url, data=open(pathname,'rb'), headers=headers)
        self.logger.debug(f"Upload: {url} : {response.text}")
        return json.loads(response.text)

    #TODO
    def create_datafile_record(self, edf_obj: DatafileRecord):
        url = self.base_url + "/api/dataCreate"
        self.logger.debug(f"Create EDF: {url} : {asdict(edf_obj)}")
        headers = {'Authorization': 'Token ' + self.token}
        response = requests.post(url, data=asdict(edf_obj), headers=headers)
        self.logger.debug(f"EDF: {response.text}")
        return json.loads(response.text)


class HarvesterManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.info("======= Harvester utility started =========")
        # self.config = self.load_config(config_path)
        # logging.debug("Config Loaded: %s" % self.config)
        # self.config = self.load_config(config_path)
        self.API = HarvesterAPI(site=f"http://{CONFIG.database.host}:{CONFIG.database.port}",
                                auth_token=CONFIG.database.auth_token)
        self.observers = list()
        observer = Observer()
        self.remote_files_by_hash = dict()
        self.local_files_by_path = dict()
        self.check_db_files()
        self.event_handler = FSMonitor(self)

        # iterate through paths and attach observers
        for folder in CONFIG.folders:
            self.check_local_files(folder.path, recursive=folder.recursive)
            # Schedules watching of a given path
            observer.schedule(self.event_handler, folder.path, recursive=folder.recursive)
            # Add observable to list of observers
            self.observers.append(observer)

        # start observer
        try:
            observer.start()
        except FileNotFoundError as e:
            self.logger.error(f"Cannot start FS monitor: {e}")
            raise e # BUG: watchdog module does not include the filename when it raises FileNotFoundError

    def wait(self):
        logging.info("== Waiting for files ==")
        try:
            while True:
                # poll every second
                time.sleep(1)
                self.check_waiting_files()
                logging.debug("== Waiting for files ==")
        except KeyboardInterrupt:
            for o in self.observers:
                o.unschedule_all()
                # stop observer if interrupted
                o.stop()
        for o in self.observers:
            # Wait until the thread terminates before exit
            o.join()

    # load cached files list - TODO
    # def load_files_list(self):
    #     try:
    #         with open(config_file_path, "r") as config_file:
    #             logging.info("Reading config from %s" % config_file_path)
    #             return yaml.safe_load(config_file)
    #     except FileNotFoundError:
    #         write_config_template(config_file_path)
    #         return yaml.safe_load(DEFAULT_CONFIG)

    def found_new_file(self, filepath, source="found"):
        if os.path.splitext(filepath)[1].lower() not in CONFIG.file_patterns: # TODO: file_patterns for each folder!
            self.logger.debug("Wrong pattern: %s" % filepath)
            return None
        if filepath in self.local_files_by_path.keys():
            self.logger.error("New path twice! %s" % filepath)
            raise ValueError("New path twice!")
        fd = FileObj(path=filepath, size=os.path.getsize(filepath), state=source)
        self.local_files_by_path[filepath] = fd
        self.logger.debug("New file: %s" % filepath)
        return fd

    def process_file(self, fd):

        if fd.ignored or fd.upload_id is not None:
            #self.logger.debug("Ignored: %s", fd.path)
            return

        size = os.path.getsize(fd.path)

        if size < CONFIG.min_file_size:
            fd.state = "too_small"
            self.logger.debug("%s: Too small - skipping!" % fd.path)
            return

        if size > fd.size:
            fd.size = size
            fd.state = 'growing'
            self.logger.info("Growing: %s", fd.path)
            return

        # check if file is open
        if has_handle(fd.path):
            fd.state = "has_handle"
            self.logger.info(f"File [{fd.path}] is open in another process - skipping!")
            return

        # check minimum age
        file_age = time.time() - os.path.getmtime(fd.path)
        if file_age < CONFIG.min_file_age:
            self.logger.info(f"File [{fd.path}] was modified only {file_age}s ago - waiting!")
            fd.state = 'waiting'
            return

        # compute hash
        file_hash = hash_file(open(fd.path, "rb"))
        self.logger.debug(f"Computed file hash for {fd.path}: {fd.fhash}")
        if not fd.fhash:
            fd.fhash = file_hash
        elif file_hash is not fd.fhash:
            self.logger.warning(f"File hash changed for {fd.path}")
            fd.fhash = file_hash
        else:
            self.logger.warning(f"Computed hash twice for {fd.path}")

        # check if it exists in the list of hashes we got from the server
        remote_file = self.remote_files_by_hash.get(fd.fhash)
        if remote_file is not None:
            logging.warning(f"Already in database: {fd.path}")
            #if remote_file.edf_id is None:
            #    assign_to_experiment
            fd.state = 'exists_remote'
            fd.ignored = True
            return

    #     self.upload_file(fd)
    #
    # def upload_file(self, fd):

        # Try to upload
        self.logger.info(f"Uploading file: {fd.path}")
        try:
            remote_file = self.API.upload_file(fd.path)
            fd.upload_id = remote_file.get('id')
            self.logger.info(f"Got upload id: {fd.upload_id}")
            self.create_edf(fd)
        except requests.exceptions.RequestException:
            fd.state = 'upload_failed'
            return fd # try again
        finally:
            fd.state = 'uploaded'
            fd.ignored = True
            self.remote_files_by_hash[fd.fhash] = fd

    def create_edf(self, fd: FileObj):
        assert fd.upload_id is not None
        edf = DatafileRecord(experiment_id=CONFIG.experiment_id, upload_id = fd.upload_id)
        self.API.create_datafile_record(edf)

    def check_db_files(self):
        file = dict()
        try:
            for file in self.API.get_hashes():
                h = file['hash']
                self.remote_files_by_hash[h] = FileObj(state="exists_remote", fhash=h)
            self.logger.info("Database has %d files" % len(self.remote_files_by_hash))
        except requests.exceptions.ConnectionError:
            self.logger.error("Cannot fetch hash list: Cannot connect to database")
        except (KeyError, TypeError):
            self.logger.warning("Hashes not returned")
            self.logger.debug(file)

    def check_local_files(self, scan_path, recursive=False, source="found_local"):
        for root, subFolders, files in os.walk(scan_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.found_new_file(file_path, source)
            if not recursive:
                break
        self.logger.info("Local machine has %d files" % len(self.local_files_by_path))

    def check_waiting_files(self):
        #self.logger.debug("%d local files" % len(self.local_files_by_path))
        for fd in self.local_files_by_path.values():
            self.process_file(fd)

    # def load_config(self, config_file_path):
    #     try:
    #         with open(config_file_path, "r") as config_file:
    #             logging.info("Reading config from %s" % config_file_path)
    #             return yaml.safe_load(config_file)
    #     except FileNotFoundError:
    #         self.write_config_template(config_file_path)
    #         return yaml.safe_load(DEFAULT_CONFIG)
    #
    #
    # def write_config_template(self, config_template_path):
    #     # template = {
    #     #     "database_authtoken": "52f1021a6e32e4202acab1c5c19f0067cc1ce38a",
    #     #     "database_host": "127.0.0.1",
    #     #     "database_port": 8000,
    #     #     "machine_id": platform.uname()[1],
    #     #
    #     # }
    #     logging.info("Writing default config to %s" % config_template_path)
    #     with open(config_template_path, "w") as config_file:
    #         config_file.write(DEFAULT_CONFIG)



class FSMonitor(FileSystemEventHandler):
    def __init__(self, manager):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.manager = manager

    def on_modified(self, event: FileSystemEvent):
        if event.is_directory:
            self.logger.debug(f'new file: event type: {event.event_type}  path : {event.src_path}')
        elif event.event_type == EVENT_TYPE_CREATED:
            self.logger.debug(f'new file : {event.src_path}')
            self.manager.found_new_file(event.src_path, 'event_new')
        elif event.event_type == EVENT_TYPE_MODIFIED:
            self.logger.debug(f'modified : {event.src_path}')
            self.manager.found_new_file(event.src_path, 'event_modified')
        elif event.event_type == EVENT_TYPE_MOVED:
            self.logger.debug(f'moved : {event.src_path}')
            self.manager.found_new_file(event.src_path, 'event_moved')
        else:
            self.logger.warning(f'Unknown FS Event : {event.event_type}, {event.src_path}')

if __name__ == "__main__":
    logging.basicConfig(filename='harvester.log', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    HM = HarvesterManager()
    HM.wait()
