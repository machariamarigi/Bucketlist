"""Module for the application's USER, BUCKETLIST and BUCKETLISTITEMS"""


class User(object):
    """Class modeling a real world user"""

    def __init__(self, username, email, password):
        """Constructor for user object"""
        self.username = username
        self.email = email
        self.password = password

        self.details = {
            'username': username,
            'email': email,
            'password': password
        }

    def get_details(self):
        return self.details


class Bucketlist(object):
    """Class modeling a bucket list"""


class BucketListItem(object):
    """Class modeling items in a bucketlist item"""
