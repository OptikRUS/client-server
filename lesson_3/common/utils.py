import json

from consts import ENCODING, MAX_PACKAGE_LENGTH


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
