import json
import sys
import time

from loger.log_decorators import log

from .consts import ENCODING, MAX_PACKAGE_LENGTH, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    MESSAGE, MESSAGE_TEXT
from .errors import IncorrectDataRecivedError


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise IncorrectDataRecivedError
    raise IncorrectDataRecivedError


@log
def send_message(socket, message):
    if not isinstance(message, dict):
        raise ValueError
    str_json_data = json.dumps(message)
    encoded_message = str_json_data.encode(ENCODING)
    socket.send(encoded_message)


@log
def valid_message(message, messages_list, client):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and \
            TIME in message and MESSAGE_TEXT in message:
        messages_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return
    else:
        send_message(client, {
            RESPONSE: 400,
            ERROR: 'BAD REQUEST'})


@log
def create_presence(LOGGER, account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def create_message(sock, LOGGER, account_name='Guest'):
    message = input('Введите сообщение для отправки или \'!!!\' для завершения работы: ')
    if message == '!!!':
        sock.close()
        LOGGER.info('Завершение работы по команде пользователя.')
        print('Спасибо за использование нашего сервиса!')
        sys.exit(0)
    message_dict = {
        ACTION: MESSAGE,
        TIME: time.time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: message
    }
    LOGGER.debug(f'Сформирован словарь сообщения: {message_dict}')
    return message_dict
