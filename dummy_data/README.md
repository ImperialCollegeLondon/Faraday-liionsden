# Generating dummy data

## Loading data

For (mostly front end) development purposes, you can load some dummy data from file to avoid having to manually create lots of foreign key objects to satisfy required fields.
From the top directory (above this one) run `manage.py loaddata dummy_data/dummy_data.json`.

## Saving data as a new fixture

To generate a new version of `dummy_data/dummy_data.json` from a populated database run `manage.py dumpdata battDB dfndb common --natural-foreign --indent 2 > dummy_data/new_dummy_data_file.json`.
