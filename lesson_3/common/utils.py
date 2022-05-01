import json
import time

from common.consts import ENCODING, MAX_PACKAGE_LENGTH, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR


def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        str_json_response = encoded_response.decode(ENCODING)
        response = json.loads(str_json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(socket, message):
    str_json_data = json.dumps(message)
    encoded_message = str_json_data.encode(ENCODING)
    socket.send(encoded_message)


def valid_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message:
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'BAD REQUEST'
    }


def valid_answer(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return "200 : OK"
        return f"400 : {message[ERROR]}"
    return ValueError


def create_presence(account_name="Guest"):
    return {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {ACCOUNT_NAME: account_name}
    }
