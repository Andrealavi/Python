# Assignment: declare a list and print the list reverted without using any other variables.
# Plus: I'll take data from a REST api

import requests

list = requests.get("https://jsonplaceholder.typicode.com/users").json()

reversedList = []

print(list, "\n\n\n")

for i in range((len(list) - 1), -1, -1):
    reversedList.append(list[i])

print(reversedList, "\n\n\n")
