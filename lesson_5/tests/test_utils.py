from unittest import TestCase
import json

from ..common.utils import valid_message, create_presence, valid_answer, get_message, send_message
from ..common.consts import ACTION, ERROR, PRESENCE, TIME, USER, RESPONSE, ACCOUNT_NAME, ENCODING


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.receved_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.receved_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(TestCase):
    bad_400 = {RESPONSE: 400, ERROR: 'BAD REQUEST'}
    client_send = TestSocket({ACTION: PRESENCE, TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}})
    client_send_bad = TestSocket([PRESENCE, TIME, USER, ACCOUNT_NAME])
    good_resp = {ACTION: PRESENCE, TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}}

    def test_valid_message_200(self):
        self.assertEqual(valid_message(self.good_resp), {RESPONSE: 200})

    def test_valid_message_without_time(self):
        self.assertEqual(valid_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_valid_message_without_user(self):
        self.assertEqual(valid_message({ACTION: PRESENCE, TIME: 10}), self.bad_400)

    def test_valid_message_without_action(self):
        self.assertEqual(valid_message({TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_valid_message_empty(self):
        self.assertEqual(valid_message({}), self.bad_400)

    def test_valid_message_wrong_action(self):
        self.assertEqual(valid_message({ACTION: 'wrong', TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_create_presence(self):
        presense = create_presence()
        presense[TIME] = 10
        self.assertEqual(presense, self.good_resp)

    def test_create_presence_with_arg(self):
        presense = create_presence('User')
        presense[TIME] = 10
        self.assertEqual(presense, {ACTION: PRESENCE, TIME: 10, USER: {ACCOUNT_NAME: 'User'}})

    def test_valid_ok_answer_200(self):
        self.assertEqual(valid_answer({RESPONSE: 200}), "200 : OK")

    def test_valid_bad_answer_400(self):
        self.assertEqual(valid_answer(self.bad_400), "400 : BAD REQUEST")

    def test_valid_bad_answer_without_response(self):
        with self.assertRaises(ValueError):
            valid_answer({ERROR: 'BAD REQUEST'})

    def test_get_message_ok(self):
        self.assertEqual(get_message(self.client_send), self.good_resp)

    def test_get_message_bad_response(self):
        with self.assertRaises(ValueError):
            get_message(self.client_send_bad)

    def test_send_message_ok(self):
        socket = TestSocket(self.good_resp)
        send_message(socket, self.good_resp)
        self.assertEqual(socket.encoded_message, socket.receved_message)

    def test_send_message_missing(self):
        with self.assertRaises(TypeError):
            send_message()
