"""Module for testing application's models"""

from unittest import TestCase

from app.models import User, BucketList, BucketlistItems


class TestUserModel(TestCase):
    """Class containing tests for a user"""

    def setUp(self):
        self.user_instance = User('mash', 'mash@mash.com', 'mash_pass')

    def test_user_get_details(self):
        """Method to test if user instantiates correctly"""
        self.assertEqual(self.user_instance.get_details(), {
            "username": "mash",
            "email": "mash@mash.com",
            "password": "mash_pass"
        })


class TestBucketlistModel(TestCase):
    """Class containing tests for Bucketlist """

    def setUp(self):
        self.bucketlist_instance = BucketList()

    def tearDown(self):
        del self.bucketlist_instance

    def test_creation_of_bucketlist_and_get_bucketlist(self):

        self.bucketlist_instance.create_bucketlist(
            'Holiday', 'Let us travel the world')
        self.assertEqual(
            self.bucketlist_instance.get_bucketlists(),
            [{"Holiday": "Let us travel the world"}],
            "Bucketlist not created")

    # def test_edit_bucketlist(self):
    #     self.bucketlist_instance.clear_bucketlist()
    #     self.bucketlist_instance.create_bucketlist(
    #         'Holiday', 'Let us travel the world')
    #     self.bucketlist_instance.edit_bucketlist(0, 'Sports', 'Visit Anfield')
    #     self.assertEquals(
    #         self.bucketlist_instance.get_bucketlists(),
    #         [{'Sports': 'Visit Anfield'}],
    #         'Cannot update bucketlist'
    #     )
