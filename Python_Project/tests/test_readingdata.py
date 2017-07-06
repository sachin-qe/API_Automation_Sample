import unittest

import sys
sys.path.append('../pages')

from readingdata import *

class readingdata_testcase(unittest.TestCase):   
    def setUp(self):
        self.readingdata_obj = readingdata()    

    def test_readingdata_value(self):
        """Test: readingdata API request: value check"""
        self.assertEqual(round(self.readingdata_obj.readingdata_api()['value'],2), round(self.readingdata_obj.readingdata_db()[0]['sum'],2))

    def test_sensorid_readingdata_value(self):
        """Test: readingdata API request with sensorid: value check"""
        self.assertEqual(round(self.readingdata_obj.readingdata_sensorid_api()['value'],2), round(self.readingdata_obj.readingdata_sensorid_db()[0]['sum'],2))

if __name__ == '__main__':
    unittest.main()