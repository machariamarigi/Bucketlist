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
    """ Class containing tests for Bucketlist """

    def setUp(self):
        self.bucketlist_instance = BucketList(
            'Holiday', 'Let us travel the world')

    def tearDown(self):
        del self.bucketlist_instance

    def test_creation_of_bucketlist_and_get_bucketlist(self):

        self.assertEqual(
            self.bucketlist_instance.get_details(),
            {
                "title": "Holiday",
                "description": "Let us travel the world",
                "items": []
            },
        )


class TestBucketlistModel(TestCase):
    """ Class containing tests for BucketlistItems """

    def setUp(self):
        self.bucketlistitem_instance = BucketlistItems(
            "Cook a pizza", "12th Nov 2017")

    def test_instance_of_bucketlist_item_and_get_bucketlist_item(self):
        self.assertEqual(
            self.bucketlistitem_instance.get_details(),
            {
                'item': "Cook a pizza",
                'duedate': "12th Nov 2017",
                'finished': False
            }
        )

