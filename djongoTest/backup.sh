#!/bin/bash


if [ "$1" == "-restore" ]
then
  echo "Restore database. This will drop changes and import from DB.sql. Are you sure? Ctrl-C to cancel."
  read FOO
  echo "Dropping database"
  #dropdb battdb
  #createdb battdb
  echo "Restoring database"
  #psql battdb < DB.sql
else
  echo "Backup database overwrites DB.sql and DB.json. Are you sure? Ctrl-C to cancel."
  read FOO
  echo "Backing up DB"
  ./manage.py graph_models battDB -X HasAttributes -o media/images/battDB_visualized.png
  pg_dump battdb > DB.sql
  ./manage.py dumpdata --indent 2 > DB.json
fi
