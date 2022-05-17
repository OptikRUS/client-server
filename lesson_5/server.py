import json
import sys
import logging
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_message, send_message, valid_message
from common.consts import DEFAULT_PORT, MAX_CONNECTIONS
from logging.config import config_server_log

SERVER_LOGGER = logging.getLogger('server')


def main():
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEFAULT_PORT
        if not 1024 < port < 65635:
            SERVER_LOGGER.critical(f"Указанный порт {port}. Значение <port> в диапазоне от 1024 до 65635")
            raise ValueError
    except IndexError:
        SERVER_LOGGER.critical("Параметры командной строки: -p <port>")

    try:
        if '-a' in sys.argv:
            ip_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            ip_address = ''
    except ValueError:
        SERVER_LOGGER.critical("Параметры командной строки: -a <address>")
    except IndexError:
        SERVER_LOGGER.critical("Отсутстввует параметр <address> после -a")
        sys.exit(1)

    SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
    SERVER_SOCKET.bind((ip_address, port))
    SERVER_SOCKET.listen(MAX_CONNECTIONS)
    SERVER_LOGGER.debug(f"Сервер {ip_address} {port} запущен и ожидает подключения")

    while True:
        client, client_address = SERVER_SOCKET.accept()
        SERVER_LOGGER.info(f"Установлено соединение с: {client_address}")
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f"Получено сообщение от клиента {message_from_client}")
            response = valid_message(message_from_client)
            SERVER_LOGGER.info(f"Ответ клиенту {response}")
            send_message(client, response)
            SERVER_LOGGER.debug(f"соединение с клиентом {client_address} закрыто")
            client.close()
        except (ValueError, json.JSONDecodeError):
            SERVER_LOGGER.error("Не удалось декодировать сообщение от пользователя")
            SERVER_LOGGER.debug(f"соединение с клиентом {client_address} закрыто")
            client.close()


if __name__ == '__main__':
    main()
