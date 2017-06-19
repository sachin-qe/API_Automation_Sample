import json
import requests
import httplib
import psycopg2

class function_library:
    json_data = json.loads(open("../config/config.json").read())

    def get_base_url();
        base_url = json_data['env_list'][0]['url'] + ":" + json_data['env_list'][0]['port'] 
        return base_url

    def token_pass():
        token = response_login_api()
        headers = {'authorization':"token:"+token}
        return headers

    def api_response():
        response = conn.getresponse()
        data = response.read()
        readable_response = data.decode("utf-8")
        return readable_response

    def connect_db():
        conn = psycopg2.connect(database="dbname", user = "username", password = "password", host = "hostname", port = "5432")
        cur = conn.cursor()

    def db_query_result():
        cur.execute(query)
        rows = cur.fetchall()
        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(itertools.izip(column_names, rows))
                for row in cur.fetchall()]
        print data

    def result():
        # code to generate report
