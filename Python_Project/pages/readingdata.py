import json
import requests
import urllib, urllib2

import sys
sys.path.append('../lib')

from function_library import *

class readingdata():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def readingdata_api(self):       
        readingdata_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingdata']
        dict_readingdata_response = self.objfunctlib.api_response(readingdata_url)  
        return dict_readingdata_response

    def readingdata_db(self):
        self.objfunctlib.connect_db()
        readingdata_db_json_data = json.loads(open("../config/queries.json").read())
        query = readingdata_db_json_data['queries_list'][0]['readingdata'].format(self.json_data['userlist'][0]['username'])
        return self.objfunctlib.db_query_result(query)

    def readingdata_sensorid_api(self):       
        readingdata_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingdata_sensorid'].format(self.json_data['sensorid'][1])
        dict_readingdata_response = self.objfunctlib.api_response(readingdata_url)
        return dict_readingdata_response
        
    def readingdata_sensorid_db(self):
        self.objfunctlib.connect_db()
        readingdata_db_json_data = json.loads(open("../config/queries.json").read())
        query = readingdata_db_json_data['queries_list'][0]['readingdata_sensorid'].format(format(self.json_data['sensorid'][1]))
        return self.objfunctlib.db_query_result(query)

# obj = readingdata()
# obj.readingdata_api()
# obj.readingdata_db()
# obj.readingdata_sensorid_db()
# obj.readingdata_sensorid_api()