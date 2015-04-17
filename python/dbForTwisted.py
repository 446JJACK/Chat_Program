#!/usr/bin/env python3
import sqlite3
DATABASE = 'test.db'

	
con = sqlite3.connect(DATABASE)
	
with con:
	#cursor = con.cursor()
	#cursor.execute('''
	#	CREATE TABLE users(ROW_ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT,
	#					email TEXT, displayname TEXT)
	 #  				''')
	cursor = con.cursor()


#username = "james"
#password = "tyler"
#email = "james"
#displayname = "hello" 

#Insert user 1 example
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',('james', 'pord', 'hel.@yahoo.com', 'JAMER'))
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',('tyler', 'passss', 'sss.@yahoo.com', 'JAMER'))
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',('chris', 'yes', 'tyler.@yahoo.com', 'JAMER'))
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',('kevin', 'pa', 'ddd.@yahoo.com', 'JAMER'))	
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',('hello', '1234', 'james.@yahoo.com', 'JAMER'))


