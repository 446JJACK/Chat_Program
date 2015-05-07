#!/usr/bin/env python

import sqlite3
import json
filename = 'wompers.db'




def createTable(conn, cursor):
    try:
        query = '''
            CREATE TABLE IF NOT EXISTS users
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT,
                PASSWORD TEXT,
                EMAIL TEXT,
                DISPLAYNAME TEXT,
                MESSAGES TEXT
            )'''
        cursor.execute(query)
        conn.commit()
        conn.close()

    except:
        Exception("Database creation failed!")

def insert( username, password, email, displayname):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users
            (
                USERNAME,
                PASSWORD,
                EMAIL,
                DISPLAYNAME
            )
            VALUES
                (?,?,?,?)
            """,
            (
                username,
                password,
                email,
                displayname
                )
            )
        conn.commit()
        conn.close()
        return True
    except:
        return False
        Exception("INSERTION FAILED!")

def getMessages(name):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        messageList = []
        query = '''
                SELECT *
                     FROM users
                WHERE
                    USERNAME = ?
                    '''
        for row in cursor.execute(query,(name)):
            messageList.append(row)
        conn.commit()
        conn.close()
        return messageList

    except:
        conn.close()
        Exception('Could not get messages')


def getUser(name):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        query = '''
                SELECT
                    USERNAME,
                    MESSAGES
                FROM
                    users
                WHERE
                    USERNAME = ?
            '''
        print("hello")
        messageList = []
        cursor.execute(query,(name,))
        for row in cursor.fetchall():
            messageList.append(row)
        print('world')
        conn.commit()
        conn.close()
        return messageList
    except Exception as e:
        conn.close()
        print(e)
        raise


def insertMessage( message, name):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        query = '''
            INSERT
                INTO users
                    (messages)
            VALUES
                (?)
            WHERE
                USERNAME = ?
            '''
        cursor.execute(query, (message, name))
        conn.commit()
        conn.close()
    except:
        conn.close()
        return "Can not insert into database"




def getDatabaseInfo():
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        databaseList = []
        query = 'SELECT * FROM users'
        cursor.execute(query)
        for row in cursor.fetchall():
            databaseList.append(row)
        conn.commit()
        conn.close()
        return databaseList
    except:
        conn.close()
        Exception("Getting Database info failed!")


conn = sqlite3.connect(filename)
cursor = conn.cursor()

if createTable(conn, cursor):
    print('table creation successful')
#if insert('kevin', 'wombocombo', 'email@email', 'WHOA!'):
  #  print('insert successful')
#messages = getDatabaseInfo()
#print(messages)
messages = getUser('kevin')
print(messages)














