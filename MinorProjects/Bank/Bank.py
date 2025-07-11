#Real World virtual atm machine minor project
import amt
pin = 6969
print("\t\tWelcome to Apna Bank\n\n")
if 'card'==input("Enter your card"):
    option = 0
    if pin == int(input("Enter your Pin")):
        choice = 'y'
        while choice == 'y':
            print("Enter your task to perform:\n")
            print("\t 1) Check Balance")
            print("\t 2) Deposit")
            print("\t 3) Withdraw")
            print("\t 0) Exit\n\n\n")
            option = int(input("Enter your choice"))
            if option >= 0 and option <=4 :
                match option:
                    case 1:
                        choice = 'y'
                        balance = amt.amt
                        print("Balance: ",balance,"\n\n\n")
                    case 2:
                        choice = 'y'
                        balance = amt.amt
                        balance += int(input("Enter value to Deposit:"))
                        amt.amt = balance
                        print("New Balance: ",balance,"\n\n\n")
                    case 3:
                        choice = 'y'
                        balance = amt.amt
                        balance -= int(input("Enter value to Withdraw:"))
                        amt.amt = balance
                        print("New Balance: ",balance,"\n\n\n")
                    case 0:
                        choice = 'n'
            else:
                print("Invalid Choice retry")
    else:
        print("Invalid Pin")
    
else:
    print("invalid card")