#!/usr/bin/env python3

#TO RUN GO TO COMMAND LINE AND TYPE -> sqlite3 users.db AND THEN
# select * from users;
##WILL SHOW WHATS IN THE DATABASE
import sqlite3

##BEGINNING OF DATABASE CLASS IN PROGRESS##

##class Database(object):
##    '''
##    This class performs database operations
##    '''
##    def __init__(self):
##        pass
##    def connect(self):
##        conn = db = sqlite3.connect('users.db')
##        return conn
##    def createTable(self):
##        db = self.connect()
##        cursor = db.cursor()
##        cursor.execute('''
##    CREATE TABLE users(ID INTEGER PRIMARY KEY, username TEXT, password TEXT,
##                       email TEXT, displayname TEXT)
##              ''')
##        cursor.commit()
##        db.close()
##        
##    def getDatabaseInfo(self):
##        db = self.connect()
##        cursor = db.cursor()
##        table = cursor.execute('select * from users')
##        db.close()
##        return table
    
#create a database files called users.db
db = sqlite3.connect('users.db')


cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(ID INTEGER PRIMARY KEY, username TEXT, password TEXT,
                       email TEXT, displayname TEXT)
              ''')
#EXAMPLE DATA##
#WHERE DATA GETS PULLED AND THEN STORED INTO DATABASE
username = ""
password = ""
email = ""
displayname = "" 

#Insert user 1 example
cursor.execute('''INSERT INTO users(username, password, email, displayname)
                  VALUES(?,?,?,?)''',(username, password, email, displayname))

print('First user inserted')#sanity check
db.commit()

db.close()
