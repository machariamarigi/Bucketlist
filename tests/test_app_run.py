""" Module to test the running the application """

from unittest import TestCase

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
        app = self.create_app()
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
