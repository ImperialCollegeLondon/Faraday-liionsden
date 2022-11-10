import logging
import os
import sys

from .production import *  # noqa: F401, F403

# Configure sending emails from Imperial mail servers
EMAIL_HOST = "smtp.cc.ic.ac.uk"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ["EMAIL_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
SERVER_EMAIL = "rcs-noreply@imperial.ac.uk"
DEFAULT_FROM_EMAIL = "rcs-noreply@imperial.ac.uk"

# Configure database settings for azure
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_NAME"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": 5432,
        # Azure postgres requires connections to be encrypted
        "OPTIONS": {"sslmode": "require"},
    }
}


# Below configuration splits console logging into stdout and stderr (for warnings or
# worse). This helps the Azure AppServiceConsoleLogs mechanism to distinguish between
# error and information messages in the log analytics workspace.
class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "{levelname} {asctime} {message}", "style": "{"},
    },
    "filters": {
        "info_filter": {
            "()": InfoFilter,
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "console_stdout": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": sys.stdout,
            "level": "DEBUG",
            "filters": ["info_filter"],
        },
        "console_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": sys.stderr,
            "level": "WARNING",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "root": {"handlers": ["console_stdout", "console_stderr"]},
    "loggers": {
        "django": {
            "handlers": ["mail_admins"],
            "level": "INFO",
        },
    },
}
