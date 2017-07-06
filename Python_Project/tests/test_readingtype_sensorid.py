import unittest

import sys
sys.path.append('../pages')

from readingtype_sensorid import *

class readingtype_testcase(unittest.TestCase):   
    def setUp(self):
        self.readingtype_obj = readingtype_sensorid()

    def test_readingtype_id(self):
        """Test: readingtype API request.:Name"""
        api_readingtype_id_list = []     
        for i in range(0,len(self.readingtype_obj.readingtype_sensorid_api())):
            api_readingtype_id_list.append(self.readingtype_obj.readingtype_sensorid_api()[i]['readingtypeid'])

        db_readingtype_id_list = [] 
        for i in range(0,len(self.readingtype_obj.readingtype_sensorid_db())):
            db_readingtype_id_list.append(self.readingtype_obj.readingtype_sensorid_db()[i]['ReadingTypeId'])

        self.assertEqual(sorted(api_readingtype_id_list), sorted(db_readingtype_id_list))

if __name__ == '__main__':
    unittest.main()