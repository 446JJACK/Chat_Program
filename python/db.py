#!/usr/bin/env python

# TO RUN GO TO COMMAND LINE AND TYPE -> sqlite3 users.db AND THEN
# select * from users;
# WILL SHOW WHATS IN THE DATABASE
import sqlite3

# creat a database files called users.db
#db = sqlite3.connect('usersexample.db')
##BEGINNING OF DATABASE CLASS IN PROGRESS##


class Database(object):

    '''
    This class performs database operations
    '''

    def __init__(self, filename):
        self.filename = filename
        self.connection = None

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
        except:
            raise Exception("connection to database failed!")

    def createTable(self):
        db = self._connect()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, password TEXT,
            email TEXT,
            displayname TEXT
            )'''
        )
        self.conn.commit()
        self.conn.close()

    def getMessages(self, name):
        db = self._connect()
        try:
            messages = self.cursor.execute(
                '''
                SELECT * FROM users WHERE NAME = ?''', name
            )
            return messages
        except:
            return "Name not found"

    def insertMessage(self, message, name):
        db = self._connect()
        try:
            self.cursor.execute(
                '''
                INSERT ? INTO users WHERE NAME = ?
                ''', message, name
            )
        except:
            return "Can not insert into database"

    def getDatabaseInfo(self):
        db = self._connect()
        cursor = db.cursor()
        table = cursor.execute('select * from users')
        db.close()
        return table

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
        self.connection

    def commit(self):
        if self.connection is not None:
            self.connection.commit()


db = Database('database.db')

db.createTable()
messages = db.getMessages("kevin")
db.insertMessage("HELLO!!", "kevin")

print(messages)

# This method will Grab data for processing
# def grabData(self):
#    db = self._connect()
#    cursor = db.cursor()
#   data = cursor.execute('select * from users where id  > ?')

# create a database files called users.db
#

#db = sqlite3._connect('users.db')


# cursor = db.cursor()
# #cursor.execute('''
#     #CREATE TABLE users(ID INTEGER PRIMARY KEY, username TEXT, password TEXT,
# #                       email TEXT, displayname TEXT)
# #              ''')
# #EXAMPLE DATA##
# accountname = "tyler"
# password = "11222"
# email = "tylergmail.com"
# displayname = "tyle"

# #WHERE DATA GETS PULLED AND THEN STORED INTO DATABASE
# username = "ashley"
# password = "password"
# email = ""
# displayname = ""

# #Insert user 1 example
# cursor.execute('''INSERT INTO users(username, password, email, displayname)
# VALUES(?,?,?,?)''',(username, password, email, displayname))

# print('First user inserted')#sanity check
# db.commit()

# db.close()
