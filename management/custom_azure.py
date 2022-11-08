import os
from datetime import datetime, timedelta
from logging import getLogger

from azure.core.exceptions import ResourceNotFoundError
from azure.core.utils import parse_connection_string
from azure.storage.blob import BlobServiceClient, generate_blob_sas
from django.conf import settings

logger = getLogger()


def generate_sas_token(blob_name, permission="r"):
    """
    Generates a SAS token for the Azure storage account.
    Permissions are read only and expiry 1 hour for now.
    """
    account_key = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "accountkey"
    ]
    azure_container = settings.AZURE_CONTAINER
    sas_token = generate_blob_sas(
        account_name=settings.AZURE_ACCOUNT_NAME,
        account_key=account_key,
        container_name=azure_container,
        blob_name=blob_name,
        expiry=datetime.utcnow() + timedelta(hours=1),
        permission=permission,
    )

    return sas_token


def download_blob(local_path="./tmp", blob_name="", sas_token=""):
    """
    Downloads a file from azure and saves it locally given the blob
    name and local file path.
    """
    blob_endpoint = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "blobendpoint"
    ]
    try:
        os.makedirs(os.path.join(local_path, "uploaded_files"), exist_ok=True)
        blob_service_client = BlobServiceClient(blob_endpoint, sas_token)
        blob_client = blob_service_client.get_container_client(
            container=settings.AZURE_CONTAINER
        )
        download_path = os.path.join(local_path, blob_name)
        with open(download_path, "wb") as f:
            f.write(blob_client.download_blob(blob_name).readall())

        return download_path

    except ResourceNotFoundError:
        logger.error(
            f"Could not find blob {blob_name} in container {settings.AZURE_CONTAINER}"
        )
        return None


def delete_blobs(blob_names, container):
    """
    Deletes the given blobs from the Azure storage account.
    """
    blob_endpoint = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "blobendpoint"
    ]
    account_key = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "accountkey"
    ]
    blob_service_client = BlobServiceClient(blob_endpoint, account_key)
    blob_client = blob_service_client.get_container_client(container=container)
    for blob_name in blob_names:
        blob_client.delete_blob(blob_name)
    return blob_names


def list_blobs(container):
    """
    Lists all the blobs in the Azure storage account.
    """
    blob_endpoint = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "blobendpoint"
    ]
    account_key = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "accountkey"
    ]
    blob_service_client = BlobServiceClient(blob_endpoint, account_key)
    blob_client = blob_service_client.get_container_client(container=container)
    return blob_client.list_blobs()
