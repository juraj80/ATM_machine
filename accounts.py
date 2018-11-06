
class Account:
    '''This is a bank account class'''
    def __init__(self, name = "BankAccount", balance = 10000):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("You now have: ", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("You now have: ", self.balance)

class currentAccount(Account):
    '''This is a current account class'''
    def __init(self, name ='Current Account', balance = 10000):
        self.name =  name
        self.balance = balance
 #       super().__init__()

    def withdraw(self, amount):
        if amount > 1000:
            print("The amount exceeded the maximum limit for daily withdrawal")
        else:
#            self.balance = self.balance - amount
            super().withdraw(amount)


class savingsAccount(Account):
    def __init__(self, name = 'Savings Account', balance = 5000):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("You now have: ", self.balance)
