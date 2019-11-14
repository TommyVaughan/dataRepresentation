import requests
import json
from xlwt import *

dateToSearch ="2019-11-12"

# url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>"+dateToSearch
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
#print(totalPages)
listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page"+ str(pageNumber)
    #print(pageUrl)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1



w = Workbook()
ws = w.add_sheet('balance')

rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1


for reportName in listOfReports:
    #print(reportName) 
    url = "https://reports.sem-o.com/api/v1/documents/"+reportName  
    #print(url) 
    response = requests.get(url)
    aReport = response.json()
    for row in aReport["rows"]:
        #print(row["StartTime"])
        #print(row["EndTime"])
        #print(row["ImbalanceVolume"])
        #print(row["ImbalancePrice"])
        #print(row["ImbalanceCost"])
     ws.write(rowNumber,0, row["StartTime"])
     ws.write(rowNumber,1,row["EndTime"])
     ws.write(rowNumber,2,row["ImbalanceVolume"])
     ws.write(rowNumber,3,row["ImbalancePrice"])
     ws.write(rowNumber,4,row["ImbalanceCost"])       
    rowNumber += 1

w.save('balance.xls')  