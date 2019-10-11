from bs4 import BeautifulSoup
with open ("../colla/cars2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# print (soup.tr)    
rows = soup.findAll("tr")
for row in rows:
    print("------")
    # print(row)
    cols = row.findAll("td")
    for col in cols:
        print(col.text)