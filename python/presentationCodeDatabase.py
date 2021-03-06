#! /usr/bin/env python3

import sqlite3

DATABASE = 'test.db'  # GLOBAL


def main():
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
    except:
        raise Exception("Connection to database failed!")

    cursor.execute('''CREATE TABLE IF NOT EXISTS groupMembers
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
               firstName VARCHAR(30),
               lastName VARCHAR(30),
               email VARCHAR(50),
               phoneNumber INT)''')

    firstName = input("Please Enter the first name of your group member: ")
    lastName = input("Please Enter the last name of your group member: ")
    email = input("Please enter the email of your group member: ")
    phoneNumber = input("Please enter the phone number of your group member: ")

    cursor.execute('''INSERT INTO groupMembers(firstName,lastName, email, phoneNumber)
                        VALUES(?,?,?,?)''', (firstName, lastName, email, phoneNumber,))
    print("Group member added! ")

    # NEVER DO THIS; VULNERABLE FOR SQL INJECTION
    #name = 'James'
    #cursor.execute("SELECT * FROM groupMembers WHERE name=? '%s'" % name)

    db.commit()  # Commits the change to database
    db.close()
main()
