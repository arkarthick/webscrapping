from urllib.request import urlopen, urlretrieve as uret
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup as bs
from base64 import b64encode as enc
import json
url = "http://opor.in/ProductDetail/Index?ProductId=212"
page = urlopen(url).read()
soup = bs(page, 'html.parser')

for item in soup.find_all('script'):
	if 'productDetail' in item.text:
		data=item.text.split('var productDetail =')[-1].split('};')[0] + "}"
		datajson=json.loads(data.strip())
		print('ProductName :'+ datajson['ProductName'])
		print('Product Code :' + datajson['ProductCode'])
		print('Price : ' , datajson['Price'][0]['FinalPrice'])
		image = datajson['ImagePath'][0]
		try:
			# filename = 212+'.jpg'
			# uret(image, filename)
			
			img_enc = enc(requests.get(image).content)
			print(len(img_enc))
		except HTTPError:
			print('no image')
       # for item in datajson['ProductSpecification']:
       #     print(item['SpecificationName'] + " : "+ item['SpecificationValue'])