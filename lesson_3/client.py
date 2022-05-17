import sys
import json
from socket import socket, AF_INET, SOCK_STREAM

from common.consts import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import create_presence, valid_answer, get_message, send_message


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 1024 < server_port < 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print("Значение <port> в диапазоне от 1024 до 65635")
        sys.exit(1)

    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect((server_address, server_port))
    message_to_server = create_presence("optikrus")
    send_message(CLIENT_SOCKET, message_to_server)

    try:
        answer = valid_answer(get_message(CLIENT_SOCKET))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print("Сообщение с сервера не декодировано")


if __name__ == '__main__':
    main()
