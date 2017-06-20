""" Module to test the running the application """

from flask import url_for
from flask_testing import TestCase

from ..app import create_app


class TestAppRun(TestCase):
    """Test the running of the application"""
    def create_app(self):
        """Create test instance of the application"""
        config_name = 'testing'
        app = create_app(config_name)
        return app

    def test_index(self):
        """Test the loading of the homepage"""
        response = self.client.get(url_for('home.homepage'))
        self.assert200(response)

    def test_login(self):
        """Test the loading og login page"""
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)




