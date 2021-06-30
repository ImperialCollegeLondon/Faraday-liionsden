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


if os.environ.get("AZURE_WORKFLOW"):
    ALLOWED_HOSTS = ["liionsden.azurewebsites.net"]
    DATABASES["default"]["HOST"] = "liionsden-db.postgres.database.azure.com"
