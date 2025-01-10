import bank

def enterBank():
    while True:
        print("Hello, what would you like to do today?")
        print("1. Open Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        userInput = input().strip()
        
        if userInput == "1":
            name = input("Enter your name: ")
            deposit = input("Enter your deposit amount: ")
            pin = int(input("Enter a PIN: "))
            bank.createAccount(name, deposit, pin)
        elif userInput == "2":
            name = input("Enter your name: ")
            pin = int(input("Enter your PIN: "))
            amount = input("Enter the amount to deposit: ")
            bank.depositMoney(name, pin, amount)
        elif userInput == "3":
            name = input("Enter your name: ")
            pin = int(input("Enter your PIN: "))
            amount = input("Enter the amount to withdraw: ")
            bank.withdrawMoney(name, pin, amount)
        elif userInput == "4":
            name = input("Enter your name: ")
            pin = int(input("Enter your PIN: "))
            bank.checkBalance(name, pin)
        elif userInput == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

enterBank()
