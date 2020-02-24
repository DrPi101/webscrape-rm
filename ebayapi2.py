import json
from ebaysdk.finding import Connection as finding # install with pip
from bs4 import BeautifulSoup # install with pip
from ebayapi import ebayapi # My API key


def get_kw():
	f = open ("ebay_search.txt", "r")
	lines = f.readlines()
	Keywords = lines
	return Keywords

def get_items(Keywords):
	api = finding(appid = ebayapi, siteid='EBAY-GB', config_file=None) # change country with 'siteid='
	api_request = { 'keywords': Keywords, 'outputSelector' : 'SellerInfo'}
	response = api.execute('findItemsByKeywords', api_request)
	soup = BeautifulSoup(response.content, 'lxml')
	items = soup.find_all('item')
	return items

def res_print(items):
    for item in items:
        cat = item.categoryname.string.lower()
        title = item.title.string.lower().strip()
        price = int(round(float(item.currentprice.string)))
        url = item.viewitemurl.string.lower()
        seller = item.sellerusername.text.lower()
        listingtype = item.listingtype.string.lower()

        print(cat)
        print("\n")
        print(title)
        print()
        print(price)
        print()
        print(url)
        print()
        print(seller)
        print("*" * 20)


ebay_results = 'ebay_results.txt' # Next : Write it to JSON

def res_text(items):
    with open(ebay_results, "a") as f:
        for item in items:
            cat = item.categoryname.string.lower()
            title = item.title.string.lower().strip()
            price = int(round(float(item.currentprice.string)))
            url = item.viewitemurl.string.lower()
            seller = item.sellerusername.text.lower()
            title = item.title.string.lower().strip()
            f.write(title)
            f.write(" £")
            f.write(str(price))
            f.write(url)
            f.write(" ")
            f.write(seller)
            f.write(" ")
            f.write("*" * 20)
            f.write("\n")


def res_json():
    pass

# main #


Keywords = get_kw()

for i in range(len(Keywords)):
	x = get_items(Keywords[i])
	res_print(x)
	res_text(x)
