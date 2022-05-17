import sys
import json
import logging
from socket import socket, AF_INET, SOCK_STREAM

from common.consts import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import create_presence, valid_answer, get_message, send_message
from logs.config import config_client_log

CLIENT_LOGGER = logging.getLogger('client')


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 1024 < server_port < 65535:
            CLIENT_LOGGER.critical(f"Неверный номер порта: {server_port} Значение <port> в диапазоне от 1024 до 65635")
        CLIENT_LOGGER.info(f"Запущен клиент с адресом {server_address} и портом {server_port}")

    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        CLIENT_LOGGER.debug(f"Будут использованы стандартные адрес {server_address} и порт {server_port}")
        sys.exit(1)

    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect((server_address, server_port))
    message_to_server = create_presence("optikrus")
    send_message(CLIENT_SOCKET, message_to_server)

    try:
        answer = valid_answer(get_message(CLIENT_SOCKET))
        CLIENT_LOGGER.info(f'Ответ от сервера {answer}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical("Не удалось декодировать сообщение")


if __name__ == '__main__':
    main()
