import json
import sys
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_message, send_message, valid_message
from common.consts import DEFAULT_PORT, MAX_CONNECTIONS


def main():
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEFAULT_PORT
        if not 1024 < port < 65635:
            raise ValueError
    except IndexError:
        print("Параметры командной строки: -p <port>")
        sys.exit(1)
    except ValueError:
        print("Значение <port> в диапазоне от 1024 до 65635")

    try:
        if '-a' in sys.argv:
            ip_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            ip_address = ''
    except ValueError:
        print("Параметры командной строки: -a <address>")
        sys.exit(1)

    SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
    SERVER_SOCKET.bind((ip_address, port))
    SERVER_SOCKET.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = SERVER_SOCKET.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = valid_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print("Некорректное сообщение о пользователя")
            client.close()


if __name__ == '__main__':
    main()
