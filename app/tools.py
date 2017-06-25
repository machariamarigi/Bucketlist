""" Module to handle various functionality that our application may need """

from .models import User


class Storage():
    """Class will handle volatile storage of the application's data"""

    users = [{'email': None, 'password': None, 'username': None, 'id': 0}]
    bucketlists = []
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
                return True

    def log_in(self, email, password):
        for user in self.users:
            if user['email'] == email:
                if user['password'] == password:
                    return user

store = Storage()
