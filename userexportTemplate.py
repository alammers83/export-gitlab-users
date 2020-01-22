import requests
import json
import csv

url = "https://gitlab.com/api/v4/groups/6543/members/all"

querystring = {"per_page":"100","page":"1"}

headers = {
    'Authorization': "Bearer token",
    'cache-control': "no-cache",
    'Postman-Token': "postman-token"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

f = open('/Users/alammers/Desktop/members.csv', "w")
f.write(response.text)
f.close()
