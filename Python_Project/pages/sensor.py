import json
import requests
import urllib2
import os
import sys
sys.path.append('../lib')

from function_library import *

class sensor():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def sensor_api(self):
        sensor_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['sensor']
        dict_sensor_response = self.objfunctlib.api_response(sensor_url)
      
        # creating list of sensors and saving it to config file which can be used in other apis
        sensor_id_list = []
        for i in range(0,len(dict_sensor_response)):
            sensor_id_list.append(dict_sensor_response[i]['sensorid'])
        filename = '../config/config.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            data['sensorid'] = sensor_id_list
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=5)

        # print dict_sensor_response
        return dict_sensor_response 


    def sensor_db(self):
        self.objfunctlib.connect_db()
        sensordb_json_data = json.loads(open("../config/queries.json").read())
        query = sensordb_json_data['queries_list'][0]['sensor'].format(self.json_data['userlist'][1]['username'])
        # print self.objfunctlib.db_query_result(query)
        return self.objfunctlib.db_query_result(query)


# obj = sensor()
# obj.sensor_api()
# obj.sensor_db()