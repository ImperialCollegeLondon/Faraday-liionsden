import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create container in configured Azure blob storage"

    def handle(self, *args, **options):
        from azure.core.exceptions import ResourceExistsError
        from azure.storage.blob import BlobServiceClient
        from django.conf import settings

        if not (settings.AZURE_CONNECTION_STRING and settings.AZURE_CONTAINER):
            logger.warn("Azure storage settings not configured. Giving up.")
            return

        blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_CONNECTION_STRING
        )
        container_client = blob_service_client.get_container_client(
            settings.AZURE_CONTAINER
        )
        if not container_client.exists():
            try:
                container_client.create_container()
            except ResourceExistsError:
                # guard against highly unlikely race condition
                pass
