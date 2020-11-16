#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent, EVENT_TYPE_MODIFIED
import os
import requests
import json
from common.utils import hash_file, has_handle

MIN_FILE_SIZE = 1024


class MyHandler(FileSystemEventHandler):
    def __init__(self, path):
        super().__init__()
        self.scan_path=path
        self.API = HarvesterAPI(site="http://127.0.0.1:8000", auth_token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.hash_list = [d['hash'] for d in self.API.get_hashes()]
        print("existing hashes in database: %s" % self.hash_list)
        print("Scanning filesystem from %s", self.scan_path)
        self.scan_files(scan_path)

    def found_new_file(self, file):
        file_hash = hash_file(open(file, "rb"))
        try:
            if os.path.getsize(file) < MIN_FILE_SIZE:
                print("%s: Too small" % file)
            elif has_handle(file):
                print("File [%s] is open in another process - skipping!" % file)
            elif file_hash in self.hash_list:
                print("Already in database: %s will be ignored" % file)
            else:
                print("Uploading file %s" % file)
                self.API.upload_file(file)
        finally:
            self.hash_list.append(file_hash)

    def scan_files(self,scan_path):
        for root, subFolders, files in os.walk(scan_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.found_new_file(file_path)


    def on_modified(self, event: FileSystemEvent):
        if event.is_directory:
            print(f'new file: event type: {event.event_type}  path : {event.src_path}')
        elif event.event_type == EVENT_TYPE_MODIFIED:
            print(f'path : {event.src_path}')
            self.found_new_file(event.src_path)



class HarvesterAPI:

    def __init__(self, site, auth_token):
        self.token = auth_token
        self.base_url = site

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
        print(response.text)



if __name__ == "__main__":
    scan_path="/tmp/data"
    event_handler = MyHandler(path=scan_path)
    observer = Observer()
    observer.schedule(event_handler, path=scan_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()