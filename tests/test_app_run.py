""" Module to test the running the application """
import unittest

from flask import url_for
from flask_testing import TestCase

from app import create_app


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

    def test_login_page_without_auth(self):
        """Test the loading of login page"""
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_signup_page_without_auth(self):
        """Test the loading of signup page"""
        response = self.client.get(url_for('auth.signup'))
        self.assert200(response)

    def test_login(self):
        """Test is a user logs in correctly"""
        sign_up_response = self.client.post(url_for('auth.signup', data={
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Case',
            'email': 'test@test.com',
            'password': 'pass',
            'confirm_password': 'pass'
        }))
        self.assertTrue(sign_up_response.status_code == 302)
        # response = self.client.post(url_for('auth.login'), data={
        #     "email": "tes"
        # })
