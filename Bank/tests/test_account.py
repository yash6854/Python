# tests/test_account.py
import unittest
from Bank.savings_account import SavingsAccount
from Bank.checking_account import CheckingAccount

class TestAccounts(unittest.TestCase):
    def test_savings_account(self):
        account = SavingsAccount(123, "Alice", 1000)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)
        account.withdraw(200)
        self.assertEqual(account.get_balance(), 1300)

    def test_checking_account(self):
        account = CheckingAccount(456, "Bob", 500)
        account.withdraw(700)
        self.assertEqual(account.get_balance(), -200)
        account.deposit(300)
        self.assertEqual(account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
