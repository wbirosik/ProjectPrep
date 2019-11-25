import requests
import json


response = requests.get("http://www.mapquestapi.com/traffic/v2/incidents?key=TKCgPH0Ge23majmKQd7uFjQ9wYgz24Up&boundingBox=40.725,-73.935,40.79,-73.985&filters=construction,incidents")
print(response.status_code)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())
#print(response.json())