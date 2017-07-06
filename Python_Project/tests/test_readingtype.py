import unittest

import sys
sys.path.append('../pages')

from reading_type import *

class readingtype_testcase(unittest.TestCase):   
    def setUp(self):
        self.readingtype_obj = reading_type()

    def test_readingtype_id(self):
        """Test: readingtype API request.:Name"""
        api_readingtype_id_list = []     
        for i in range(0,len(self.readingtype_obj.reading_type_api())):
            api_readingtype_id_list.append(self.readingtype_obj.reading_type_api()[i]['readingtypeid'])
    
        db_readingtype_id_list = [] 
        for i in range(0,len(self.readingtype_obj.reading_type_db())):
            db_readingtype_id_list.append(self.readingtype_obj.reading_type_db()[i]['ReadingTypeId'])

        self.assertEqual(sorted(api_readingtype_id_list), db_readingtype_id_list)

if __name__ == '__main__':
    unittest.main()