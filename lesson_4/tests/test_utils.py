from unittest import TestCase

from lesson_4.common.utils import valid_message, create_presence, valid_answer
from lesson_4.common.consts import ACTION, ERROR, PRESENCE, TIME, USER, RESPONSE, ACCOUNT_NAME


class TestServer(TestCase):
    bad_400 = {RESPONSE: 400, ERROR: 'BAD REQUEST'}

    def test_valid_message_200(self):
        self.assertEqual(valid_message({ACTION: PRESENCE, TIME: 10,
                                        USER: {ACCOUNT_NAME: 'Guest'}}), {RESPONSE: 200})

    def test_valid_message_without_time(self):
        self.assertEqual(valid_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_valid_message_without_user(self):
        self.assertEqual(valid_message({ACTION: PRESENCE, TIME: 10}), self.bad_400)

    def test_valid_message_without_action(self):
        self.assertEqual(valid_message({TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_valid_message_empty(self):
        self.assertEqual(valid_message({}), self.bad_400)

    def test_valid_message_wrong_action(self):
        self.assertEqual(valid_message({ACTION: 'wrong',
                                        TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}}), self.bad_400)

    def test_create_presence(self):
        presense = create_presence()
        presense[TIME] = 10
        self.assertEqual(presense, {ACTION: PRESENCE, TIME: 10, USER: {ACCOUNT_NAME: 'Guest'}})

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



