#!/usr/bin/env python3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent, EVENT_TYPE_MODIFIED, EVENT_TYPE_CREATED, EVENT_TYPE_MOVED
import os
import sys
import requests
import json
from common.utils import hash_file, has_handle
from threading import Thread
import platform
import yaml
import logging
from dataclasses import dataclass

from .harvester import CONFIG

# schema for info about files in local filesystem
@dataclass
class FileObj:
    hash: str = ""
    path: str = ""
    size: int = 0
    ignored: bool = False
    state: str = "default"

    def check(self):
        pass


class FSMonitor(FileSystemEventHandler):
    def __init__(self, config):
        super().__init__()
        self.harvester_config = config.get('harvester')
        self.logger = logging.getLogger(self.__class__.__name__)

        self.scan_path = config.get()
        #self.API = HarvesterAPI(site="http://ns3122207.ip-54-38-195.eu:10802", auth_token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.API = HarvesterAPI(site="http://localhost:8000",
                                auth_token="52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.check_db_files()
        self.check_local_files(source="exists_local")

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
        if os.path.splitext(filepath)[1].upper() not in [".CSV", ".TSV", ".MPT"]: # TODO: check config.file_patterns for this folder!
            self.logger.debug("Wrong pattern: %s" % filepath)
            return None
        if filepath in self.local_files_by_path.keys():
            self.logger.error("New path twice! %s" % filepath)
            # raise ValueError("New path twice!")
            # return None
        fd = FileObj(state=source)
        self.local_files_by_path[filepath] = fd
        self.logger.debug("New file: %s" % filepath)
        return fd

    def process_file(self, fd):

        if fd.ignored:
            self.logger.debug("Ignored: %s", fd.path)
            return fd

        size = os.path.getsize(fd.path)

        if size < self.harvester_config['min_file_size']:
            fd.state = "too_small"
            self.logger.debug("%s: Too small - skipping!" % fd.path)
            return fd

        if size > fd.size:
            fd.size = size
            fd.state = 'growing'
            self.logger.info("Growing: %s", fd.path)
            return fd

        # check if file is open
        if has_handle(fd.path):
            fd.state = "has_handle"
            self.logger.info("File [%s] is open in another process - skipping!" % fd.path)
            return fd

        # check minimum age
        file_age = time.time() - os.path.getmtime(fd.path)
        if file_age < self.harvester_config['min_file_age']:
            self.logger.info("File [%s] was modified only %ds ago - waiting!" % (fd.path, file_age))
            fd.state = 'waiting'
            return fd

        # compute hash
        file_hash = hash_file(open(fd.path, "rb"))
        self.logger.debug("Computed file hash for %s: %s" % (fd.path, fd.hash))
        if not fd.hash:
            fd.hash = file_hash
        elif file_hash is not fd.hash:
            self.logger.warning("File hash changed for %s" % fd.path)
            fd.hash = file_hash
        else:
            self.logger.warning("Computed hash twice for %s" % fd.path)

        # check if it exists in the list of hashes we got from the server
        remote_file = self.remote_files_by_hash.get(fd.hash)
        if remote_file is not None:
            logging.warning("Already in database: " % fd.path)
            fd.state = 'exists_remote'
            fd.ignored = True
            return fd

        # Try to upload
        self.logger.info("Uploading file %s" % fd.path)
        try:
            self.API.upload_file(fd.path)
        except requests.exceptions.RequestException:
            fd.state = 'upload_failed'
            return fd # try again
        finally:
            fd.state = 'uploaded'
            fd.ignored = True
            self.remote_files_by_hash[fd.hash] = fd
            return fd

    def check_db_files(self):
        file = dict()
        try:
            for file in self.API.get_hashes():
                h = file['hash']
                self.remote_files_by_hash[h] = FileObj(state="exists_remote", hash=h)
            self.logger.info("Database has %d files" % len(self.remote_files_by_hash))
        except requests.exceptions.ConnectionError:
            self.logger.error("Cannot connect to database")
        except (KeyError, TypeError):
            self.logger.warning("Hashes not returned")
            self.logger.debug(file)

    def check_local_files(self, source="found_local"):
        for root, subFolders, files in os.walk(self.scan_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.found_new_file(file_path, source)
        self.logger.info("Local machine has %d files" % len(self.local_files_by_path))

    def check_waiting_files(self):
        self.logger.info("%d files waiting" % len(self.local_files_by_path))
        for fd in self.local_files_by_path:
            self.process_file(fd)

    def on_modified(self, event: FileSystemEvent):
        if event.is_directory:
            self.logger.debug(f'new file: event type: {event.event_type}  path : {event.src_path}')
        elif event.event_type == EVENT_TYPE_CREATED:
            self.logger.debug(f'new file : {event.src_path}')
            self.found_new_file(event.src_path, 'event_new')
        elif event.event_type == EVENT_TYPE_MODIFIED:
            self.logger.debug(f'modified : {event.src_path}')
            self.found_new_file(event.src_path, 'event_modified')
        elif event.event_type == EVENT_TYPE_MOVED:
            self.logger.debug(f'moved : {event.src_path}')
            self.found_new_file(event.src_path, 'event_moved')
        else:
            self.logger.warning(f'Unknown FS Event : {event.event_type}, {event.src_path}')


class HarvesterAPI:

    def __init__(self, site, auth_token):
        self.token = auth_token
        self.base_url = site
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_hashes(self):
        url = self.base_url + "/api/hash_list"
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
        return json.loads(response.text)

    def create_datafile_record(self, file_obj):
        pass


class QueueManager(Thread):
    def __init__(self,  h: FSMonitor, t: float = 1):
        self.handler = h
        self.wait_time = t
        super(QueueManager, self).__init__()

    def run(self):
        while(True):
            time.sleep(self.wait_time)
            self.handler.check_waiting_files()


class HarvesterManager:
    def __init__(self, config_path: str):
        logging.info("======= Harvester utility started =========")
        # self.config = self.load_config(config_path)
        # logging.debug("Config Loaded: %s" % self.config)
        # self.config = self.load_config(config_path)
        self.observers = dict()
        observer = Observer()
        self.event_handler = FSMonitor(config=self.config)
        self.remote_files_by_hash = dict()
        self.local_files_by_path = dict()
        self.waiting_files = list()

        # iterate through paths and attach observers
        for folder in CONFIG.folders:
            # convert line into string and strip newline character
            targetPath = str(folder.path).rstrip()
            # Schedules watching of a given path
            observer.schedule(self.event_handler, targetPath)
            # Add observable to list of observers
            self.observers[targetPath] = observer

        # start observer
        observer.start()

    def wait(self):
        logging.info("== Waiting for files ==")
        try:
            while True:
                # poll every second
                time.sleep(1)
        except KeyboardInterrupt:
            for o in self.observers:
                o.unschedule_all()
                # stop observer if interrupted
                o.stop()
        for o in self.observers:
            # Wait until the thread terminates before exit
            o.join()

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

if __name__ == "__main__":
    logging.basicConfig(filename='harvester.log', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("======= Harvester utility started =========")
    HM = HarvesterManager(str(sys.argv[1]))



    observer.schedule(event_handler, path=scan_path, recursive=True)
    observer.start()
    timer = QueueManager(event_handler)
    timer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()