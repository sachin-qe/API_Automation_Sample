import unittest

import sys
sys.path.append('../pages')

from member import *

class member_testcase(unittest.TestCase):   
    def setUp(self):
        self.member_obj = member()
        
    # def tearDown(self):
    #     print "sensor1_tearDown"        

    def test_member_id(self):
        """Test: Member API request: MemberID"""
    	self.member_obj = member()
        # api response values
        api_member_id = self.member_obj.member_api()['memberid']

        # db response values
        db_member_id = self.member_obj.member_db()[0]['MemberId']

        self.assertEqual(api_member_id, db_member_id)

    def test_member_id(self):        
        """Test: Member API request: UserName"""
        self.member_obj = member()
        
        api_member_username = self.member_obj.member_api()['username']

        db_member_username = self.member_obj.member_db()[0]['UserName']

        self.assertEqual(api_member_username, db_member_username)

# if __name__ == '__main__':
#     unittest.main()

# member_obj = member_testcase()
# member_obj.member_test_request()