# Assignment: create a Python script, which asks the user to insert his name, surname and age.
# Then, the script has to check wether the user's data are correct and print on screen a good-ending message.
# Plus: I'll save data on a database using mysql.connector

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


def databaseInsertion(name, surname, age):

    statement = 'INSERT INTO Users (nome, cognome, eta) VALUES (%s, %s, %s)'
    values = (name, surname, age)
    mycursor.execute(statement, values)
    mydb.commit()


def dataInput(datumName, expectedType):
    datum = input("Insert your {} here:".format(datumName))

    if expectedType == 'string':
        regex = "\d"
    elif expectedType == 'int':
        regex = "[a-zA-Z]"

    while (True):
        if re.search(regex, datum):
            print("\n Please insert data in a correct format \n")
            datum = input("Insert your {} here:".format(datumName))
        else:
            break
    return datum


print("Hello User!", "\n\n\n",  fg(2))
print("Are you ready for the complete casino experience? Please fill out with your data and be ready to play!",
      fg(117), "\n\n")

name = dataInput('name', 'string')
surname = dataInput('surname', 'string')
age = int(dataInput('age', 'int'))

databaseInsertion(name, surname, age)

print("\n Thank you for your registration! It was a success!!!", bg(2))


mydb.close()
