#!/usr/bin/env python3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent, EVENT_TYPE_MODIFIED
import os
import sys
import requests
import json
from common.utils import hash_file, has_handle
from threading import Thread
import platform
import yaml
import logging



harverster_config = dict()
DEFAULT_CONFIG = """
database:    # Database connection config 
    auth_token: 52f1021a6e32e4202acab1c5c19f0067cc1ce38a
    host: 127.0.0.1
    port: 8000
    
harvester:
    machine_id: "%s"      # uniquely identifies this harvester client - default is machine's hostname
    min_file_size: 1024   # do not import very small files - 1024 = 1kB
    min_file_age: 60      # do not import files modified very recently (<60s ago) - they are probably still in use
    
folders:   # Configure folders to monitor
 - "default": # default folder config
    {
       recurse: True,                                           # set to True to descend into sub-folders, False otherwise
       auth_token: "52f1021a6e32e4202acab1c5c19f0067cc1ce38a",   # use a different auth token to assign files to a different user. FIXME: this won't work, because the initial list of hashes are currently for one user only, not all users
       experiment_id: 1,                                        # experiment ID to set in the database. Use 'None' to assign later
       file_extensions:                                        # list of file extensions to upload
       [ ".csv", ".tsv", ".mpt" ], 
       parser: "biologic",                                    # choices will be "biologic", "maccor", "ivium", "neware", etc. but currently only biologic is supported 
       columns:                                               # Columns to extract from file:  Not yet implemented - select parser config via website
       [
         "ECell/V": "Cell Voltage",
         "I/mA":    "Current"
       ]
    }
 - "/tmp/harvester-data": 
    {
       recurse: True,                                           # set to True to descend into sub-folders, False otherwise
       auth_token: "52f1021a6e32e4202acab1c5c19f0067cc1ce38a",   # use a different auth token to assign files to a different user. FIXME: this won't work, because the initial list of hashes are currently for one user only, not all users
       experiment_id: 1,                                        # experiment ID to set in the database. Use 'None' to assign later
       file_extensions:                                        # list of file extensions to upload
       [ ".csv", ".tsv", ".mpt" ], 
       parser: "biologic",                                    # choices will be "biologic", "maccor", "ivium", "neware", etc. but currently only biologic is supported 
       columns:                                               # Columns to extract from file:  Not yet implemented - select parser config via website
       [
         "ECell/V": "Cell Voltage",
         "I/mA":    "Current"
       ]
    }
     
""" % platform.uname()[1] or "unknown" # set default machine_id to hostname





