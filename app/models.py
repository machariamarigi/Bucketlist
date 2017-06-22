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

    def edit_bucketlist(self, key, title, description):
        """Edit an existing bucketlis"""
        edit_bucketlist = self.all_bucketlists[key]

        edit_bucketlist = {title: description}
        self.all_bucketlists[key]
        return self.all_bucketlists

    def delete_bucketlist(self, key):
        """Method to delete a bucketlist"""
        self.all_bucketlists.pop(key)
        return self.all_bucketlists

    def clear_bucketlist(self):
        self.all_bucketlists = []


class BucketlistItems(BucketList):
    """Class modeling bucket list items with CRUD operations"""
    all_bucketlist_items = []
    items_details = {}

    def create_bucketlist_items(self, key, title, due_date, done):
        """Method used to populate bucketlist with items"""
        self.items_details[title] = {key: due_date}
        self.all_bucketlist_items.append({
            title: done
        })

    def get_bucketlists_item_detail(self, key):
        """Return details of an item from the bucketlist"""
        return self.activity_details[key]

    def update_bucketlist_item(
            self, key, bucket_title, item_title, due_date, done):
        """Method to update items into the bucketlist"""
        self.all_bucketlist_items[key] = {
            item_title: done}

        self.activity_details[
            bucketlist_activity_name] = {bucketlist_name: due_date}

        return self.all_bucketlist_items
