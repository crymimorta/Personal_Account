from PersonalAccount import PersonalAccount
if __name__ == "__main__":
    account = PersonalAccount(123456, "John Doe")
    print(account)
    
    account.deposit(500)
    print(f"Balance after deposit: ${account.get_balance():.2f}")
    
    account.withdraw(200)
    print(f"Balance after withdrawal: ${account.get_balance():.2f}")
    
    account.print_transaction_history()
    
    account + 300
    account - 100  
    print(f"Balance after operations: ${account.get_balance():.2f}")
    account.print_transaction_history()

    account.__add__(500)
    account.get_balance()

    account.__sub__(150)
    account.print_transaction_history()
    print(account.get_balance())