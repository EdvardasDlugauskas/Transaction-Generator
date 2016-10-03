import json
from Client import Client, User
from functions import *
from random import shuffle

MAX_TRANS = 100

ConversionID = 1001

USER_COUNT = 1000

clients = [Client("Croka-Cola"), Client("Noike"), Client("Adidoos"), Client("Maximus")]

transactions = []
# For each user
for iuser in range(USER_COUNT):
    user = User(iuser)
    # For each transaction
    for itrans in range(1, MAX_TRANS):
        client = choice(clients)
        # Got click
        if isLucky(2):
            transactions.append(create_transaction(client, user, trans_type=2, weak_date_incr=True))
            if isLucky(95):
                transactions.extend(create_logpoint_chain(client, user))

        # Got direct search
        elif isLucky(1):
            transactions.extend(create_logpoint_chain(client, user, url_from_override="www.google.com"))

        # Impression
        else:
            transactions.append(create_transaction(client, user))
            if isLucky(2):
                transactions.extend(create_logpoint_chain(client, user, url_from_override="www.google.com"))


shuffle(transactions)

with open("bigdata.txt", "w") as file:
    file.write(json.dumps(transactions, indent=4, sort_keys=True))

# Write out user info for help