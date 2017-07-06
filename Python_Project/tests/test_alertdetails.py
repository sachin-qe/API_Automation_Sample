import unittest

import sys
sys.path.append('../pages')

from alert_details import *

class alert_details_testcase(unittest.TestCase):   
    def setUp(self):
        self.alert_details_obj = alert_details()   

    def test_alert_details_id(self):
        """Test: alert_details API request: AlertId"""
        self.assertEqual(self.alert_details_obj.alert_details_api()['alertid'], self.alert_details_obj.alert_details_db()[0]['AlertId'])

    def test_alert_details_sensorid(self):        
        """Test: alert_details API request: SensorId"""
        self.assertEqual(self.alert_details_obj.alert_details_api()['sensorid'], self.alert_details_obj.alert_details_db()[0]['SensorId'])

    def test_alert_details_alertcategory(self):        
        """Test: alert_details API request: alertcategory"""
        self.assertEqual(self.alert_details_obj.alert_details_api()['alertcategory'], self.alert_details_obj.alert_details_db()[0]['AlertCategory'])

    def test_alert_details_readingtypeid(self):        
        """Test: alert_details API request: readingtypeid"""
        self.assertEqual(self.alert_details_obj.alert_details_api()['readingtypeid'], self.alert_details_obj.alert_details_db()[0]['ReadingTypeId'])

    def test_alert_details_thresholdvalue(self):        
        """Test: alert_details API request: thresholdvalue"""
        self.assertEqual(self.alert_details_obj.alert_details_api()['thresholdvalue'], self.alert_details_obj.alert_details_db()[0]['ThresholdValue'])        

    def test_event_details_id(self):
        """Test: alert_details API request: EventId"""
        self.assertEqual(self.alert_details_obj.event_details_api()['eventid'], self.alert_details_obj.event_details_db()[0]['EventId'])

    def test_event_details_sensorid(self):        
        """Test: alert_details API request: SensorId"""
        self.assertEqual(self.alert_details_obj.event_details_api()['sensorid'], self.alert_details_obj.event_details_db()[0]['SensorId'])

    def test_event_details_eventname(self):        
        """Test: alert_details API request: alertcategory"""
        self.assertEqual(self.alert_details_obj.event_details_api()['eventname'], self.alert_details_obj.event_details_db()[0]['EventName'])


if __name__ == '__main__':
    unittest.main()
