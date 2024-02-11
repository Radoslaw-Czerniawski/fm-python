import requests

API_URL = "http://shibe.online/api/shibes?count=1"
PARAMS = {"count": 10}

response = requests.get(API_URL, params=PARAMS)

status_code = response.status_code
print("status code: ", status_code)

response_json = response.json()
print(response_json)
