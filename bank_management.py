import random
from datetime import datetime

class Bank:
    total_loan_amount = 0
    accounts = {}
    def __init__(self):
        self.loan_limit = 2
        self.bankrupt = False
        self.loan_feature_enabled = True 

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100000, 999999)
        self.accounts[account_number] = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "balance": 0,  
            "transactions": [],  
            "loan_count": 0
        }
        print(f"Mr.{name}, Your account has been successfully created. Your account number is: {account_number}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Deposited {amount}, datetime: {datetime.now()}")
            print(f"{amount} deposited successfully")
        else:
            print("Account does not exist")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Your current balance is: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if not self.bankrupt:
                if amount <= self.accounts[account_number]["balance"]:
                    self.accounts[account_number]["balance"] -= amount
                    self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Withdraw {amount}, datetime: {datetime.now()}")
                    print(f"{amount} withdrawn successfully")
                else:
                    print("Invalid withdrawal amount")
            else:
                print("The bank is bankrupt")
        else:
            print("Account does not exist")

    def check_transaction_history(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number]["transactions"])
        else:
            print("Account does not exist")

    def take_loan(self, account_number, amount):
        if account_number in self.accounts and not self.bankrupt and self.loan_feature_enabled:
            if self.accounts[account_number]["loan_count"] < self.loan_limit:
                    self.accounts[account_number]["balance"] += amount
                    self.total_loan_amount += amount
                    self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Took loan {amount}, datetime: {datetime.now()}")
                    self.accounts[account_number]["loan_count"] += 1
                    print(f"{amount} loan successful")
            else:
                print("Maximum loan limit reached")
        elif not self.loan_feature_enabled:
            print("The loan feature is currently disabled.")
        else:
            print("Account does not exist")

    def fund_transfer(self, account_number, receiver_acc_number, amount):
        if account_number in self.accounts:
            if receiver_acc_number in self.accounts:
                if amount <= self.accounts[account_number]["balance"] and amount >= 0:
                    self.accounts[account_number]["balance"] -= amount
                    self.accounts[receiver_acc_number]["balance"] += amount
                    print(f"{amount} transfer successful")
                else:
                    print("Invalid transfer amount or insufficient balance")
            else:
                print("Receiver account does not exist")
        else:
            print("Sender account does not exist")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status
        print("Loan feature is now", "enabled" if status else "disabled")

    def toggle_bankrupt_status(self, status):
        self.bankrupt = status
        print("Bankrupt status is now", "enabled" if status else "disabled")
