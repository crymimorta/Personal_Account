from Amount import Amount
class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount > 0:
            transaction = Amount(amount, 'DEPOSIT')
            self.transactions.append(transaction)
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount>0 and self.balance>= amount:
            transaction = Amount(amount, 'WITHDRAW')
            self.transactions.append(transaction)
            self.balance-=amount
        else: print('Insufficient funds')
    
    def print_transaction_history(self):
        if self.transactions:
            print(f"Transaction history for {self.account_holder}:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions yet.")
    
    def get_balance(self):
        return self.balance
    
    def get_account_number(self,):
        return self.account_number
    
    def set_account_number(self, account_number):
        self.account_number = account_number
    
    def get_account_holder(self):
        return self.account_holder
    
    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance:.2f}"
    
    def __add__(self, amount: float):
        self.deposit(amount)
        return self
    
    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self