import json
import requests
import sqlite3
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bs
from base64 import b64encode as enc
from os import listdir
from timeit import timeit

from productId_data import filters


# def f_product_list():
# 	product_id_li = []
# 	#enter prooduct id in the list to get and store the info of the product
# 	paths = ["C:\\Users\\dARK_soul\\Desktop\\Git\\srenterprise\\images"]
# 	new_li = []
# 	for path in paths:
# 		files = listdir(path)
# 		for file in files:
# 			x = file[:-4]#remove .jpg 
# 			new_li.append(int(x))
# 	product_set = set(new_li+product_id_li)
# 	# print(len(img_set))
# 	print('list generated')
# 	return product_set


# def f_insert(PRODUCT_ID, IMAGE, MODEL, PRICE, PRODUCT_CODE, SPEC):
# 	# dbase.execute(""" INSERT INTO 'misty ro details'('PRODUCT ID', 'IMAGE', 'MODEL', 'PRICE', 
# 	# 	'PRODUCT CODE', 'PRICE', 'MEMBARANE', 'PUMP', 'FILTER LIFE', 'FILTERS', 'INPUT_VOLTAGE',
# 	# 	'MAXIMUM TDS', 'MINIMUM INLET PRESSURE / TEMP', 'PRODUCT DIMENSION', 'PURIFICATION CAPACITY',
# 	# 	'STORAGE CAPACITY', 'POWER CONSUMPTION', 'WEIGHT'
# 	# 	VALUE(?,?,?,?,?),(PRODUCT_ID, IMAGE, MODEL, PRICE, SPEC)
# 	# 	) """)
# 	dbase.execute(""" INSERT INTO 'Misty RO'('PRODUCT ID', 'IMAGE', 'MODEL', 'PRICE', 'PRODUCT CODE', 'SPEC')
# 		VALUES(?,?,?,?,?,?)""",(PRODUCT_ID, IMAGE, MODEL, PRICE, PRODUCT_CODE, SPEC))

# 	dbase.commit()


# def f_encode(image):
# 	done = False
# 	while not done:
# 		try:
# 			img_enc = enc(requests.get(image).content)
# 			done = True
# 		except:
# 			done = False
# 	return img_enc

def f_gen_text_file(data):
	with open('Filter_data.json', 'w+') as file:
		json.dump(data, file, indent=4)
	print('file generated')


def f_scrap(product_id):
	url = f"http://opor.in/ProductDetail/Index?ProductId={product_id}"
	opened = False
	while not opened:
		try:
			page = urlopen(url).read()
			opened = True
		except:
			break
	if opened == True:
		soup = bs(page, 'html.parser')
		#open and read the link
		for item in soup.find_all('script'):
			if 'productDetail' in item.text:
				data=item.text.split('var productDetail =')[-1].split('};')[0] + "}"
				datajson=json.loads(data.strip())

				''' 
				use for databasde

				# image_link = datajson['ImagePath'][0]
				# image = f_encode(image_link)
				# model = datajson['ProductName']#str
				# price = datajson['Price'][0]['FinalPrice']#int
				# product_code = datajson['ProductCode']#str
				# spec = str(datajson['ProductSpecification'])
				# f_insert(product_id, image, model, price, product_code, spec)
				'''

				product_id = {}
				
				product_id["ProductName"] = datajson['ProductName']#str
				product_id["ProductCode"] = datajson['ProductCode'] 
				product_id["Price"] = datajson['Price'][0]['FinalPrice']#int 
				product_id["Image"] = image_link = datajson['ImagePath'][0]
				product_id["Specification"] = datajson['ProductSpecification']
				print('sucess')
				return product_id
				
	else:
		print('problem occured')


def main(filters):
	# dbase =sqlite3.connect('sqlite_test.darkbase')#connect to the database
	data = {}
	for _filter in filters:
		catogery = _filter
		data[catogery] = {}
		# scrap_data = {}
		for x,y in filters[_filter].items():
			variant = x
			product_set = y
			data[catogery][variant] = {}

			
		
	# catogory = '12LPH'
	# product_set = [216, 217, 218]
			
			print(product_set)
			for product_id in product_set:
				print(product_id)
				a = f_scrap(product_id)

				if a != None:
					data[catogery][variant][product_id] = a
				print(len(data))

	f_gen_text_file(data)
		
	# dbase.close()#close the data base


if __name__ == '__main__':
	start = timeit()
	main(filters)
	end = timeit()
	print(end-start)
