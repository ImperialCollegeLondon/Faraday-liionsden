# External Python packages and Django apps

Here is a brief summary of how and where imported Python packages and Django apps are used in the code.

## Django apps

- django-jsoneditor: unused?
- [django-rest-framework](https://www.django-rest-framework.org/): Some views are written using DRF but these are not used.
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/): Enables various extra Django management commands.
- [django-ipware](https://pypi.org/project/django-ipware/): unused?
- [django-mptt](https://django-mptt.readthedocs.io/en/latest/): Allows for modified preorder tree traversal in models. This is used for the DeviceSPecification model so that hierarchical structures of single cells, packs and modules can be defined.
- [django-guardian](https://django-guardian.readthedocs.io/en/stable/): Object level permissions.
- [django-bootstrap-v5](https://pypi.org/project/django-bootstrap-v5/): Blend bootstrap v5 with Django for clean and reactive frontend pages.
- [django-tables2](https://django-tables2.readthedocs.io/en/latest/): Creating HTML tables for searching through lists of models.
- [django-cleanup](https://pypi.org/project/django-cleanup/): Automatically deletes/changes files for FileField when the model with that fielfield is deleted/changed.
- [django-better-admin-arrayfield](https://pypi.org/project/django-better-admin-arrayfield/): Improves the arrayfield interface in the admin site.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used for all frontend forms.
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/): Links crispy forms and bootstrap5 within Django so that forms fit in with the bootstrap5 look and behaviour of the rest of the frontend.
- [django-bootstrap-datepicker-plus](https://pypi.org/project/django-bootstrap-datepicker-plus/): Used to allow users to pick date and time interactively using a widget in forms, rather than typing in DD-MM-YYYY format etc.
- [django-filter](https://django-filter.readthedocs.io/en/stable/): Used to filter the queryset for the TableViews, allowing users to search for objects using the form at the top of the page.
- [django-storages[azure]](https://django-storages.readthedocs.io/en/latest/): Allows us to use the Azure blob storage backend for files.
- [django-override-storage](https://pypi.org/project/django-override-storage/): Allows to override the file storage from Azure blob storage to local file storage, for example. Mostly useful for testing.

## Other Python packages

- [pandas](https://pandas.pydata.org/): Used throughout for handling time-series data.
- [preparenovonix](https://pypi.org/project/preparenovonix/): Can handle common issues encountered in data files generated with a range of software versions from the Novonix battery-testers, but novonix parsing has not been implemented yet.
- pyYAML: Used to parse biologic header files.
- [xlrd](https://xlrd.readthedocs.io/en/latest/): Used to read Excel spreadhseets of Maccor data.
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/): Used to read Excel spreadsheets of Maccor data.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): Needed for postgreSQL backend.
- [coreapi-cli](https://www.coreapi.org/tools-and-resources/command-line-client/): Useful for Django REST Framework?
- [idutils](https://pypi.org/project/idutils/): Used for DOI validation.
- [whitenoise](https://whitenoise.evans.io/en/latest/): Middleware.
- [model_bakery](https://model-bakery.readthedocs.io/en/latest/): Fixtures for tests in Django.
- [python-magic](https://pypi.org/project/python-magic/): Used to identify the extension and MIME type of files to see if they are valid for e.g. parsing.
- [tablib](https://tablib.readthedocs.io/en/stable/): You must have tablib installed in order to use the django-tables2 export functionality.
- [molmass](https://pypi.org/project/molmass/): Used to automatically calculate the chemical formula of compounds.
- [plotly](https://plotly.com/python/): Used to generate interactive plots of parsed data.
- [oauthlib](https://github.com/oauthlib/oauthlib): Python OAuth framework. Required by django-storages[azure] and version specified due to dependabot security recommendation.
- [pillow](https://pillow.readthedocs.io/en/stable/): Image processing library. Required by matplotlib and version specified due to dependabot security recommendation.
- [cryptography](https://cryptography.io/en/latest/): Required by django-storages[azure] and version specified due to dependabot security recommendation.
- [debugpy](https://github.com/microsoft/debugpy): Used to enable debug sessions in VS Code when Django is running in a Docker container.
