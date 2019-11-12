import requests
import json

# url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json()

listOfReports = []
#output to console
#print(data)
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])

for reportName in listOfReports:
    #print(reportName) 
    url = "https://reports.sem-o.com/api/v1/documents/"+reportName  
    print(url) 

#save this to a file
filename = 'allreports.json'

#writing json data
f = open(filename, 'w')
json.dump(data, f, indent=4)

