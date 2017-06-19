import json
import requests
import httplib
import psycopg2
import function_library

class login:
    json_data = json.loads(open("../config/config.json").read())
    # def __init__(self):
        # self.username = username
        # self.password = password

    def login_data():
        username = json_data['userlist'][0]['username']
        password = json_data['userlist'][0]['password']
        login_url =  get_base_url() + json_data['apilist'][0]['login'] + "?username=" + username + "&password=" + password
        return login_url

    def login_api():
        conn =  httplib.HTTPConnection()
        conn.request("GET", login_data())
        readable_login_response = api_response(login_url)
        token_value = json.loads(readable_login_response)['token']
        return token_value

    def login_db():
        # import pdb;pdb.set_trace()
        connect_db()
        json_data = json.loads(open("../config/queries.json").read())
        query = json_data['queries_list'][0]['login'].format(json_data['userlist'][0]['username'])
        print query
        db_query_result() 

# login_data()
# response_login_api()
# sensor()

# l = login()
# l.login_data()
# l.reponse_login_api()
# l.response_login_db()