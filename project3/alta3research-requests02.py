#!/usr/bin/env python3
""" Project3 | Julian Rosa
    send a GET request to my Flask API """

import requests
from pprint import pprint
import json

#URL where i want to get data from
URL = "http://0.0.0.0:2225/rickmortydata"

#get api to return json and convert to a pythonic dictionary
resp= requests.get(URL).json()

pprint(resp[0]["name"])
pprint(resp[1]["name"])
pprint(resp[2]["name"])
pprint(resp[3]["name"])

print("===============================")

#create new character to post to rickmortchars object in API
new_character = {
    "name" : "Summer Smith",
    "first episode appearance" : "Pilot",
    "birthday" : "December 2",
    "age" : " 17 ",
    "species" : "human"
        }

#take python object and return it as a JSON string
new_character = json.dumps(new_character)

#url where we want to send request and json string to attach with it 
resp = requests.post(URL, json =  new_character)

#print response back from the post request
pprint(resp.json())
