import os.path
import sys

import logging.handlers

from common.consts import LOGGING_LEVEL


FORMATTER = logging.Formatter("%(asctime)s %(levelname)-10s %(filename)-23s %(message)s")

PATH = os.path.join(os.path.dirname(__file__), "server.log")

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when="D")
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')