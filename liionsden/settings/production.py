import os

from .settings import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = ["liionsden.rcs.ic.ac.uk"]
SECRET_KEY = os.environ["SECRET_KEY"]
EMAIL_HOST = "smarthost.cc.ic.ac.uk"
SERVER_EMAIL = "noreply@imperial.ac.uk"
ADMINS = [("Diego Alonso Álvarez", "d.alonso-alvarez@imperial.ac.uk")]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 15552000
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


if os.environ.get("WEBSITE_HOSTNAME") == "liionsden.azurewebsites.net":
    ALLOWED_HOSTS = ["liionsden.azurewebsites.net"]
    DATABASES["default"]["HOST"] = os.environ["AZURE_POSTGRESQL_HOST"]
    DATABASES["default"]["USER"] = os.environ["AZURE_POSTGRESQL_USER"]
    DATABASES["default"]["PASSWORD"] = os.environ["AZURE_POSTGRESQL_PASS"]
    DATABSES["default"]["NAME"] = os.environ["AZURE_POSTGRESQL_NAME"]
    DATABSES["default"]["OPTIONS"] = {"sslmode": "require"}
