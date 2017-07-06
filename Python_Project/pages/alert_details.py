import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class alert_details():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def alert_details_api(self):
        alert_details_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['alertdetails'].format(self.json_data['alertid'][0])
        dict_alert_details_response = self.objfunctlib.api_response(alert_details_url)
        return dict_alert_details_response 

    def alert_details_db(self):
        self.objfunctlib.connect_db()
        alert_details_db_json_data = json.loads(open("../config/queries.json").read())
        query = alert_details_db_json_data['queries_list'][0]['alertdetails'].format(self.json_data['alertid'][0])
        return self.objfunctlib.db_query_result(query)

    def event_details_api(self):
        event_details_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['eventdetails'].format(self.json_data['eventid'][0])
        dict_event_details_response = self.objfunctlib.api_response(event_details_url)
        return dict_event_details_response 

    def event_details_db(self):
        self.objfunctlib.connect_db()
        alert_details_db_json_data = json.loads(open("../config/queries.json").read())
        query = alert_details_db_json_data['queries_list'][0]['eventdetails'].format(self.json_data['eventid'][0])
        return self.objfunctlib.db_query_result(query)

obj = alert_details()
obj.alert_details_api()