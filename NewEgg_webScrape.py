## Author: Isachi (Izzy) Halphen
## Created: 25th Aug 2020
## Modified: 
## Purpose: to webscrape newegg.com for graphic cards
## Comments: tried running it from cmd line but the prodcts.csv wouldn't show up
##           

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# web scrapping graphic cards from newegg
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card"

# opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
page_soup.findAll("div",{"class":"item-container"})

fileName = "products.csv"
f = open(fileName, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

# this loop for run for however many containers there are which is 12
# it will grab the brand
for container in containers:

	brand = container.div.div.a.img["title"]

	# not the title, need to extract from container
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()


	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)
	
	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

# end

f.close()

