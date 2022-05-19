# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, val_dep):
        self.balance += val_dep
        return self.balance
        
    def withdraw(self, val_with):
        self.balance -= val_with
        return self.balance

acc = BankAccount("Darcy")
print(f"Balance of {acc.owner} is {acc.balance}")

acc.deposit(200)
print(f"Balance of {acc.owner} is {acc.balance}")

acc.withdraw(120)
print(f"Balance of {acc.owner} is {acc.balance}")