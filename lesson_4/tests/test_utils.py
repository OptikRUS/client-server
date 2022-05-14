from unittest import TestCase

from lesson_4.common.utils import valid_message, create_presence


class TestServer(TestCase):
    bad_400 = {'response': 400, 'error': 'BAD REQUEST'}

    def test_valid_message_200(self):
        self.assertEqual(valid_message({'action': 'presence', 'time': 10,
                                        'user': {'account_name': 'Guest'}}), {'response': 200})

    def test_valid_message_without_time(self):
        self.assertEqual(valid_message({'action': 'presence', 'user': {'account_name': 'Guest'}}), self.bad_400)

    def test_valid_message_without_user(self):
        self.assertEqual(valid_message({'action': 'presence', 'time': 10}), self.bad_400)

    def test_valid_message_without_action(self):
        self.assertEqual(valid_message({'time': 10, 'user': {'account_name': 'Guest'}}), self.bad_400)

    def test_valid_message_empty(self):
        self.assertEqual(valid_message({}), self.bad_400)

    def test_valid_message_wrong_action(self):
        self.assertEqual(valid_message({'action': 'wrong',
                                        'time': 10, 'user': {'account_name': 'Guest'}}), self.bad_400)

    def test_create_presence(self):
        presense = create_presence()
        presense['time'] = 10
        self.assertEqual(presense, {'action': 'presence', 'time': 10, 'user': {'account_name': 'Guest'}})

    def test_create_presence_with_arg(self):
        presense = create_presence('User')
        presense['time'] = 10
        self.assertEqual(presense, {'action': 'presence', 'time': 10, 'user': {'account_name': 'User'}})

    # def test_
