import requests
import json

ACCESS_TOKEN=raw_input("Access TOken: ") 
ROOM_ID=raw_input("Room ID: ")
USER_ID=raw_input("User E-mail: ")
MAX=raw_input("Max: ")

URL = "https://api.ciscospark.com/v1/messages"
HEADERS = {"content-type" : "application/json; charset=utf-8", "authorization" : "Bearer " + ACCESS_TOKEN}
PARAMS = {"roomId" : ROOM_ID, "max" : MAX}

response = requests.get(url=URL, headers=HEADERS, params=PARAMS).json()

for item in response["items"]:
    if item["personEmail"] == USER_ID:
        requests.delete(url=URL + "/" + item['id'], headers=HEADERS)
    else:
        print(item)
