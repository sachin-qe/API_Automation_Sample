import json
import requests
import httplib
import psycopg2
import itertools

class function_library():
    
    def __init__(self):
        self.json_data = json.loads(open("../config/config.json").read())
        self. url = self.json_data['env_list'][0]['url'] 
        self.port = self.json_data['env_list'][0]['port']


    def get_base_url(self):
        base_url =  self.url + ":" + self.port
        return base_url

    def api_response(self, url, header):
        conn =  httplib.HTTPConnection(self.url,self.port)
        response = conn.getresponse()
        data = response.read()
        readable_response = data.decode("utf-8")
        return readable_response

    def connect_db(self):
        self.conn = psycopg2.connect(database="smarter*****", user = "postgres", password = "*****", host = "demo.****.se", port = "5432")
        self.cur = self.conn.cursor()
        return self.cur

    def db_query_result(self, query):
        cursor = self.connect_db()
        self.query = query
        cursor.execute(self.query)
        rows = cursor.fetchall()
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = list()
        # print len(rows)
        for row in rows:
            data.append(dict(itertools.izip(column_names, row)))
        return data

    # def result():
        # code to generate report
