import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from login import *
from function_library import *

class alert():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def alert_api(self):
        alert_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['alert']
        dict_alert_response = self.objfunctlib.api_response(alert_url)

        api_alert_list = []  
        for i in range(0, len(dict_alert_response['system_alerts'])):
                api_alert_list.append(dict_alert_response['system_alerts'][i]['alertid'])

        api_event_list = []
        for i in range(0, len(dict_alert_response['user_defined_alerts'])):
                api_event_list.append(dict_alert_response['user_defined_alerts'][i]['eventid'])

        filename = '../config/config.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            data['alertid'] = api_alert_list
            data['eventid'] = api_event_list

        os.remove(filename)
        with open(filename, 'w') as f:
            # data['token'] = "token:" + dict_api_response['token']
            json.dump(data, f, indent=5)

        return dict_alert_response

    def alert_db(self):
        self.objfunctlib.connect_db()
        alertdb_json_data = json.loads(open("../config/queries.json").read())
        query = alertdb_json_data['queries_list'][0]['alert'].format(self.json_data['userlist'][0]['username'])
        # print query
        return self.objfunctlib.db_query_result(query)

    def event_db(self):
        self.objfunctlib.connect_db()
        eventdb_json_data = json.loads(open("../config/queries.json").read())
        query = eventdb_json_data['queries_list'][0]['event'].format(self.json_data['userlist'][0]['username'])
        # print query
        return self.objfunctlib.db_query_result(query)


obj = alert()
obj.alert_api()
# obj.alert_db()