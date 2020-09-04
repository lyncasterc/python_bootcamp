# Define Bank Account Below:
class BankAccount:
    def __init__(self,owner,balance=0.0):
      self.owner = owner
      self.balance = balance
    
    def deposit(self,num):
        self.balance += num
        return self.balance
    
    def withdraw(self,num):
        self.balance -= num
        return self.balance

account1 = BankAccount("Charlie")

account1.deposit(1203)

print(account1.balance)

account1.withdraw(100)

print(account1.balance)