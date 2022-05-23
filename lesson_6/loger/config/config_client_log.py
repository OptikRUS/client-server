import logging
import os.path
import sys

from common.consts import LOGGING_LEVEL


FORMATTER = logging.Formatter("%(asctime)s %(levelname)-10s %(name)-23s %(message)s")

PATH = os.path.join(os.path.dirname(__file__), "logs/client.log")

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)
