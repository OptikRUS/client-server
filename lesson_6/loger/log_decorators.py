import inspect
import sys
import logging


def log(func):
    if sys.argv[0] == 'client.py':
        LOGGER = logging.getLogger('client')
    else:
        LOGGER = logging.getLogger('server')

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        LOGGER.debug(f'Функция {func.__name__} вызвана из модуля {func.__module__.split(".")[-1]}', stacklevel=2)
        return res

    return wrapper
