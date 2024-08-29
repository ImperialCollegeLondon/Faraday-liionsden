# Infrastructure

## Containerisation

[Docker](https://www.docker.com/) is used to containerise the main app so that it is
always run in the same linux environment. Two other Docker containers are needed in
addition to the main `web` container:

- `db`: A postgres container based on the [official postgres Docker
  image](https://hub.docker.com/_/postgres). This hosts the backend database used by
  Django.
- `azurite`: In production any media files (e.g. raw data files, PDFs etc. uploaded by
  users) are stored in [Azure
  Blob](https://azure.microsoft.com/en-gb/products/storage/blobs) Containers. It is not
  practical nor wise to rely on a cloud container for local development so the [Azurite
  image](https://hub.docker.com/_/microsoft-azure-storage-azurite) is used to run an
  Azure Storage emulator.

The three containers are coordinated using [Docker
Compose](https://docs.docker.com/compose/). The configuration is controlled in the
`docker-compose.yml` file in the top directory.

The `web` container itself is configured in the `Dockerfile`, which details a few extra
steps including running additional scripts in the `scripts/` directory.

### Idiosyncrasies

#### Locally saved postgres database

It should usually be enough to run `docker-compose up --build` and `docker-compose down
--volumes` to start and stop the services.

The `db` container is configures to mount the volume `data/db` to save the database.
This means that when the services are restarted the last known state of the database
is restored. In general this is useful, but if changes are made to the database schema
in Django that are incompatible with the saved data, it will not be possible to start
the services and you will likely see a vague error about an unhealthy database or
similar.

If this happens the easist solution is to delete `data/db` entirely and restart the
service.

**The main time this happens is when checking out a branch on which Django migrations
have been applied that introduce changes which are not reflected in your current
branch.**

## Unit tests

### Test basics

Unit tests are orgainsed by app in the `tests/` directory. We use the `TestCase` class
built in to Django, which is a subclass of the Python `unittest.TestCase` class. More
information can be found in [the Django docs on writing and running
tests](https://docs.djangoproject.com/en/4.1/topics/testing/overview/).

### Model bakery

We make use of [model bakery](https://model-bakery.readthedocs.io/en/latest/) to
generate test fixtures.

### Running tests

Unit tests should be run locally from inside the running container. Run

```bash
docker-compose exec -it web bash
```

to start a bash session inside the container. Then run

```python
python manage.py test
```

to run the tests. You can add the `-v 2` option to get a more verbose
output and you can specify which test(s)) to run as you would with the Python unittest
library, e.g. `python manage.py test tests.battDB.test_views.CreateBatchTest -v 2`.

Unit tests are run automatically as part of the CI actions on GitHub (see below).

## Continuous integration and deployment (CI  & CD)

[GitHub Actions](https://github.com/features/actions) are used to automatically run
three CI/CD steps. This is configured in `.github/worklflows/ci.yml`:

- **QA:** Runs the pre-commit hooks configured in `.pre-commit-config.yaml`. This is run
  every time code is pushed to any branch and ensures that formatting and linting is
  consistent in case the pre-commit hooks were skipped locally.
- **Test:** Builds the python environment and runs all unit tests. This is also run
  every time code is pushed to any branch and only if the QA step passes.
- **Publish:** Builds and pushes a new Docker image of `web` to the GitHub Container
  Registry then deploys that image to the Azure App Service instance of Liionsden. This
  step only runs when changes are merged into the `main` branch and only if the Test
  step passes.

## Azure

The development/production version of the app running on Azure was initially configured
using [Terraform](https://www.terraform.io/) and [this guide on setting up a web
application with
Terraform](https://github.com/ImperialCollegeLondon/terraform_web_app_configuration). We <!-- markdown-link-check-disable-line -->
have followed the "One Time Usage" workflow on that guide so please refer to it and the
Terraform docs if any changes need to be made.

## Django configuration

The core Django configuration settings are defined in `liionsden/settings/settings.py`.
These settings are augmented for production in `liionsden/settings/production.py` and
`liionsden/settings/azure.py`. These changes configure various passwords and e-mail
addresses that are used for production, as well as database and logging settings.
