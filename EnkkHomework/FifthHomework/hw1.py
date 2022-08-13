# Assignment: Create a script which prints all users' email from ./data/01_data.json

import json

with open("./data/01_data.json", 'r') as f:

    users = json.load(f)

[print([user['email'] for user in users][i]) for i in range(len(users))]
