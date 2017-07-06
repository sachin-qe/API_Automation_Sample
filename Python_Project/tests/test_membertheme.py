import unittest

import sys
sys.path.append('../pages')

from member_theme import *

class membertheme_testcase(unittest.TestCase):   
    def setUp(self):
        self.membertheme_obj = member_theme()

    def test_membertheme_id(self):
        """Test: MemberTheme API request.:ID"""
        self.assertEqual(self.membertheme_obj.member_theme_api()['id'], self.membertheme_obj.member_theme_db()[0]['Id'])

    def test_membertheme_name(self):
        """Test: MemberTheme API request.:Name"""
        self.assertEqual(self.membertheme_obj.member_theme_api()['themename'], self.membertheme_obj.member_theme_db()[0]['ThemeName'])

if __name__ == '__main__':
    # unittest.main()
    HTMLTestRunner.main()