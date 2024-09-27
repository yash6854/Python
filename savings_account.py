
from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
