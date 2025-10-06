class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("not enough funds in account")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
