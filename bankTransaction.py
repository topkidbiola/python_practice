class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        
    def withdraw(self, amount):
        if 0 < amount <+ self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Insufficient funds"
        
account = BankAccount("8134726471", 500000)
print("Account Number:",account.get_account_number())
print("Initial Balance:",account.get_balance())
print("Balance after deposit of 200000:",account.deposit(200000))
print("Balance after withdrawal of 100000:",account.withdraw(100000))
print("Attempt to withdraw 700000:",account.withdraw(700000))

        
