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

## Continuous integration and deployment (CI  & CD)

## Azure

## Django configuration
