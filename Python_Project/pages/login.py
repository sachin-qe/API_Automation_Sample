import json
import requests
import urllib2, urllib

# import httplib,urllib
# import ast
# import psycopg2
import os

import sys
sys.path.append('../lib')

from function_library import *

class login():
    
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.username = self.json_data['userlist'][0]['username']
        self.password = self.json_data['userlist'][0]['password']
        self.objfunctlib = function_library()

    def login_url(self):
        login_url =  self.json_data['apilist'][0]['login']
        return login_url

    def login_api(self):
            login_data = urllib.urlencode({"username" : self.username, "password" : self.password})
            login_request = urllib2.Request(self.objfunctlib.get_base_url()+self.login_url(),login_data)
            login_response = urllib2.urlopen(login_request).read().decode("utf-8")
            dict_api_response = json.loads(login_response)  

            filename = '../config/config.json'
            with open(filename, 'r') as f:
                data = json.load(f)
                data['token'] = "token:" + dict_api_response['token']

            os.remove(filename)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=5)

            # return dict_api_response
            token_value = "token:" + dict_api_response['token']
            member_id = dict_api_response['memberid']
            return token_value, member_id


    def login_db(self):
        self.objfunctlib.connect_db()
        self.query_json_data = json.loads(open("../config/queries.json").read())
        self.query = self.query_json_data['queries_list'][0]['login'].format(self.json_data['userlist'][0]['username'])
        member_details = self.objfunctlib.db_query_result(self.query)
        member_id = member_details[0]["MemberId"]
        return member_id