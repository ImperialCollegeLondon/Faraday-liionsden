import os
from datetime import datetime, timedelta
from logging import getLogger

from azure.core.exceptions import ResourceNotFoundError
from azure.core.utils import parse_connection_string
from azure.storage.blob import BlobServiceClient, generate_blob_sas
from django.conf import settings

logger = getLogger()


def get_blob_endpoint():
    """
    Returns the blob endpoint for the Azure storage account.
    Detects if the connection string container is for a local emulator.
    If it is, modifies the endpoint to use the localhost.
    TODO: modify based on whether in local dev or production - see download_blob.
    """
    blob_endpoint = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "blobendpoint"
    ]
    if "azurite" in blob_endpoint:
        blob_endpoint = blob_endpoint.replace("azurite", "localhost")
    return blob_endpoint


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
    TODO: This is not used. Remove and replace with a function to get the correct
    blob URL, which are used by the views. Correct URL based on whether in local
    dev or production.
    """
    blob_endpoint = get_blob_endpoint()
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
    blob_endpoint = get_blob_endpoint()
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
    blob_endpoint = get_blob_endpoint()
    account_key = parse_connection_string(settings.AZURE_CONNECTION_STRING)[
        "accountkey"
    ]
    blob_service_client = BlobServiceClient(blob_endpoint, account_key)
    blob_client = blob_service_client.get_container_client(container=container)
    return blob_client.list_blobs()
