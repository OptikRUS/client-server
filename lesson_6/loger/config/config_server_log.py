import os.path
import sys

import logging.handlers

from common.consts import LOGGING_LEVEL


FORMATTER = logging.Formatter("%(asctime)s %(levelname)-5s %(filename)-10s %(message)s")

PATH = os.path.join(os.path.dirname(__file__), "logs/server.log")

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when="D")
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)
