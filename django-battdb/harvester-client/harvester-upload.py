#!/usr/bin/env python3

import requests
import json
import sys
import os


class HarvesterUploader:

    token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a"

    def upload_file(pathname):

        (dirname, filename) = os.path.split(pathname)
        url = "http://127.0.0.1:8000/battDB/upload/" + filename

        headers = {'Authorization': 'Token ' + token, "Content-Type": "application/octet-stream"}
        # "Content-Disposition": "attachment; filename=foo"}

        # Call REST API
        response = requests.put(url, data=open(arg,'rb'), headers=headers)

        # Print Response
        print(response.text)
