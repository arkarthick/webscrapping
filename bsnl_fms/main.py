from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import urllib
from bs4 import BeautifulSoup as bs
import csv
import datetime


while True:
	try:
		browser = webdriver.Firefox()
		browser.get('https://fms.bsnl.in/')
		break
	except WebDriverException:
		print('trying toopen the browser')


user_name = 'natarajan_tntvl'
password = '01012018'

username = browser.find_element_by_name('username')
username.send_keys(user_name)

pas = browser.find_element_by_name('password')
pas.send_keys(password)

submit = browser.find_element_by_id('submit-form')
submit.click()

sleep(25)
# order = browser.find_element_by_xpath('//*[@id="bookedOrders"]')
# order.click()
menu = browser.find_element_by_link_text('Work')
menu.click()
provision_order = browser.find_element_by_link_text('Pending Provision Orders')
provision_order.click()
sleep(10)
browser.find_element_by_class_name('mypagetitle').click()
length = Select(browser.find_element_by_name('bookedorders_length'))
length.select_by_value('-1')


# url = 'https://www.guru99.com/selenium-python.html'
# page = urllib.request.urlopen(url)
# soup = bs(page, 'html.parser')
# name_box = soup.find('div', attrs={'class': 'page-header'})
# name = name_box.text.strip() # strip() is used to remove starting and trailing
# with open('files\\index.csv', 'a') as csv_file:
# 	writer = csv.writer(csv_file)
# 	writer.writerow([name])

# Exception
# NoSuchWindowException