from socket import socket, AF_INET, SOCK_STREAM
from common.consts import ENCODING

SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(('', 8007))
SERVER_SOCKET.listen(1)

try:
    while True:
        CLIENT_SOCK, ADDR = SERVER_SOCKET.accept()
        DATA = CLIENT_SOCK.recv(4096)
        print(f'Сообщение "{DATA.decode(ENCODING)}" было отправлено клиентом: {ADDR}')
        MSG = "Привет, клиент"
        CLIENT_SOCK.send(MSG.encode(ENCODING))
        CLIENT_SOCK.close()
finally:
    SERVER_SOCKET.close()
