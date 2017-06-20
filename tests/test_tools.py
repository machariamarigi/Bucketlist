""" Module will be used to test volatile application Auth and """

import unittest

from ..app.tools import Auth, Storage


class TestAuth(unittest.TestCase):
    """Class for testing user Authentication"""

    def setUp(self):
        """method to be called before every test"""
        self.auth = Auth()

    def test_signup(self):
        """Method to test if a user is signed up properly"""
        initial_users = len(self.auth.users)
        user = self.auth.signup("test@test.com", "test_password")
        final_users = len(self.auth.users)
        added_user = final_users - initial_users
        self.assertEquals(1, added_user, "User was not added")


if __name__ == '__main__':
    unittest.main
