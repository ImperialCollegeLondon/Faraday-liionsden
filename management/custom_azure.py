from datetime import datetime, timedelta
from logging import getLogger
from urllib.parse import urlparse

from azure.core.utils import parse_connection_string
from azure.storage.blob import generate_blob_sas
from django.conf import settings

logger = getLogger()


def get_blob_url(uploaded_file):
    """
    Returns the blob url of a raw data file in an Azure storage account.
    Detects if a local azurite emulator is being used for local development
    and redirects to the localhost url if so.
    args:
        uploaded_file: UploadedFile object
    returns:
        blob_url: string
    """
    parsed_url = urlparse(uploaded_file.url)

    if urlparse(uploaded_file.url).hostname == "azurite":
        return parsed_url._replace(netloc=f"localhost:{parsed_url.port}").geturl()
    return uploaded_file.url


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
