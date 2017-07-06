import unittest

import sys
sys.path.append('../pages')

from alert import *

class alert_testcase(unittest.TestCase):   
    def setUp(self):
        self.alert_obj = alert()

    def test_system_alert_id(self):
        """Test: alert API request.:AlertID"""
        api_system_alert_id_list = []
        data = self.alert_obj.alert_api()
        for i in range(0,len(self.alert_obj.alert_api()['system_alerts'])):
            api_system_alert_id_list.append(self.alert_obj.alert_api()['system_alerts'][i]['alertid'])

        db_system_alert_id_list = []
        for i in range(0,len(self.alert_obj.alert_db())):
            db_system_alert_id_list.append(self.alert_obj.alert_db()[i]['AlertId'])
        
        self.assertEqual(api_system_alert_id_list, db_system_alert_id_list)

    def test_system_alert_name(self):
        """Test: alert API request.:AlertName"""        
        api_system_alert_name_list = []
        for i in range(0,len(self.alert_obj.alert_api()['system_alerts'])):
            api_system_alert_name_list.append(self.alert_obj.alert_api()['system_alerts'][i]['label'])

        db_system_alert_name_list = []
        for i in range(0,len(self.alert_obj.alert_db())):
            db_system_alert_name_list.append(self.alert_obj.alert_db()[i]['Label'])

        self.assertEqual(api_system_alert_name_list, db_system_alert_name_list)

    def test_user_defined_events_id(self):
        """Test: alert API request.:EventID"""        
        api_user_defined_events_id_list = []
        for i in range(0,len(self.alert_obj.alert_api()['user_defined_alerts'])):
            api_user_defined_events_id_list.append(self.alert_obj.alert_api()['user_defined_alerts'][i]['eventid'])

        db_user_defined_events_id_list = []
        for i in range(0,len(self.alert_obj.event_db())):
            db_user_defined_events_id_list.append(self.alert_obj.event_db()[i]['EventId'])

        self.assertEqual(api_user_defined_events_id_list, db_user_defined_events_id_list)

    def test_user_defined_events_name(self):
        """Test: alert API request.:EventName"""        
        api_user_defined_events_name_list = []
        for i in range(0,len(self.alert_obj.alert_api()['user_defined_alerts'])):
            api_user_defined_events_name_list.append(self.alert_obj.alert_api()['user_defined_alerts'][i]['eventname'])

        db_user_defined_events_name_list = []
        for i in range(0,len(self.alert_obj.event_db())):
            db_user_defined_events_name_list.append(self.alert_obj.event_db()[i]['EventName'])

        self.assertEqual(api_user_defined_events_name_list, db_user_defined_events_name_list)

if __name__ == '__main__':
    unittest.main()