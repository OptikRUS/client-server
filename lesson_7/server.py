import json
import time
import sys
import logging
import argparse
from select import select
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_message, send_message, valid_message
from common.consts import DEFAULT_PORT, MAX_CONNECTIONS, ACTION, MESSAGE, SENDER, TIME, MESSAGE_TEXT
from loger.log_decorators import log
from loger.config import config_server_log

SERVER_LOGGER = logging.getLogger('server')


@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(
            f'Попытка запуска сервера с указанием неподходящего порта {listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)
    return listen_address, listen_port


def main():
    listen_address, listen_port = arg_parser()

    SERVER_LOGGER.info(f"Сервер на порту {listen_port} запущен и ожидает подключения по адресу {listen_port}")

    SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
    SERVER_SOCKET.bind((listen_address, listen_port))
    SERVER_SOCKET.settimeout(.5)

    clients = []
    messages = []

    SERVER_SOCKET.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = SERVER_SOCKET.accept()
        except OSError:
            pass
        else:
            SERVER_LOGGER.info(f"Установлено соединение с: {client_address}")

        recv_data_lst = []
        send_data_lst = []
        err_lst = []

        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    valid_message(get_message(client_with_message), messages, client_with_message)
                except (ValueError, json.JSONDecodeError):
                    SERVER_LOGGER.debug(f"Соединение с клиентом {client_with_message.getpeername()} закрыто.")
                    clients.remove(client_with_message)

        if messages and send_data_lst:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for waiting_client in send_data_lst:
                try:
                    send_message(waiting_client, message)
                except (ValueError, json.JSONDecodeError):
                    SERVER_LOGGER.debug(f"Соединение с клиентом {waiting_client.getpeername()} закрыто.")
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()
