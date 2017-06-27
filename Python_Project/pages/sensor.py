import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class sensor():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def sensor_api(self):
        sensor_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['sensor']
        headers = {'authorization':self.json_data['token']}
        sensor_request = urllib2.Request(sensor_url, headers = headers)
        sensor_response =  urllib2.urlopen(sensor_request).read().decode("utf-8")
        dict_sensor_response = json.loads(sensor_response)
        print dict_sensor_response
        return dict_sensor_response 


    def sensor_db(self):
        self.objfunctlib.connect_db()
        sensordb_json_data = json.loads(open("../config/queries.json").read())
        query = sensordb_json_data['queries_list'][0]['sensor'].format(self.json_data['userlist'][1]['username'])
        print self.objfunctlib.db_query_result(query)
        return self.objfunctlib.db_query_result(query)

