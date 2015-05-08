#!/usr/bin/env python

import sqlite3
import json
filename = 'wompers.db'




def createUserTable(conn, cursor):
    try:
        query = '''
            CREATE TABLE IF NOT EXISTS users
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT,
                PASSWORD TEXT,
                EMAIL TEXT,
                DISPLAYNAME TEXT,
            )'''
        cursor.execute(query)
        conn.commit()
        conn.close()

    except:
        Exception("Database creation failed!")

def createMessagesTable(conn, cursor):
    try:
        query = '''
            CREATE TABLE IF NOT EXISTS messageTable
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT,
                DISPLAYNAME TEXT,
                MESSAGES TEXT
            )'''
        cursor.execute(query)
        conn.commit()
        conn.close()

    except:
        Exception("Database creation failed!")

def insertIntoUsers( username, password, email, displayname):
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
    except:
        Exception("INSERTION FAILED!")

def insertIntoMessages( username, displayname, message):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO messageTable
            (
                USERNAME,
                DISPLAYNAME,
                MESSAGES
            )
            VALUES
                (?,?,?)
            """,
            (
                username,
                displayname,
                message
                )
            )
        conn.commit()
        conn.close()
    except:
        Exception("INSERTION FAILED!")

def getFromMessages(username, displayname):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()

        query = '''
                SELECT
                    DISPLAYNAME,
                    MESSAGES
                FROM
                    messageTable
                WHERE
                    USERNAME = ?
                    and
                    DISPLAYNAME = ?
            '''

        messageList = []
        cursor.execute(query,(username, displayname,))
        for row in cursor.fetchall():
            messageList.append(row)

        conn.commit()
        conn.close()
        return messageList
    except Exception as e:
        conn.close()
        print(e)
        raise


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

        messageList = []
        cursor.execute(query,(name,))
        for row in cursor.fetchall():
            messageList.append(row)

        conn.commit()
        conn.close()
        return messageList
    except Exception as e:
        conn.close()
        print(e)
        raise


def updateMessage( message, name):
    pass
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        query = '''
            UPDATE
                users
                    (MESSAGES)
            VALUES
                (?)
            WHERE
                USERNAME = ?
            '''
        cursor.execute(query, (message, name,))

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

if createUserTable(conn, cursor):
    print('table creation successful')
if createMessagesTable(conn, cursor):
    print('messages table created!')
insertIntoMessages('john smith', 'theJohnGuy', 'All Hail Caesar')
#if insertIntoUsers('kevin', 'wombocombo', 'email@email', 'WHOA!'):
  #  print('insert successful')
#messages = getDatabaseInfo()
#print(messages)
#insertMessage('hello world!', 'kevin')
messages = getFromMessages('kevin boyette', 'kevin')
print(messages)
messages = getFromMessages('john smith', 'theJohnGuy')
print(messages)














