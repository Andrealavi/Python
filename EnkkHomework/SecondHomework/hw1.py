# Assignment: Create a python script which declares two lists of five elements.
# Then the user has to fill them from the command line. Eventually, the script has to concatenate the two lists.
# Plus: I would let the user chose whether to fill the lists manually or to auto fill them by randomly generating numbers.

import random


def listFill(choice):
    list = []

    for i in range(5):
        if choice == 1:
            list.append(input("Insert a number: "))
        elif choice == 2:
            list.append(random.randint(0, 1000))

    return list


print("Choose want you want to do \n\n")
print("1. Fill lists with your data")
print("2. Fill lists with random data \n")

choice = int(input())

firstList = listFill(choice)
secondList = listFill(choice)

concatenatedList = [*firstList, *secondList]

print(firstList, "\n")
print(secondList, "\n")

print("\n\n", concatenatedList)
