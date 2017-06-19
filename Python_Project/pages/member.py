import json
import requests
import httplib
import psycopg2
import function_library

class member:
    json_data = json.loads(open("../config/config.json").read())

    def member_api():
        member_url = get_base_url() + json_data['apilist'][0]['member']
        conn.request("GET", member_url, headers=token_pass())
        readable_member_response = api_response()
        print readable_member_response

    def member_db():
        connect_db()
        json_data = json.loads(open("../config/queries.json").read())
        query = json_data['queries_list'][0]['login']
        print query
        db_query_result() 