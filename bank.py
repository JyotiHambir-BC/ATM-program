def show_balance(balance):
    print("***********************************")
    print(f"Your balance is £{balance:.2f}")
    print("***********************************")

def deposit():
    print("***********************************")
    amount = float(input("Please Enter the Amount to be Deposited: "))
    print("***********************************")

    if amount < 0:
        print("***********************************")
        print("Amount should be greater than 0 ")
        print("***********************************")
        return 0
    else:
        return amount

def withdraw_money(balance):
    print("***********************************")
    amount = float(input("Enter the amount you want to withdraw: "))
    print("***********************************")

    if amount > balance:
        print("***********************************")
        print("Insufficient Funds")
        return 0
        print("***********************************")
    elif amount < 0:
        print("***********************************")
        print("Please enter the valid amount")
        return 0
        print("***********************************")
    else:
        print("***********************************")
        print(f"You withdraw £{amount} and your current balance is £{balance - amount}")
        return amount
        print("***********************************")

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************************")
        print("     Banking Program     ")
        print("***********************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw Cash")
        print("4. Exit")
        print("***********************************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw_money(balance)
        elif choice == '4':
            is_running = False
        else:
            print("***********************************")
            print("Option not Valid")
            print("***********************************")
    print("***********************************")       
    print("Thank you!! Have a nice Day!")
    print("***********************************")

main()