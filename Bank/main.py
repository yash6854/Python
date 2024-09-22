
from account_manager import AccountManager

def main():
    manager = AccountManager()
    account1 = manager.create_account("savings", 101, "Mayur", 1000)
    account2 = manager.create_account("checking", 102, "Yash", 500)


    print(f"Mayur's balance: {account1.get_balance()}")
    print(f"Yash's  balance: {account2.get_balance()}")
    


if __name__ == "__main__":
    main()
