""" Model to test the application's volatile storage """

from unittest import TestCase

from app.tools import Storage


class TestStorage(TestCase):
    """Class to test storage of users, bucketlists and bucketlist items"""

    def setUp(self):
        self.test_store = Storage()

    def test_create_user(self):
        initial_users = len(self.test_store.users)
        self.test_store.add_user('test', 'test@test.com', 'test')
        final_users = len(self.test_store.users)
        self.assertAlmostEquals(
            1, final_users-initial_users, 'User not created')
