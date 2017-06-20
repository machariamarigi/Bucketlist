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
        """Method to sign up users"""

        user = {
            'id': id + 1,
            'email': email,
            'password': password
        }

        self.users.append(user)

    def login(self, email, password):
        """Method to login users"""
        for user in self.users:
            if email in dict.values(user):
                if password == user['password']:
                    return True
                else:
                    return False
        else:
            return False


class Storage(object):
    """
        This class enables users to perform CRUD operations with their profile
        and the bucket list
    """
    pass
