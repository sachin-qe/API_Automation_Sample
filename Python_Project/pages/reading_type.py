import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class reading_type():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def reading_type_api(self):
        reading_type_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingtype']
        headers = {'authorization':self.json_data['token']}
        reading_type_request = urllib2.Request(reading_type_url, headers = headers)
        reading_type_response =  urllib2.urlopen(reading_type_request).read().decode("utf-8")
        dict_reading_type_response = json.loads(reading_type_response)
        # print dict_reading_type_response 
        return dict_reading_type_response 

    def reading_type_db(self):
        self.objfunctlib.connect_db()
        member_theme_db_json_data = json.loads(open("../config/queries.json").read())
        query = member_theme_db_json_data['queries_list'][0]['readingtype'].format(self.json_data['userlist'][0]['username'])
        # print query
        # print self.objfunctlib.db_query_result(query)
        # api_readingtype_id_list = []
        # for i in range(0,len(len(self.objfunctlib.db_query_result(query)['ReadingTypeId']))):
        #     api_sensor_id_list.append(self.objfunctlib.db_query_result(query)['ReadingTypeId'])
        #     print len(api_sensor_id_list)
        return self.objfunctlib.db_query_result(query)
        
# obj = reading_type()
# obj.reading_type_api()