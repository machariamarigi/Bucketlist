""" Module to handle various functionality that our application may need """

from .models import User, BucketList


class Storage():
    """Class will handle volatile storage of the application's data"""

    users = [{'email': None, 'password': None, 'username': None, 'id': 0}]
    bucketlists = [{'title': None, 'description': None, 'id': 0}]
    bucketlist_items = []

    def add_user(self, username, email, password):
        new_user = User(username, email, password)
        new_user_details = new_user.get_details()
        for user in self.users:
            if new_user_details['email'] == user['email']:
                break
                return False
            else:
                new_user_details['id'] = len(self.users)
                self.users.append(new_user_details)

    def add_bucketlist(self, title, description):
        new_bucketlist = BucketList(title, description)
        new_bucketlist_details = new_bucketlist.get_details()
        new_bucketlist_details['id'] = len(self.bucketlists)
        self.bucketlists.append(new_bucketlist_details)

    def get_bucketlists(self):
        return self.bucketlists

    def get_single_bucketlist(self, id):
        for bucketlist in self.bucketlists:
            if bucketlist['id'] == id:
                single_bucketlist = bucketlist
                return single_bucketlist

    def remove_bucketlist(self, id):
        del self.bucketlists[id]


store = Storage()
# store.add_bucketlist('mash', 'cool')
# print(store.get_single_bucketlist(1))
# store.add_bucketlist('masha', 'coolio')
# print(store.get_bucketlists())
# store.remove_bucketlist(1)
# print(store.get_bucketlists())
