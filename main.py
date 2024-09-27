
from account_manager import AccountManager

def main():
    manager = AccountManager()
    account1 = manager.create_account("savings", 101, "Mayur", 1000)
    account2 = manager.create_account("checking", 102, "Yash", 5000)

    print(f"Mayur's balance: {account1.get_balance()}")
    print(f"Yash's  balance: {account2.get_balance()}")

    print(f"Yash deposited : {account1.deposit(2000)} ")
    print(f"Mayur withdrawed : {account2.withdraw(300)}")

    print(f"Mayur's balance: {account1.get_balance()}")
    print(f"Yash's  balance: {account2.get_balance()}")

    print(account1.apply_interest())
    print(f"Mayur's balance: {account1.get_balance()}")
    
if __name__ == "__main__":
    main()
