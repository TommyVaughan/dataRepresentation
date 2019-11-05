import requests
import json


#print (html)
apiKey =  '518ea3c2be84481352584ec4f1befd72bd335f91'
url = 'https://github.com/TommyVaughan/dataRepresentation'
filename = "datarep.json"

response = requests.get(url, auth=('token', apiKey))

datarepJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(datarepJSON, file, indent=4)

#print (response.status_code)
