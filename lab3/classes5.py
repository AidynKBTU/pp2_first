class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

owner = input()
initial_balance = float(input())
account = Account(owner, initial_balance)

deposit_amount = float(input())
account.deposit(deposit_amount)

withdraw_amount = float(input())
account.withdraw(withdraw_amount)
