#!/bin/bash


if [ "$1" == "-restore" ]
then
  echo "Restore database. This will drop changes and import from DB.sql. "
  echo "WARNING! YOU MUST CLOSE ALL DJANGO INSTANCES OR THIS WILL BREAK EVERTHING HORRIBLY"
  echo "Are you sure? Ctrl-C to cancel."
  read FOO
  echo "Dropping database"
  dropdb battdb
  createdb battdb
  echo "Restoring database"
  psql battdb < DB.sql
else
  echo "Backup database overwrites DB.sql and DB.json. Are you sure? Ctrl-C to cancel."
  echo "Note: This will not include stored timeseries data (this can be restored from CSV files)"
  read FOO
  #echo "Deleting DataRange objects"
  #./manage.py shell < delete_dataranges.py
  echo "Backing up DB"
  ./manage.py graph_models -a -X HasAttributes -o media/images/battDB_visualized.png
  pg_dump battdb --exclude-table "*datarange*" > DB.sql
  ./manage.py dumpdata -e battDB.DataRange --indent 2 > DB.json
fi
