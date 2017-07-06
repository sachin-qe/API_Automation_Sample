import unittest

import sys
sys.path.append('../pages')

from readingseries import *

class readingseries_testcase(unittest.TestCase):   
    def setUp(self):
        self.readingseries_obj = readingseries()    

    def test_readingseries_value(self):
        """Test: readingseries API request: value check"""
        self.assertEqual(self.readingseries_obj.readingseries_api(), self.readingseries_obj.readingseries_db())

    def test_sensorid_readingseries_value(self):
        """Test: readingseries API request with sensorid: value check"""
        self.assertEqual(self.readingseries_obj.readingseries_sensorid_api(), self.readingseries_obj.readingseries_sensorid_db())


if __name__ == '__main__':
    unittest.main()