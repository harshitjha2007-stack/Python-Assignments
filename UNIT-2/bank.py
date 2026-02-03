# Create a class to represent a bank account. Include attributes like account number, balance, and methods like deposit, withdraw and check balance.


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposit successful.","New Balance: ",self.balance )


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal Sucessful", "New Balance: " ,self.balance)


    def check_balance(self):
        return self.balance
    

account= BankAccount("ACC2007",1464281)
print(account.deposit(200000))
print(account.withdraw(25000))
print(account.check_balance())