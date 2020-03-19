#product id scrapper

import json
import requests
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bs


def f_gen_text_file(data, filename):
	with open(f'{filename}.json', 'w+') as file:
		json.dump(data, file, indent=4)
	print('file generated')


def f_scrap(category_id):
	url = f"http://opor.in/ProductSearch/Index?CategoryId={category_id}"
	opened = False
	while not opened:
		try:
			page = urlopen(url).read()
			opened = True
		except Exception as e:
			print(e)
			break
	if opened == True:
		soup = bs(page, 'html.parser')
		#open and read the link
		for item in soup.find_all('script'):
			if 'productList' in item.text:
				data=item.text.split('var productList =')[-1].split('};')[0] + "}"
				datajson=json.loads(data.strip())
				product_id_li = []
				# print(len(datajson["ProductList"]))
				product_list = datajson['ProductList']
				for product in product_list:
					product_id_li.append(product['ProductId'])

				print(product_id_li)

				
	else:
		print('problem occured')


while True:
	category_id = input('>>>')
	if category_id == 'exit()':
		break
	else:
		f_scrap(category_id)