import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class apitest():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def api_response(self):
        print len(self.json_data['apilist'][0])
        for i in range(0, len(self.json_data['apilist'][0])):
            url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['i']
            print url
            # headers = {'authorization':self.json_data['token']}
            # api_request = urllib2.Request(url, headers = headers)
            # api_response =  urllib2.urlopen(api_request).read().decode("utf-8")
            # dict_response = json.loads(api_response)
            # return dict_member_theme_response 

    def db_response(self):
        self.objfunctlib.connect_db()
        db_queries = json.loads(open("../config/queries.json").read())
        print len(db_queries['queries_list'][0])
        for i in range(0, len(db_queries['queries_list'][0])):
            query = db_queries['queries_list'][i].format(self.json_data['userlist'][0]['username'])
            print query
            # return self.objfunctlib.db_query_result(query)
        

obj = apitest()
# obj.api_response()
obj.db_response()