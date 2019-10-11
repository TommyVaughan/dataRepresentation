from bs4 import BeautifulSoup
with open ("../colla/cars2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print (soup.prettify())    