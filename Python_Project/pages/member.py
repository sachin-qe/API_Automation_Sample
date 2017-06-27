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
        headers = {'authorization':self.json_data['token']}
        member_request = urllib2.Request(member_url, headers = headers)
        member_response =  urllib2.urlopen(member_request).read().decode("utf-8")
        dict_member_response = json.loads(member_response)[0]
        print dict_member_response
        return dict_member_response

    def member_db(self):
        self.objfunctlib.connect_db()
        memberdb_json_data = json.loads(open("../config/queries.json").read())
        query = memberdb_json_data['queries_list'][0]['member'].format(self.json_data['userlist'][0]['username'])
        print query
        print self.objfunctlib.db_query_result(query)
        return self.objfunctlib.db_query_result(query)