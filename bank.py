import accounts

def createAccount(name, balance, pin):
    if accounts.getAccount(name, pin) is None:
        account = {"name": name, "balance": float(balance), "pin": pin, "transactions": []}
        accounts.addAccount(account)
    else:
        print("Account already exists.")

def depositMoney(name, pin, amount):
    account = accounts.getAccount(name, pin)
    if account:
        account["balance"] += float(amount)
        timestamp = accounts.getCurrentTime()
        account["transactions"].append(f'Deposited {amount} at {timestamp}')
        accounts.updateAccount(account)
        print(f"Deposited {amount} to {name}'s account.")
    else:
        print("Invalid account or PIN.")

def withdrawMoney(name, pin, amount):
    account = accounts.getAccount(name, pin)
    if account:
        if account["balance"] >= float(amount):
            account["balance"] -= float(amount)
            timestamp = accounts.getCurrentTime()
            account["transactions"].append(f'Withdrew {amount} at {timestamp}')
            accounts.updateAccount(account)
            print(f"Withdrew {amount} from {name}'s account.")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid account or PIN.")

def checkBalance(name, pin):
    account = accounts.getAccount(name, pin)
    if account:
        print(f"{name}'s balance is {account['balance']}.")
    else:
        print("Invalid account or PIN.")

def viewTransactions(name, pin):
    account = accounts.getAccount(name, pin)
    if account:
        print(f"Transaction history for {name}:")
        for transaction in account["transactions"]:
            print(transaction)
    else:
        print("Invalid account or PIN.")
