# Assignment: Create a script that makes a table of todos for each user taken from https://jsonplaceholder.typicode.com/users.
# Todos have to be taken from https://jsonplaceholder.typicode.com/todos

# Example:

'''
    +------------------------------------------------------------+------+
    |                      Kurtis Weissnat                       | TODO |
    +------------------------------------------------------------+------+
    |    inventore aut nihil minima laudantium hic qui omnis     |  ✓   |
    |                 provident aut nobis culpa                  |  ✓   |
    |     facere ipsa nam eum voluptates reiciendis vero qui     |  X   |
    |     asperiores illo tempora fuga sed ut quasi adipisci     |  X   |
    |                        qui sit non                         |  X   |
    |           placeat minima consequatur rem qui ut            |  ✓   |
    |  consequatur doloribus id possimus voluptas a voluptatem   |  X   |
    | aut consectetur in blanditiis deserunt quia sed laboriosam |  ✓   |
    +------------------------------------------------------------+------+
'''

import requests
from prettytable import PrettyTable

users = requests.get("https://jsonplaceholder.typicode.com/users").json()

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

for todo in todos:
    if todo['completed'] == False:
        todo['completed'] = 'X'
    elif todo['completed'] == True:
        todo['completed'] = '✓'

usersTodos = [{'name': user['name'], "todos": [
    {'title': todo['title'], 'completed': todo['completed']} for todo in todos if todo['userId'] == user['id']]} for user in users]

for userTodos in usersTodos:

    userTable = PrettyTable()

    userTable.field_names = [userTodos['name'], 'TODO']

    userTable.add_rows([todo['title'], todo['completed']]
                       for todo in userTodos['todos'])

    print(userTable, "\n")
