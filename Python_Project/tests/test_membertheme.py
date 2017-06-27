import unittest

import sys
sys.path.append('../pages')

from member_theme import *

class membertheme_testcase(unittest.TestCase):   
    def setUp(self):
        self.membertheme_obj = member_theme()
        
    # def tearDown(self):
    #     print "sensor1_tearDown"        

    def test_membertheme_id(self):
        """Test: MemberTheme API request.:ID"""
    	self.membertheme_obj = member_theme()

        api_membertheme_id = self.membertheme_obj.member_theme_api()['id']

        db_membertheme_id = self.membertheme_obj.member_theme_db()[0]['Id']

        self.assertEqual(api_membertheme_id, db_membertheme_id)

    def test_membertheme_name(self):
        """Test: MemberTheme API request.:Name"""
        self.membertheme_obj = member_theme()

        api_membertheme_name = self.membertheme_obj.member_theme_api()['themename']

        db_membertheme_name = self.membertheme_obj.member_theme_db()[0]['ThemeName']

        self.assertEqual(api_membertheme_name, db_membertheme_name)

# if __name__ == '__main__':
#     unittest.main()