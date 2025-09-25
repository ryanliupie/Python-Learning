import sys
# Python Banking Program 

def show_balance(balance): 
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0: 
        print("That is not a valid point")
        return 0 
    else: 
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance: 
        print("Insufficient funds")
        return 0 

    elif amount < 0: 
        print("Account must be greater than 0")
        return 0 
    else: 
        return amount

balance = 0 
is_running = True 

def main(): 

    while is_running: 
        print("Banking Program\n")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw") 
        print("4. Exit")

        choice = int(input("Choose your desired option (1, 2, 3, or 4): "))
        if choice == 1: 
            show_balance(balance)
            is_running == False
        
        elif choice == 2: 
            balance += deposit()
        
        elif choice == 3: 
            withdraw(balance)
            balance -= withdraw(balance)
        
        elif choice == 4: 
            is_running = False

        else: 
            print("You did not select a choice, please try again.")

    print("Thank you, have a nice day")

if __name__ == "__main__": 
    main()



