import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from login import *
from function_library import *

class getbillingsensor():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def getbilling_sensor_api(self):
        getbilling_sensor_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['getbillingsensor']
        dict_getbilling_sensor_response = self.objfunctlib.api_response(getbilling_sensor_url)
        return dict_getbilling_sensor_response

    def getbilling_sensor_db(self):
        self.objfunctlib.connect_db()
        getbilling_sensordb_json_data = json.loads(open("../config/queries.json").read())
        query = getbilling_sensordb_json_data['queries_list'][0]['getbillingsensor'].format(self.json_data['userlist'][0]['username'])
        return self.objfunctlib.db_query_result(query)