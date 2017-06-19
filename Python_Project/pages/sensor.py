import json
import requests
import httplib
import psycopg2
import function_library

class sensor:
    json_data = json.loads(open("../config/config.json").read())
    
	def sensor_api():
		sensor_url = get_base_url() + json_data['apilist'][0]['sensor']
    	conn.request("GET", sensor_url, headers=token_pass())    
    	readable_sensor_response = api_response():
    	print readable_sensor_response

    def sensor_db():
        connect_db()
        json_data = json.loads(open("../config/queries.json").read())
        query = json_data['queries_list'][0]['sensor']
        print query
        db_query_result()     	