class FSMonitor(FileSystemEventHandler):
    def __init__(self, config):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.files_by_hash = dict()
        self.waiting_files = list()
        self.scan_path = config.get()
        #self.API = HarvesterAPI(site="http://ns3122207.ip-54-38-195.eu:10802", auth_token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.API = HarvesterAPI(site="http://localhost:8000",
                                auth_token="52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.check_db_files()
        self.check_local_files(state="exists_local")


    def load_files_list(self):
        try:
            with open(config_file_path, "r") as config_file:
                logging.info("Reading config from %s" % config_file_path)
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            write_config_template(config_file_path)
            return yaml.safe_load(DEFAULT_CONFIG)

    def found_new_file(self, fd):
        fp = self.files_by_name.get(filepath) or None
        if fp is None:  # create new entry in files dict
            fp = dict({'state': state, 'path': filepath, 'size': os.path.getsize(filepath)})
            self.files_by_name[filepath] = fp
            self.logger.info("New file: %s" % fp)
        else: # we've already checked this file before
            if os.path.getsize(filepath) > fp['size']:
                fp['state'] = 'growing'

        if(fp['state'] == 'ignored' or fp['state'] == 'growing' or fp['state'] == 'uploaded'):
            return

        if fp['size'] < MIN_FILE_SIZE:
            #print("%s: Too small - skipping!" % filepath)
            return

        if has_handle(filepath):
            self.logger.info("File [%s] is open in another process - skipping!" % filepath)
            return

        file_age = time.time() - os.path.getmtime(filepath)
        if file_age < MIN_FILE_AGE:
            self.logger.info("File [%s] was modified only %ds ago - waiting!" % (filepath, file_age))
            fp['state'] = 'waiting'
            return
    #     self.consider_upload(filepath)
    #
    # def consider_upload(self, filepath):
        fp = self.files_by_name.get(filepath) or dict()
        state = fp.get('state') or 'new'
        if(state == 'ignored'):
            return

        file_hash = hash_file(open(filepath, "rb"))
        fd = self.files_by_hash.get(file_hash)
        #print("Considering file: %s (%s) - %s" % (filepath, file_hash, state))
        self.logger.info("Considering file: %s " % fd)

        if fd is None: # create new entry in files dict
            fd = fp
            self.files_by_hash[file_hash] = fd
        else: # already existed - check state of existing entry
            if(fd['state'] == 'ignored'):
                return
            if fd['state'] == 'exists_remote':
                logging.info("Already in database: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return
            if fd['state'] == 'exists_local':
                logging.info("Local file system contains duplicates: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return
            if fd['state'] == 'uploaded':
                logging.info("Already in database: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return

        # now we have a file which we think is valid

        fp.update(fd)
#        fd.update(fp)
        ## Process state machine
        self.logger.info("consider_upload: fd=%s" % fd)
        self.files_by_hash[file_hash] = fd
        self.logger.info("Uploading file %s" % filepath)
        try:
            self.API.upload_file(filepath)
        finally:
            fd['state'] = 'uploaded'

    def check_db_files(self):
        file = dict()
        try:
            for file in self.API.get_hashes():
                h = file['hash']
                self.files_by_hash[h] = dict({'state': 'exists_remote'})
            self.logger.info("Database has %d files" % len(self.files_by_hash))
        except requests.exceptions.ConnectionError:
            self.logger.error("Cannot connect to database")
        except (KeyError, TypeError):
            self.logger.warning("Hashes not returned")
            self.logger.debug(file)


    def check_local_files(self, state='new'):
        for root, subFolders, files in os.walk(self.scan_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.found_new_file(file_path)
        self.logger.info("Local machine has %d files" % len(self.files_by_name))

    def check_waiting_files(self):
        self.logger.info("%d files waiting" % len(self.waiting_files))
        for f in self.waiting_files:
            self.recheck_file(f)

    def on_modified(self, event: FileSystemEvent):
        if event.is_directory:
            self.logger.info(f'new file: event type: {event.event_type}  path : {event.src_path}')
        elif event.event_type == EVENT_TYPE_MODIFIED:
            self.logger.info(f'path : {event.src_path}')
            self.found_new_file(event.src_path, 'new')


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
        self.config = self.load_config(config_path)
        logging.debug("Config Loaded: %s" % self.config)
        self.config = self.load_config(config_path)
        self.observers = dict()
        self.observer = Observer()
        self.event_handler = FSMonitor(config=self.config)

        # iterate through paths and attach observers
        for line in paths:
            # convert line into string and strip newline character
            targetPath = str(line).rstrip()
            # Schedules watching of a given path
            observer.schedule(event_handler, targetPath)
            # Add observable to list of observers
            observers.append(observer)

    def start_monitor(self, path: str, config: dict):
        pass

    def start(self):
        # start observer
        self.observer.start()

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

    def load_config(self, config_file_path):
        try:
            with open(config_file_path, "r") as config_file:
                logging.info("Reading config from %s" % config_file_path)
                return yaml.safe_load(config_file)
        except FileNotFoundError:
            self.write_config_template(config_file_path)
            return yaml.safe_load(DEFAULT_CONFIG)


    def write_config_template(self, config_template_path):
        # template = {
        #     "database_authtoken": "52f1021a6e32e4202acab1c5c19f0067cc1ce38a",
        #     "database_host": "127.0.0.1",
        #     "database_port": 8000,
        #     "machine_id": platform.uname()[1],
        #
        # }
        logging.info("Writing default config to %s" % config_template_path)
        with open(config_template_path, "w") as config_file:
            config_file.write(DEFAULT_CONFIG)

if __name__ == "__main__":
    logging.basicConfig(filename='harvester.log', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    HM = HarvesterManager(str(sys.argv[1]))
    logging.info("======= Harvester utility started =========")

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