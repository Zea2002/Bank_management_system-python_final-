class User:
    def __init__(self, bank_instance):
        self.bank = bank_instance

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        self.bank.withdraw(account_number, amount)

    def check_balance(self, account_number):
        self.bank.check_balance(account_number)

    def see_transaction(self, account_number):
        self.bank.check_transaction_history(account_number)

    def fund_transfer(self, account_number, receiver_acc_number, amount):
        self.bank.fund_transfer(account_number, receiver_acc_number, amount)

    def take_loan(self, account_number, amount):
        self.bank.take_loan(account_number, amount)

