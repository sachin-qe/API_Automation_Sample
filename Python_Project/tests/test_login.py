import unittest

import sys
sys.path.append('../pages')

from login import *

class login_testcase(unittest.TestCase):
    def setUp(self):       
        self.login_obj = login()
        self.login_obj.login_api()
        self.login_obj.login_db()

    def test_request(self):
        """Test: Login API request."""
        api_member_id = self.login_obj.login_api()[1]
        db_member_id = self.login_obj.login_db()
        self.assertEqual(api_member_id, db_member_id)

if __name__ == '__main__':
   # unittest.main()
   HTMLTestRunner.main()
