class AtmMachine:
    def __init__(self , balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return 1
        else:
            return 0
    def deposit(self, amount):
        self.balance = self.balance + amount
    def bal(self):
        print(self.balance)
        return self.balance


print("\n\nWelcome To OOP ATM Machine\n\n")
account = AtmMachine(int(input("\nEnter an initial balance : ")))
while True:
    print("\n\n\t1. Withdraw")
    print("\t2. Deposit")
    print("\t3. Show Balance")
    print("\t0. Exit")
    choice = int(input("\nEnter Your choice : "))
    match choice:
        case 1:
            amount = int(input("\nEnter the amount to withdraw : "))
            if account.withdraw(amount):
                print("Withdrawal successful \nNew Balance:")
                account.bal()
            else:
                print("Insufficient Balance")
        case 2:
            account.deposit(amount = int(input("\nEnter the amount to withdraw : ")))
            account.bal()
        case 3:
            print("Balance : ",account.bal())
        case _:
            break
