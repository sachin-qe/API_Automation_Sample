import unittest

import sys
sys.path.append('../pages')

from sensor import *

class member_testcase(unittest.TestCase):   
    def setUp(self):
        self.sensor_obj = sensor()
        
    # def tearDown(self):
    #     print "sensor1_tearDown"        

    def test_request(self):
        """Test: Sensor API request."""
    	self.sensor_obj = sensor()

        api_sensor_id_list = []

        for i in range(0,len(self.sensor_obj.sensor_api())):
        
            api_sensor_id_list.append(self.sensor_obj.sensor_api()[i]['sensorid'])

        db_sensor_id_list = []

        for i in range(0,len(self.sensor_obj.sensor_db())):
        
            db_sensor_id_list.append(self.sensor_obj.sensor_db()[i]['SensorId'])

        # self.assertEqual(api_sensor_id_list, db_sensor_id_list)



    def test_sensorname(self):
        self.sensor_obj = sensor()

        api_sensor_name_list = []

        for i in range(0,len(self.sensor_obj.sensor_api())):

            api_sensor_name_list.append(self.sensor_obj.sensor_api()[i]['name'])

        db_sensor_name_list = []

        for i in range(0,len(self.sensor_obj.sensor_db())):

            db_sensor_name_list.append(self.sensor_obj.sensor_db()[i]['Name'])

        # self.assertEqual(api_sensor_name_list, db_sensor_name_list)


if __name__ == '__main__':
    unittest.main()