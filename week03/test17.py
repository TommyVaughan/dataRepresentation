import requests

from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')
# print (soup.prettify())

listings = soup.findAll("div", class_="PropertyListingCard" )
for listing in listings:
 entry = []

 price = listing.find(class_="PropertyListingCard__Price").text
 entry.append(price)
 address = listing.find(class_="PropertyListingCard__Address").text
 entry.append(address)
 print(entry)