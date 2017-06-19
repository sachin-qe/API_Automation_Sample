import os.path
import unittest
from urlparse import urlparse

from pages import login

from mock import patch

class LoginTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        login_obj = login()
        login_obj.login_data()
        loginlogin_obj.login_api()
        login_obj.login_db()
        
    def tearDown(self):
        self.patcher.stop()

    def test_request(self):
        """Test a simple request."""
        self.assertEqual(login_obj.login_api(), login_obj.login_db())
 
