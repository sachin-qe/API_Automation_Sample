import unittest

import sys
sys.path.append('../pages')

from reading_type import *

class readingtype_testcase(unittest.TestCase):   
    def setUp(self):
        self.readingtype_obj = reading_type()
        
    # def tearDown(self):
    #     print "sensor1_tearDown"        

    # def test_readingtype_id(self):
    #     """Test: readingtype API request.:ID"""
    # 	self.readingtype_obj = reading_type()

    #     api_readingtype_id = self.readingtype_obj.reading_type_api()['id']

    #     db_readingtype_id = self.readingtype_obj.reading_type_db()[0]['Id']

    #     self.assertEqual(api_readingtype_id, db_readingtype_id)

    def test_readingtype_id(self):
        """Test: readingtype API request.:Name"""
        self.readingtype_obj = reading_type()

        api_readingtype_id_list = []     
        for i in range(0,len(self.readingtype_obj.reading_type_api())):
            api_readingtype_id_list.append(self.readingtype_obj.reading_type_api()[i]['readingtypeid'])

        db_readingtype_id_list = [] 
        for i in range(0,len(self.readingtype_obj.reading_type_db())):
            db_readingtype_id_list.append(self.readingtype_obj.reading_type_db()[i]['ReadingTypeId'])
        
        self.assertEqual(api_readingtype_id_list, db_readingtype_id_list)

if __name__ == '__main__':
    unittest.main()