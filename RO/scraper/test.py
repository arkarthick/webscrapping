import sqlite3

dbase = sqlite3.connect('RO.darkbase')
c = dbase.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS 'test'(Id INTEGER, Name TEXT)''')
c.execute(''' INSERT INTO 'test'(Id, Name) VALUES (?,?)''',(1,'Ram'))
c.close()