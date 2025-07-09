import json
import requests
import sys
if len(sys.argv) != 2:
    print("Not eghnof sfdf")
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#print(json.dumps(response.json(), indent=2)) #indent is from the json laibary it sapirtae data by one colum

o = response.json()
for re in o["results"]:
    print(re["trackName"])