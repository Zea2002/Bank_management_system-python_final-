from bank_management import Bank
from admin import Admin
from user import User


def user_menu(bank_instance):
    U = User(bank_instance)
    while True:
        print("Option\n")
        print("1. Create account")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Check transaction history")
        print("5. Fund transfer")
        print("6. Withdraw")
        print("7. Take loan")
        print("8. Exit")
        choice = int(input("Enter the option: "))
        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account_type: ")
            U.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.deposit(account_number, amount)
        elif choice == 3:
            account_number = int(input("Enter account Number: "))
            U.check_balance(account_number)
        elif choice == 4:
            account_number = int(input("Enter account Number: "))
            U.see_transaction(account_number)
        elif choice == 5:
            account_number = int(input("Enter account Number: "))
            receiver_acc = int(input("Enter receiver account number: "))
            amount = int(input("Enter amount: "))
            U.fund_transfer(account_number, receiver_acc, amount)
        elif choice == 6:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.withdraw(account_number, amount)
        elif choice == 7:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.take_loan(account_number, amount)
        elif choice == 8:
            break
        else:
            print("Invalid input, try again")


def admin_menu(bank_instance):
    name = input("Enter admin name: ")
    email = input("Enter admin email: ")
    A = Admin(name, email, bank_instance) 
    while True:
        print("Option\n")
        print("1. Create account")
        print("2. Delete account")
        print("3. All user accounts")
        print("4. Total available balance")
        print("5. Total loan amount")
        print("6. Change Loan feature")
        print("7. Change Bankrupt status")
        print("8. Exit")
        choice = int(input("Enter the option: "))
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account_type: ")
            A.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account Number: "))
            A.delete_account(account_number)
        elif choice == 3:
            A.see_all_user_accounts()
        elif choice == 4:
            A.total_available_balance()
        elif choice == 5:
            A.check_total_loan_amount()
        elif choice == 6:
            status = input("Enter 'on' to enable or 'off' to disable loan feature: ").lower()
            if status == 'on':
                A.toggle_loan_feature(True)
            elif status == 'off':
                A.toggle_loan_feature(False)
            else:
                print("Invalid input")
        elif choice == 7:
            status = input("Enter 'on' to enable or 'off' to disable bankrupt status: ").lower()
            if status == 'on':
                A.change_bankrupt_status(True)
            elif status == 'off':
                A.change_bankrupt_status(False)
            else:
                print("Invalid input")
        elif choice == 8:
            break
        else:
            print("Invalid input, try again")

bank_instance = Bank()
while True:
    print("Option\n")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter option: "))
    if choice == 1:
        user_menu(bank_instance)
    elif choice == 2:
        admin_menu(bank_instance)
    elif choice == 3:
        break
    else:
        print("Invalid option, try again")
