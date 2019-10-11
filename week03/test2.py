from bs4 import BeautifulSoup

with open("file:///C:/Users/I304302/OneDrive%20-%20SAP%20SE/Desktop/colla/cars2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print (soup.prettify())

