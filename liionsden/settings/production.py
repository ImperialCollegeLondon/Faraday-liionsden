import os

from .settings import *  # noqa: F403

DEBUG = False
ALLOWED_HOSTS = ["liionsden.rcs.ic.ac.uk"]
SECRET_KEY = os.environ["SECRET_KEY"]
EMAIL_HOST = "smarthost.cc.ic.ac.uk"
SERVER_EMAIL = "noreply@imperial.ac.uk"
ADMINS = [("Daniel Davies", "d.w.davies@imperial.ac.uk")]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 15552000
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
