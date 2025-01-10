import datetime

listOfAccounts = [
    {"name": "Alice Smith", "balance": 1000, "pin": 1234, "transactions": []},
    {"name": "Bob Johnson", "balance": 500, "pin": 5678, "transactions": []},
    {"name": "Charlie Brown", "balance": 200, "pin": 8901, "transactions": []},
]

def addAccount(account):
    listOfAccounts.append(account)
    print("Account created successfully!")

def getAccount(name, pin):
    for account in listOfAccounts:
        if account["name"] == name and account["pin"] == pin:
            return account
    return None

def updateAccount(account):
    for i, acc in enumerate(listOfAccounts):
        if acc["name"] == account["name"] and acc["pin"] == account["pin"]:
            listOfAccounts[i] = account
            break

def getCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
