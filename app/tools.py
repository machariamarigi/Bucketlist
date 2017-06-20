"""Module for volatile storage functionality"""

id = 0


class Auth(object):
    """
        This class should enable users to be able to sign up and sign into the
        app
    """
    def __init__(self):
        """ Auth Constructor"""
        self.users = []

    def signup(self, email, password):
        user = {
            'id': id + 1,
            'email': email,
            'password': password
        }

        self.users.append(user)


class Storage(object):
    """
        This class enables users to perform CRUD operations with their profile
        and the bucket list
    """
    pass
