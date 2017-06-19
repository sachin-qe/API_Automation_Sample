# import json
# import requests
# import httplib
# import yaml

# from urllib2 import urlopen

# baseurl = 'beta.smartsen.se'
# port = 8090
# conn =  httplib.HTTPConnection(baseurl, port)

# class LoginAPI():
#     def request(self, user, pwd):

#    	    with open("user.yml", 'r') as stream:
#                 try:
#                     print(yaml.load(stream))
#                 except yaml.YAMLError as exc:
#         	       print(exc)
        
#             url = "/api/api_token_auth/?username="+user+"&password="+pwd
#             # response = urlopen(url)
#             conn.request("GET", url)
#             response = conn.getresponse()
#             raw_data = response.read().decode('utf-8')
#             return json.loads(raw_data)



import json
import requests
import httplib
import psycopg2

class login:
    json_data = json.loads(open("../config/config.json").read())
    # def __init__(self):
        # self.username = username
        # self.password = password

    # def get_base_url();
    #     base_url = json_data['env_list'][0]['url'] + ":" + json_data['env_list'][0]['port'] 
    #     return base_url

    def login_data():
        username = json_data['userlist'][0]['username']
        password = json_data['userlist'][0]['password']
        login_url =  get_base_url() + json_data['apilist'][0]['login'] + "?username=" + username + "&password=" + password
        return login_url

    def login_api():
        conn =  httplib.HTTPConnection()
        conn.request("GET", login_data())
        readable_login_response = api_response()
        token_value = json.loads(readable_login_response)['token']
        return token_value

    def login_db():
        # import pdb;pdb.set_trace()
        connect_db()
        json_data = json.loads(open("../config/queries.json").read())
        query = json_data['queries_list'][0]['login']
        print query
        db_query_result() 

    # def connect_db():
    #     conn = psycopg2.connect(database="smartsense", user = "postgres", password = "p05+9r35", host = "smartsen.se", port = "5432")
    #     cur = conn.cursor()

    # def db_query_result():
    #     cur.execute(query)
    #     rows = cur.fetchall()
    #     desc = cur.description
    #     column_names = [col[0] for col in desc]
    #     data = [dict(itertools.izip(column_names, rows))
    #             for row in cur.fetchall()]
    #     print data

    # def token_pass():
    #     token = response_login_api()
    #     headers = {'authorization':"token:"+token}
    #     return headers

    # def api_response():
    #     response = conn.getresponse()
    #     data = response.read()
    #     readable_response = data.decode("utf-8")
    #     return readable_response

    # def member_api():
    #     member_url = get_base_url() + json_data['apilist'][0]['member']
    #     conn.request("GET", member_url, headers=token_pass())
    #     readable_member_response = api_response()
    #     print readable_member_response

    # def sensor_api():
    #     sensor_url = get_base_url() + json_data['apilist'][0]['sensor']
    #     conn.request("GET", sensor_url, headers=token_pass())    
    #     readable_sensor_response = api_response():
    #     print readable_sensor_response

# login_data()
# response_login_api()
# sensor()

# l = login()
# l.login_data()
# l.reponse_login_api()
# l.response_login_db()