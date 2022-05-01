from socket import socket, AF_INET, SOCK_STREAM
from common.consts import ENCODING

CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect(('localhost', 8007))
MSG = "Привет, сервер!"
CLIENT_SOCKET.send(MSG.encode(ENCODING))
DATA = CLIENT_SOCKET.recv(4096)
print(f'Сообщение с сервера: "{DATA.decode(ENCODING)}" длиной {len(DATA)} байт')
CLIENT_SOCKET.close()
