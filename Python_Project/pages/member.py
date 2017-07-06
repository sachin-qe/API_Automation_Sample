import json
import requests
import urllib2

import sys
sys.path.append('../lib')

from login import *
from function_library import *

class member():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def member_api(self):
        member_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['member']
        dict_member_response = self.objfunctlib.api_response(member_url)
        return dict_member_response[0]

    def member_db(self):
        self.objfunctlib.connect_db()
        memberdb_json_data = json.loads(open("../config/queries.json").read())
        query = memberdb_json_data['queries_list'][0]['member'].format(self.json_data['userlist'][0]['username'])
        return self.objfunctlib.db_query_result(query)
        