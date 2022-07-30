# Assignment: starting from ../FirstHomework/hw1.py, create a command line interface which allows to save 10 users' data.
# Data have to be saved into a dictionary and then into a list, which contains all of them.
# The script has to refuse the insertion if the nickname is already used by another user.
# After insertion, the script has to calculate male and female percentage and users' max, min and average age.
# Plus: I'll use a database to save data.

import mysql.connector
import os
import dotenv
from colored import fg, bg
import re
import statistics

dotenv.load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
)

mycursor = mydb.cursor()


def databaseInsertion(name, surname, gender, nickname, age):

    statement = 'INSERT INTO Users (nome, cognome, sesso, nickname, eta) VALUES (%s, %s, %s, %s, %s)'
    values = (name, surname, gender, nickname, age)
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


def getUsersAge():
    usersAge = []

    users = dataRetrieving('Users')

    for user in users:
        usersAge.append(user[5])

    return usersAge


def getUsersGender():
    usersGender = []

    users = dataRetrieving('Users')

    for user in users:
        usersGender.append(user[3])

    return usersGender


def getGenderPercentage(genderOfInterest):
    genders = getUsersGender()

    nGenderOfInterest = genders.count(genderOfInterest)

    return ((100*nGenderOfInterest)/len(genders))


def dataInput(datumName, expectedType):
    if datumName == 'gender':
        print("To indicate the gender just write M (male) or F (female)")

    datum = input("Insert your {} here: ".format(datumName))

    if expectedType == 'gender':
        datum = datum.upper()

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


for i in range(5):
    name = dataInput('name', 'string')
    surname = dataInput('surname', 'string')
    gender = dataInput('gender', 'string')
    nickname = dataInput('nickname', '')
    age = int(dataInput('age', 'int'))

    databaseInsertion(name, surname, gender, nickname, age)

    print("\n Thank you for your registration! It was a success!!! \n\n\n")

usersAge = getUsersAge()

print("Now it's time for a bit of statistics \n\n\n")
print("The minimum age of our users is: ", min(usersAge))
print("The maximum age of our users is: ", max(usersAge))
print("The average age of our users is: ", statistics.fmean(usersAge))

print("\n\n Talking about genders, the percentage of male is {}%, meanwhile the percentage of female is {}%".format(
    getGenderPercentage('M'), getGenderPercentage('F')))

mydb.close()
