import json
import requests
import sqlite3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from base64 import b64encode as enc
from os import listdir


def f_new_list():
	paths = ["C:\\Users\\dARK_soul\\Desktop\\Git\\srenterprise\\images"]
	new_li = []
	for path in paths:
		files = listdir(path)
		for file in files:
			x = file[:-4]#remove .jpg 
			new_li.append(int(x))
	return new_li
new_li = f_new_list()
product_li = []
#enter prooduct id in the list to get and store the info of the product
product_set = set(new_li+product_li)
# print(len(img_set))


dbase =sqlite3.connect('sqlite_test.darkbase')
#connect to the database


def f_insert(PRODUCT_ID, IMAGE, MODEL, PRICE, PRODUCT_CODE, SPEC):
	# dbase.execute(""" INSERT INTO 'misty ro details'('PRODUCT ID', 'IMAGE', 'MODEL', 'PRICE', 
	# 	'PRODUCT CODE', 'PRICE', 'MEMBARANE', 'PUMP', 'FILTER LIFE', 'FILTERS', 'INPUT_VOLTAGE',
	# 	'MAXIMUM TDS', 'MINIMUM INLET PRESSURE / TEMP', 'PRODUCT DIMENSION', 'PURIFICATION CAPACITY',
	# 	'STORAGE CAPACITY', 'POWER CONSUMPTION', 'WEIGHT'
	# 	VALUE(?,?,?,?,?),(PRODUCT_ID, IMAGE, MODEL, PRICE, SPEC)
	# 	) """)
	dbase.execute(""" INSERT INTO 'Misty RO'('PRODUCT ID', 'IMAGE', 'MODEL', 'PRICE', 'PRODUCT CODE', 'SPEC')
		VALUES(?,?,?,?,?,?)""",(PRODUCT_ID, IMAGE, MODEL, PRICE, PRODUCT_CODE, SPEC))

	dbase.commit()


def f_encode(image):
	done = False
	while not done:
		try:
			img_enc = enc(requests.get(image).content)
			done = True
		except:
			done = False
	return img_enc


def f_scrap(product_id):
	url = f"http://opor.in/ProductDetail/Index?ProductId={product_id}"
	page = urlopen(url).read()
	soup = bs(page, 'html.parser')
	#open and read the link
	for item in soup.find_all('script'):
		if 'productDetail' in item.text:
			data=item.text.split('var productDetail =')[-1].split('};')[0] + "}"
			datajson=json.loads(data.strip())

			image_link = datajson['ImagePath'][0]
			image = f_encode(image_link)
			model = datajson['ProductName']#str
			price = datajson['Price'][0]['FinalPrice']#int
			product_code = datajson['ProductCode']#str
			spec = str(datajson['ProductSpecification'])

			f_insert(product_id, image, model, price, product_code, spec)


for product_id in product_set:
	f_scrap(product_id)
	
dbase.close()