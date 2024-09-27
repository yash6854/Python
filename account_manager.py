
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number, holder_name, initial_deposit=0.0):
        if account_type == "savings":
            account = SavingsAccount(account_number, holder_name, initial_deposit)
        elif account_type == "checking":
            account = CheckingAccount(account_number, holder_name, initial_deposit)
        else:
            return None
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)
