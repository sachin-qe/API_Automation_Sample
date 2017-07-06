import json
import requests
import urllib2
import os

import sys
sys.path.append('../lib')

from function_library import *

class reading_type():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def reading_type_api(self):
        reading_type_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingtype']
        dict_reading_type_response = self.objfunctlib.api_response(reading_type_url)

        readingtype_id_list = []
        for i in range(0,len(dict_reading_type_response)):
            readingtype_id_list.append(dict_reading_type_response[i]['readingtypeid'])
        filename = '../config/config.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            data['readingtypeid'] = readingtype_id_list
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=5)

        return dict_reading_type_response 

    def reading_type_db(self):
        self.objfunctlib.connect_db()
        member_theme_db_json_data = json.loads(open("../config/queries.json").read())
        query = member_theme_db_json_data['queries_list'][0]['readingtype'].format(self.json_data['userlist'][0]['username'])
        return self.objfunctlib.db_query_result(query)
