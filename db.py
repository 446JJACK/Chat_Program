#!/usr/bin/env python3

#TO RUN GO TO COMMAND LINE AND TYPE -> sqlite3 users.db AND THEN
# select * from users;
##WILL SHOW WHATS IN THE DATABASE


import sqlite3

#creat a database files called users.db
db = sqlite3.connect('users.db')


cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(ID INTEGER PRIMARY KEY, accountname TEXT, password TEXT,
                       email TEXT, displayname TEXT)
              ''')
#EXAMPLE DATA##
accountname = "jlivu00"
password = "12345"
email = "james@gmail.com"
displayname = "james"

#Insert user 1 example
cursor.execute('''INSERT INTO users(accountname, password, email, displayname)
                  VALUES(?,?,?,?)''',(accountname, password, email, displayname))

print('First user inserted')#sanity check
db.commit()
