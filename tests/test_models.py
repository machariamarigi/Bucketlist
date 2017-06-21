"""Module for testing application's models"""

from unittest import TestCase

from app.models import User, Bucketlist, BucketListItem


class TestUserModel(TestCase):
    """Class containing tests for a user"""

    def setUp(self):
        self.user_instance = User('mash', 'mash@mash.com', 'mash_pass')

    def test_user_get_details(self):
        """Method to test if user instantiates correctly"""
        self.assertEqual(self.user_instance.get_details(), {
            "username": "mash", "email": "mash@mash.com", "password": "mash_pass"
        })


class TestBucketList(TestCase):
    """Class containing tests for Bucketlist"""
    def setUp(self):
        self.bucket_list = Bucketlist()

    def test_create_bucketlist(self):
        intial_bucklists = len(self.bucket_list.bucketlists)
        self.bucket_list.create_bucketlist('Travel', 'Where I want to go')
        final_bucketlist = len(self.bucket_list.bucketlists)
        difference = final_bucketlist - intial_bucklists
        self.assertEquals(difference, 1, "Bucketlist is not created")
