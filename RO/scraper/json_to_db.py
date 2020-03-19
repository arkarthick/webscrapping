import json
import sqlite3


jsonfile = json.load(open('filter_data.json'))

dbase = sqlite3.connect('RO.darkbase')

c = dbase.cursor()

def create_table():
	c.execute(''' CREATE TABLE IF NOT EXISTS 'Domestic Filters'(
		Id INTEGER PRIMARY KEY UNIQUE,
		LPH INTEGER,
		ProductId INTEGER,
		Name TEXT,
		Price INTEGER,
		Image TEXT,
		Spec TEXT
		);''')

	c.execute(''' CREATE TABLE IF NOT EXISTS 'Industrial Filters'(
		Id INTEGER PRIMARY KEY UNIQUE,
		LPH INTEGER,
		ProductId INTEGER ,
		Name TEXT,
		Price INTEGER,
		Image TEXT,
		Spec TEXT
		);''')


def domestic_insert(data):
	c.execute("INSERT INTO 'Domestic Filters'(Id, LPH, ProductId, Name, Price, Image, Spec) VALUES(?, ?, ?, ?, ?, ?, ?)", data)
	dbase.commit()
def ind_insert(data):
	c.execute('''INSERT INTO 'Industrial Filters'(Id, LPH, ProductId, Name, Price, Image, Spec) VALUES(?, ?, ?, ?, ?, ?, ?)''', data)
	dbase.commit()


def load_data(variant_type):
	count = 0
	x = []
	for variant_lph in jsonfile[variant_type]:
		for lph in jsonfile[variant_type][variant_lph]:
			for name in jsonfile[variant_type][variant_lph][lph]:
				
				if lph in x:
					pass
				else:
					x.append(lph)
					count += 1
					name = jsonfile[variant_type][variant_lph][lph]['ProductName']
					code = jsonfile[variant_type][variant_lph][lph]['ProductCode']
					price = int(jsonfile[variant_type][variant_lph][lph]['Price'])
					img = jsonfile[variant_type][variant_lph][lph]['Image']
					spec = str(jsonfile[variant_type][variant_lph][lph]['Specification'])
					product_id = int(lph)

					data = (count, int(variant_lph[:-3]), product_id, name, price, img, spec)
					# print(data)
					# print(count)
					
					if variant_type == 'Domestic Filters':
						print(x)
						domestic_insert(data)
					elif variant_type == 'Industrial Filters':

						print(x)
						ind_insert(data)
				


create_table()
for variant in jsonfile:
	# print(variant)
	load_data(variant)

	print('')
# domestic_insert("'Domestic Filters'")
c.close()