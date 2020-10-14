#!/bin/bash

DIR = $1

inotifywait -e create /tmp -m -r  --format '%w%f' "$DIR" | while read f do
   /usr/bin/env python3 ./harvester_upload.py $f
   
