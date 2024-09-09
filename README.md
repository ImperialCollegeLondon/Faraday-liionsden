# Liionsden

:warning: **Liionsden is currently in development** :warning:

Liionsden is a platform for storing data about lithium-ion batteries and their performance. It automatically parses data from the output files of battery cycler machines and stores this information in a database, associating it with specific experiments and devices. Metadata is stored about specific experiments, batches of devices and individual devices.

The development server is running [here](https://liionsden.rcs.ic.ac.uk/) (internal to Imperial College). <!-- markdown-link-check-disable-line -->

It will be possible to browse the database, as well as add to it, via a web-app and programatically via an API.

Liionsden is developed at Imperial College London, funded by the [Faraday Institution Multi-scale Modelling Project](https://www.faraday.ac.uk/research/lithium-ion/battery-system-modelling/).

## Database structure

The database currently stores recorded cycler data along with metadata about:

- **Experiments:** protocol, equipment used, configuration...
- **Devices:** batch number, specification, chemical composition...

A simplified version of the main `battDB` app is shown below. This does not include models in the `common` and `dfndb` app, which deal with data relating to users, organisations, components, parameters, methods.

![database graph](graph.png)

## Usage

Public data in the database can be browsed using the web platform. Registered "contributor" users can add experimental data, register equipment and batches of devices via the web platform.

In future, this will also be posible via the API.

## Local installation

If you want to run a local version of Liionsden, we recommend using [Docker](https://www.docker.com/). A `docker-compose.yml` is provided to include all the required environment variables and containers.
To start the app, run `docker compose up --build`.

Dummy data can be loaded by running `manage.py loaddata dummy_data/dummy_data.json` from inside the web application container.

Full instructions to follow once the platform is in production.

## Development notes

Development documentation is ongoing and can be found [in the relevant docs subdirectory](https://github.com/ImperialCollegeLondon/Faraday-liionsden/tree/develop/docs/development).

Some general hints and potential gotchas:

- To run Django management commands, you will need to execute them inside the container, ie `docker-compose exec web python manage.py showmigrations`.
- For local development, the password for the admin user is set as `password` in an [initial migration](https://github.com/ImperialCollegeLondon/Faraday-liionsden/blob/develop/management/migrations/0004_add_superuser.py). This comes from an environment variable [set in docker-compose.yml](https://github.com/ImperialCollegeLondon/Faraday-liionsden/blob/develop/docker-compose.yml#L36).
- If the `web` container won't start it may be because changes have been made such that the existing postgres database is incompatible with the Django code. The database is stored locally in `data/db` and persists after Docker is shutfown, so completely remove that directory and try again.

### Contribution guidelines

We are following the [pip-tools](https://pypi.org/project/pip-tools/) `pip-compile`
convetion to generate `requirements.txt` and `requirements-dev.txt` from
`pyproject.toml` for dependencies and development dependencies, respectively.

### Related open-source software

- [Galvanalyser](https://github.com/Battery-Intelligence-Lab/galvanalyser)
- [Liiondb](https://github.com/ndrewwang/liiondb) ([web app](http://www.liiondb.com/))
- [PyBaMM](https://www.pybamm.org/)

### TODOs

Generally development TODOs should be tracked in [issues](https://github.com/ImperialCollegeLondon/Faraday-liionsden/issues) and/or [project board](https://github.com/ImperialCollegeLondon/Faraday-liionsden/projects/1). <!-- markdown-link-check-disable-line -->
