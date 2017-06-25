""" Model to test the application's volatile storage """

from unittest import TestCase

from app.tools import Storage


class TestStorage(TestCase):
    """Class to test storage of users, bucketlists and bucketlist items"""

    def setUp(self):
        self.test_store = Storage()

    def test_create_user(self):
        """Test if we can add new users into the system"""
        initial_users = len(self.test_store.users)
        self.test_store.add_user('test', 'test@test.com', 'test')
        final_users = len(self.test_store.users)
        self.assertEquals(
            1, final_users-initial_users, 'User not created')

    def test_create_bucketlist(self):
        """Test to see if we can add a new bucketlist"""
        initial_bucketlists = len(self.test_store.bucketlists)
        self.test_store.add_bucketlist('travel', 'visit london')
        final_bucketlists = len(self.test_store.bucketlists)
        self.assertEquals(
            1, final_bucketlists-initial_bucketlists, 'User not created')
