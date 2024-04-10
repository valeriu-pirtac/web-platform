import sys

from loguru import logger as LOG

API_VERSION = 1.0
API_PREFIX = f"/api/{API_VERSION}"

LOGGER_CONFIG = {
    "handlers": [
        {"sink": sys.stdout},
    ],
    "extra": {},
}

LOG.configure(**LOGGER_CONFIG)
