import os
import sys

DEBUG = True
SECRET_KEY = "thisisnotneeded"


INSTALLED_APPS = [
    "tests.testapp",
    "securepasswords",
]

MIDDLEWARE = []

SITE_ID = 1

MEDIA_PATH = "/media/"
STATIC_URL = "/static/"

ROOT_URLCONF = "tests.testapp.urls"


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"console": {"format": "%(asctime)s %(levelname)-8s %(name)-12s %(message)s"}},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "stream": sys.stdout,
        },
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "securepasswords": {
            "handlers": ["console"],
            "level": os.getenv("SECUREPASSWORDS_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
