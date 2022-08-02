import os
from datetime import datetime, timedelta

from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import (
    BlobServiceClient,
    ContainerSasPermissions,
    generate_container_sas,
)
from storages.backends.azure_storage import AzureStorage

from liionsden.settings import settings


class AzureMediaStorage(AzureStorage):
    account_name = "liionsdenmedia"
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = "liionsdenmedia"
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    azure_container = "static"
    expiration_secs = None


def generate_sas_token():
    """Generates a SAS token for the Azure storage account."""
    try:
        account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
        azure_container = settings.MEDIA_LOCATION
        sas_token = generate_container_sas(
            account_name=settings.AZURE_ACCOUNT_NAME,
            account_key=account_key,
            container_name=azure_container,
            expiry=datetime.utcnow() + timedelta(hours=1),
            permission="r",
        )
        return sas_token
    except ResourceNotFoundError:
        # TODO log something
        return None


def download_blob(local_path="./tmp", blob_name="", sas_token=""):
    """
    Downloads a file from azure and saves it locally given the blob
    name and local file path.
    """
    os.makedirs(os.path.join(local_path, "uploaded_files"), exist_ok=True)
    blob_service_client = BlobServiceClient(settings.AZURE_CUSTOM_DOMAIN, sas_token)
    blob_client = blob_service_client.get_container_client(
        container=settings.MEDIA_LOCATION
    )
    download_path = os.path.join(local_path, blob_name)
    with open(download_path, "wb") as f:
        f.write(blob_client.download_blob(blob_name).readall())
