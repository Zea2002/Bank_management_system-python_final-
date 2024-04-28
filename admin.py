class Admin:
    def __init__(self, name, email, bank_instance):
        self.name = name
        self.email = email
        self.bank = bank_instance

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)
    
    def see_all_user_accounts(self):
        for account_number, account_info in self.bank.accounts.items():
            print(f"Account Number: {account_number}")
            print(f"Name: {account_info['name']}")
            print(f"Email: {account_info['email']}")
            print(f"Address: {account_info['address']}")
            print(f"Account Type: {account_info['account_type']}")
            print(f"Balance: {account_info['balance']}")
            print("------------------------")

    def check_total_loan_amount(self):
        print(f"Total loan amount is: {self.bank.total_loan_amount}")

    def total_available_balance(self):
        print(f"Total available balance is: {sum(acc['balance'] for acc in self.bank.accounts.values())}")

    def toggle_loan_feature(self, status):
        self.bank.toggle_loan_feature(status)

    def change_bankrupt_status(self, status):
        self.bank.toggle_bankrupt_status(status)

