#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Get environment variables to show up in SSH session
eval $(printenv | awk -F= '{print "export " "\""$1"\"""=""\""$2"\"" }' >> /etc/profile)
