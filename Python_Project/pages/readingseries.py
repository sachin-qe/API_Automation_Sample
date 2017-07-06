import json
import requests
import urllib, urllib2

import sys
sys.path.append('../lib')

# from login import *
from function_library import *

class readingseries():
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self.objfunctlib = function_library()

    def readingseries_api(self):
        readingseries_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingseries'].format(self.json_data['readingtypeid'][1])
        dict_readingseries_response = self.objfunctlib.api_response(readingseries_url)
        timestamp_list = []
        readingvalue_list = []
        for i in range(0, len(dict_readingseries_response[1]['timeseries'])):
            timestamp_list.append(dict_readingseries_response[1]['timeseries'][i]['timeStamp'])
            readingvalue_list.append(round(dict_readingseries_response[1]['timeseries'][i]['value'], 2))
        readingseries_dict = dict(zip(timestamp_list, readingvalue_list))
        return sorted(readingseries_dict.iteritems())
        
    def readingseries_db(self):
        self.objfunctlib.connect_db()
        readingseries_db_json_data = json.loads(open("../config/queries.json").read())
        query = readingseries_db_json_data['queries_list'][0]['readingseries'].format(self.json_data['readingtypeid'][1],self.json_data['userlist'][0]['username'])
        data = self.objfunctlib.db_query_result(query)
        timestamp_list = [] 
        readingvalue_list = []
        for i in range(0,len(data)):
            timestamp_list.append((int)(data[i]['TimeStamp'].strftime('%s')))
            readingvalue_list.append(round(data[i]['sum'],2))
        readingseries_dict = dict(zip(timestamp_list, readingvalue_list))
        return sorted(readingseries_dict.iteritems())

    def readingseries_sensorid_api(self):
        readingseries_url = self.objfunctlib.get_base_url() + self.json_data['apilist'][0]['readingseries_sensorid'].format(self.json_data['readingtypeid'][1], self.json_data['sensorid'][0])
        print readingseries_url
        dict_readingseries_response = self.objfunctlib.api_response(readingseries_url)
        timestamp_list = []
        readingvalue_list = []
        for i in range(0, len(dict_readingseries_response[1]['timeseries'])):
            timestamp_list.append(dict_readingseries_response[1]['timeseries'][i]['timeStamp'])
            readingvalue_list.append(round(dict_readingseries_response[1]['timeseries'][i]['value'], 2))
        readingseries_dict = dict(zip(timestamp_list, readingvalue_list))
        return sorted(readingseries_dict.iteritems())
        
    def readingseries_sensorid_db(self):
        self.objfunctlib.connect_db()
        readingseries_db_json_data = json.loads(open("../config/queries.json").read())
        query = readingseries_db_json_data['queries_list'][0]['readingseries_sensorid'].format(self.json_data['sensorid'][0], self.json_data['readingtypeid'][1])
        data = self.objfunctlib.db_query_result(query)
        timestamp_list = [] 
        readingvalue_list = []
        for i in range(0,len(data)):
            timestamp_list.append((int)(data[i]['TimeStamp'].strftime('%s')))
            readingvalue_list.append(round(data[i]['sum'],2))
        readingseries_dict = dict(zip(timestamp_list, readingvalue_list))
        return sorted(readingseries_dict.iteritems())