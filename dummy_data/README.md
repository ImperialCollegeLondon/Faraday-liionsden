# Generating dummy data

There is probably a better way to do this but generating users separately then loading data from other apps seems to be the safest way if starting from a totally fresh database during development.

## Loading data

For (mostly front end) development purposes, you can generated dummy data that is realistic.
This can't be achieved easily with model_bakery which is useful for tests but fills fields with nonsense. From the top directory (above this one) run:

1. Generate a superuser `manage.py createsuperuser <username>`.
2. Generate other users `manage.py shell < dummy_data/generate_users.py`. You can add additional users to `generate_users.py` if you want.
3. load the data `manage.py loaddata dummy_data/dummy_data.json`.

## Saving data as a new fixture

To generate a new version of `dummy_data/dummy_data.json`, run `manage.py dumpdata battDB dfndb common --natural-foreign --indent 2 > dummy_data/new_dummy_data_file.json`.
