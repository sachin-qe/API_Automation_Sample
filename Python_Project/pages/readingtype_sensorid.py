import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class readingtype_sensorid():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def readingtype_sensorid_api(self):
        readingtype_sensorid_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingtype_sensorid'].format(self.json_data['sensorid'][0])
        dict_readingtype_sensorid_response = self.objfunctlib.api_response(readingtype_sensorid_url)
        return dict_readingtype_sensorid_response 

    def readingtype_sensorid_db(self):
        self.objfunctlib.connect_db()
        member_theme_db_json_data = json.loads(open("../config/queries.json").read())
        query = member_theme_db_json_data['queries_list'][0]['readingtype_sensorid'].format(self.json_data['sensorid'][0])
        return sorted(self.objfunctlib.db_query_result(query))