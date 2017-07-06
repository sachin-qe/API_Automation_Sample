import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from function_library import *

class member_theme():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def member_theme_api(self):
        member_theme_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['membertheme']
        dict_member_theme_response = self.objfunctlib.api_response(member_theme_url)
        return dict_member_theme_response 

    def member_theme_db(self):
        self.objfunctlib.connect_db()
        member_theme_db_json_data = json.loads(open("../config/queries.json").read())
        query = member_theme_db_json_data['queries_list'][0]['membertheme'].format(self.json_data['userlist'][0]['username'])
        return self.objfunctlib.db_query_result(query)
        