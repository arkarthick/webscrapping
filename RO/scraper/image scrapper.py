from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, urlretrieve as uret
from urllib.error import HTTPError

_range = (212,215)


for product_id in range(600,1626):
	try:
		img = 'http://admin.opor.in//Image/Product/{}0.jpg'.format(product_id)
		filename = str(product_id)+'.jpg'
		uret(img, filename)
	except HTTPError:
		pass