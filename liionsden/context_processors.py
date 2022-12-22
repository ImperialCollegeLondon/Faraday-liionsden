import os


def export_vars(request):
    data = {}
    data["SETTING_TYPE"] = os.environ["DJANGO_SETTINGS_MODULE"]
    data["PRIVACY_NOTICE_SAS_URL"] = os.environ.get("PRIVACY_NOTICE_SAS_URL")
    return data
