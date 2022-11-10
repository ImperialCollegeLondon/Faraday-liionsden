from datetime import datetime, timedelta
from logging import getLogger

from azure.core.utils import parse_connection_string
from azure.storage.blob import generate_blob_sas
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
