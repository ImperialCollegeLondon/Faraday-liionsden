#!/usr/bin/env python3

import requests
import json

url = "http://127.0.0.1:8000/battDB/upload/"
token = "52f1021a6e32e4202acab1c5c19f0067cc1ce38a"

data = {
    
    }

headers = {'Authorization': 'Token ' + token, "Content-Type": "multipart/form-data"}

#Call REST API
response = requests.put(url, data=data, headers=headers)

#Print Response
print(response.text)
