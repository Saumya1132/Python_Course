# simulate basic bank account using bank account class

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self.balance
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    
    def transfer(self, amount, to_account):
        if self.withdraw(amount):
            to_account.deposit(amount)
            return True
        else:
            return False
    
    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Current Balance:", self.balance)
    
    def get_account_holder_name(self):
        return self.account_holder_name
    
    def get_account_number(self):
        return self.account_number
    
account1 = BankAccount("12345678", "Alice Smith", 500)
account2 = BankAccount("87654321", "Bob Johnson", 1000)

print("Initial Account Info:")
account1.display_account_info()
account2.display_account_info()

account1.deposit(200)
print("\nAfter depositing $200 into account1:")
account1.display_account_info()

account2.withdraw(150)
print("\nAfter withdrawing $150 from account2:")
account2.display_account_info()

account1.transfer(300, account2)
print("\nAfter transferring $300 from account1 to account2:")
account1.display_account_info()
account2.display_account_info()

print("\nFinal Balances:")
print(f"Account 1 balance: ${account1.get_balance()}")
print(f"Account 2 balance: ${account2.get_balance()}")
