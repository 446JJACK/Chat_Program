#!/usr/bin/env python3

#TO RUN GO TO COMMAND LINE AND TYPE -> sqlite3 users.db AND THEN
# select * from users;
##WILL SHOW WHATS IN THE DATABASE


import sqlite3

#creat a database files called users.db
db = sqlite3.connect('usersexample.db')


cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(ID INTEGER PRIMARY KEY, username TEXT, password TEXT,
                       email TEXT, displayname TEXT)
              ''')
#EXAMPLE DATA##
<<<<<<< HEAD:db.py
accountname = "jlivu001"
password = "12345"
email = "james@gmail.com"
displayname = "james"
=======
#WHERE DATA GETS PULLED AND THEN STORED INTO DATABASE
username = ""
password = ""
email = ""
displayname = "" 
>>>>>>> 71b51381f2fc827b3b4d271294cf53187ee3701d:python/db.py

#Insert user 1 example
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',(username, password, email, displayname))

print('First user inserted')#sanity check
db.commit()

db.close()
