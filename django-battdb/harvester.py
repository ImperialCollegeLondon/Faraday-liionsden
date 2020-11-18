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

MIN_FILE_SIZE = 1024  # do not import very small files - 1024 = 1kB
MIN_FILE_AGE = 60     # do not import files modified very recently (<60s ago) - they are probably still in use


class MyHandler(FileSystemEventHandler):
    def __init__(self, path):
        super().__init__()
        self.files_by_hash = dict()
        self.files_by_name = dict()
        self.scan_path = path
        self.API = HarvesterAPI(site="http://127.0.0.1:8000", auth_token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a")
        self.check_db_files()
        self.check_local_files(state="exists_local")

    def found_new_file(self, filepath, state):
        fp = self.files_by_name.get(filepath)
        if fp is None:  # create new entry in files dict
            fp = dict({'state': state, 'path': filepath, 'size': os.path.getsize(filepath)})
            self.files_by_name[filepath] = fp
        else: # we've already checked this file before
            if os.path.getsize(filepath) > fp['size']:
                fp['state'] = 'growing'

        if(fp['state'] == 'ignored' or fp['state'] == 'growing' or fp['state'] == 'uploaded'):
            return

        if fp['size'] < MIN_FILE_SIZE:
            #print("%s: Too small - skipping!" % filepath)
            return

        if has_handle(filepath):
            print("File [%s] is open in another process - skipping!" % filepath)
            return

        file_age = time.time() - os.path.getmtime(filepath)
        if file_age < MIN_FILE_AGE:
            print("File [%s] was modified only %ds ago - waiting!" % (filepath, file_age))
            return
    #     self.consider_upload(filepath)
    #
    # def consider_upload(self, filepath):
        fp = self.files_by_name.get(filepath) or dict()
        state = fp.get('state') or 'new'
        file_hash = hash_file(open(filepath, "rb"))
        fd = self.files_by_hash.get(file_hash)
        print("Considering file: %s (%s) - %s" % (filepath, file_hash, state))

        if fd is None: # create new entry in files dict
            fd = fp
            self.files_by_hash[file_hash] = fd
        else: # already existed - check state of existing entry
            if(fd['state'] == 'ignored'):
                return
            if fd['state'] == 'exists_remote':
                print("Already in database: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return
            if fd['state'] == 'exists_local':
                print("Local file system contains duplicates: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return
            if fd['state'] == 'uploaded':
                print("Already in database: %s will be ignored" % filepath)
                fd['state'] = 'ignored'
                return

        # now we have a file which we think is valid

        fd.update(fp)
        ## Process state machine
        print("consider_upload: fd=%s" % fd)
        self.files_by_hash[file_hash] = fd
        print("Uploading file %s" % filepath)
        try:
            self.API.upload_file(filepath)
        finally:
            fd['state'] = 'uploaded'

    def check_db_files(self):
        for file in self.API.get_hashes():
            h = file['hash']
            self.files_by_hash[h] = dict({'state': 'exists_remote'})
        print("Database has %d files" % len(self.files_by_hash))

    def check_local_files(self, state='new'):
        for root, subFolders, files in os.walk(self.scan_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                self.found_new_file(file_path, state=state)
        print("Local machine has %d files" % len(self.files_by_name))

    def check_waiting_files(self):
        waiting_files = [f for f in self.files_by_name if f.get('state') == 'waiting']
        print("%d files waiting" % len(waiting_files))
        for f in waiting_files:
            self.found_new_file(f, 'checked')

    def on_modified(self, event: FileSystemEvent):
        if event.is_directory:
            print(f'new file: event type: {event.event_type}  path : {event.src_path}')
        elif event.event_type == EVENT_TYPE_MODIFIED:
            print(f'path : {event.src_path}')
            self.found_new_file(event.src_path, 'new')



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


class CheckTimer(Thread):
    def __init__(self,  h: MyHandler, t: float = 1):
        self.handler = h
        self.wait_time = t
        super(CheckTimer, self).__init__()

    def run(self):
        while(True):
            time.sleep(self.wait_time)
            self.handler.check_local_files()


if __name__ == "__main__":
    scan_path=sys.argv[1]
    event_handler = MyHandler(path=scan_path)
    observer = Observer()
    observer.schedule(event_handler, path=scan_path, recursive=True)
    observer.start()
    timer = CheckTimer(event_handler)
    timer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()