"""Module for testing application's models"""

from unittest import TestCase

from ..app.models import User, Bucketlist, BucketListItem


class TestUserModel(TestCase):
    """Class containing tests for a user"""

    def setUp(self):
        self.user_instance = User('mash', 'mash@mash.com', 'mash_pass')

    def test_user_instance(self):
        """Method to test if user instantiates correctly"""
        self.assertEqual(self.user_instance.get_details(), {
            "username": "mash", "email": "mash@mash.com", "password": "mash_pass"
        })


class TestBucketList(TestCaes):
    """Class containing trsts for Bucketlist"""