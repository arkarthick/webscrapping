import json
import requests
import sqlite3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from base64 import b64encode as enc

product_id = 212
url = f"http://opor.in/ProductDetail/Index?ProductId={product_id}"
page = urlopen(url).read()
soup = bs(page, 'html.parser')
#open and read the link
for item in soup.find_all('script'):
	if 'productDetail' in item.text:
		data=item.text.split('var productDetail =')[-1].split('};')[0] + "}"
		datajson=json.loads(data.strip())
		# for item in datajson['ProductSpecification']:
		# 	li = [8508,39,53,8491,8492,8496,8498,8500,8503,8504,8510,8512]
		# 	for i in li:
		# 		if item['SpecificationId'] == i:
		print(str(datajson['ProductSpecification']))
		





# 	CREATE TABLE `misty ro details` (
# 	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	`PRODUCT ID`	TEXT UNIQUE,
# 	`IMAGE`	TEXT NOT NULL,
# 	`MODEL`	TEXT NOT NULL,
# 	`PRODUCT CODE`	TEXT,
# 	`PRICE`	INTEGER,
# 	`MEMBARANE`	TEXT,
# 	`PUMP`	TEXT,
# 	`FILTER LIFE`	TEXT,
# 	`FILTERS`	TEXT,
# 	`INPUT_VOLTAGE`	TEXT,
# 	`MAXIMUM TDS`	TEXT,
# 	`MINIMUM INLET PRESSURE / TEMP`	TEXT,
# 	`PRODUCT DIMENSION`	TEXT,
# 	`PURIFICATION CAPACITY`	TEXT,
# 	`STORAGE CAPACITY`	TEXT,
# 	`POWER CONSUMPTION`	TEXT,
# 	`WEIGHT`	TEXT
# );