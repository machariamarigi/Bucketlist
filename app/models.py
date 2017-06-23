"""Module for the application's USER, BUCKETLIST and BUCKETLISTITEMS"""

from flask_login import UserMixin


class User(UserMixin):
    """Class modeling a real world user"""

    def __init__(self, username, email, password):
        """Constructor for user object"""
        self.username = username
        self.email = email
        self.password = password

        self.details = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def get_details(self):
        return self.details


class BucketList(object):
    """Class modeling a bicket list with CRUD operations"""
    all_bucketlists = []

    def __init__(self):
        self.bucketlist = {}
        self.id = 1

    def create_bucketlist(self, title, description):
        """Create bucketlist item"""

        self.bucketlist[title] = description
        self.all_bucketlists.append({
            title: description
        })

    def get_bucketlists(self):
        """Method to get all the bucketlists"""
        return self.all_bucketlists

    def delete_bucketlist(self, key):
        """Method to delete a bucketlist"""
        self.all_bucketlists.pop(key)
        return self.all_bucketlists


class BucketlistItems(BucketList):
    """Class modeling bucket list items with CRUD operations"""
    all_bucketlist_items = []
    items_details = {}

    def create_bucketlist_items(self, title, due_date, done):
        """Method used to populate bucketlist with items"""
        self.items_details[title] = due_date
        self.all_bucketlist_items.append({
            title: done
        })


