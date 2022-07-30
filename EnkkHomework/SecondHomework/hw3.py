# Assignment: starting from ../FirstHomework/hw1.py, create a command line interface which allows to save 10 users' data.
# Data have to be saved into a dictionary and then into a list, which contains all of them.
# The script has to refuse the insertion if the nickname is already used by another user.
# Plus: I'll use a database to save data.

import mysql.connector
import os
import dotenv
from colored import fg, bg
import re

dotenv.load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
)

mycursor = mydb.cursor()


def databaseInsertion(name, surname, nickname, age):

    statement = 'INSERT INTO Users (nome, cognome, nickname, eta) VALUES (%s, %s, %s, %s)'
    values = (name, surname, nickname, age)
    mycursor.execute(statement, values)
    mydb.commit()


def dataRetrieving(table):

    statement = 'SELECT * FROM {}'.format(table)
    mycursor.execute(statement)

    return mycursor.fetchall()


def nicknameControl(nickname):
    users = dataRetrieving('Users')

    for user in users:
        if nickname == user[3]:
            return True

    return False


def dataInput(datumName, expectedType):
    datum = input("Insert your {} here:".format(datumName))

    if expectedType == 'string':
        regex = "\d"
    elif expectedType == 'int':
        regex = "[a-zA-Z]"
    else:
        regex = ""

    while (True):
        if (re.search(regex, datum) and regex != '') or (datumName == 'nickname' and nicknameControl(datum)):
            if datumName == 'nickname':
                print("\n {} nickname is already used. Please insert another nickname. \n".format(
                    datum))
            else:
                print("\n Please insert data in a correct format \n")
            datum = input("Insert your {} here:".format(datumName))
        else:
            break
    return datum


for i in range(10):
    name = dataInput('name', 'string')
    surname = dataInput('surname', 'string')
    nickname = dataInput('nickname', '')
    age = int(dataInput('age', 'int'))

    databaseInsertion(name, surname, nickname, age)

    print("\n Thank you for your registration! It was a success!!! \n\n\n")

mydb.close()
