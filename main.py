import json
from Client import Client, User
from functions import *
from random import shuffle

MAX_TRANS = 100

ConversionID = 1001

clients = [Client("Croka-Cola"), Client("Noike"), Client("Adidoos"), Client("Maximus")]

transactions = []
# For each user
for iuser in range(50):
    user = User(iuser)
    # For each transaction
    for itrans in range(1, MAX_TRANS):
        client = choice(clients)
        # Got click
        if isLucky(2):
            transactions.append(create_transaction(client, user, trans_type=2))
            if isLucky(95):
                transactions.extend(create_logpoint_chain(client, user))

        # Got direct search
        elif isLucky(1):
            transactions.extend(create_logpoint_chain(client, user, url_from_override="www.google.com"))
        else:
            transactions.append(create_transaction(client, user))


shuffle(transactions)

with open("bigdata.txt", "w") as file:
    file.write(json.dumps(transactions))

