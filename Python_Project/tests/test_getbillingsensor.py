import unittest

import sys
sys.path.append('../pages')

from getbillingsensor import *

class getbillingsensor_testcase(unittest.TestCase):   
    def setUp(self):
        self.getbillingsensor_obj = getbillingsensor()

    def test_getbillingsensor_id(self):
        """Test: GetBillingSensor API request: BillingSensorId"""

        api_billingsensor_id_list = []
        # api response values
        for i in range(0,len(self.getbillingsensor_obj.getbilling_sensor_api())):        
            api_billingsensor_id_list.append(self.getbillingsensor_obj.getbilling_sensor_api()[i]['SensorId'])

        db_getbillingsensor_id_list = []
        # db response values
        for i in range(0,len(self.getbillingsensor_obj.getbilling_sensor_db())):        
            db_getbillingsensor_id_list.append(self.getbillingsensor_obj.getbilling_sensor_db()[i]['SensorId'])
        
        self.assertEqual(api_billingsensor_id_list, db_getbillingsensor_id_list)

if __name__ == '__main__':
    unittest.main()