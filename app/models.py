"""Module for the application's USER, BUCKETLIST and BUCKETLISTITEMS"""


class User():
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
    """Class modeling a bucket list with CRUD operations"""

    def __init__(self, title, description, items=None):
        """Create bucketlist item"""
        self.title = title
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items

        self.details = {
            'title': self.title,
            'description': self.description,
            'items': self.items
        }

    def get_details(self):
        """Method to get all the bucketlists"""
        return self.details


class BucketlistItems(BucketList):
    """Class modeling bucket list items with CRUD operations"""

    def __init__(self, item, duedate, finished=False):
        """Constructor for a Bucketlist item"""
        self.item = item
        self.duedate = duedate
        self.finished = finished

        self.details = {
            'item': self.item,
            'duedate': self.duedate,
            'finished': self.finished
        }

    def get_details(self):
        """Method to get all the bucketlists"""
        return self.details
    