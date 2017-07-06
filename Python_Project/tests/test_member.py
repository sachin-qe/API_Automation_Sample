import unittest

import sys
sys.path.append('../pages')

from member import *

class member_testcase(unittest.TestCase):   
    def setUp(self):
        self.member_obj = member()    

    def test_member_id(self):
        """Test: Member API request: MemberID"""
        self.assertEqual(self.member_obj.member_api()['memberid'], self.member_obj.member_db()[0]['MemberId'])

    def test_member_username(self):        
        """Test: Member API request: UserName"""
        self.assertEqual(self.member_obj.member_api()['username'], self.member_obj.member_db()[0]['UserName'])

if __name__ == '__main__':
    unittest.main()