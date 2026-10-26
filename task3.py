class BankAccount:
    def __init__(self, owner, balance ):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('Сумм больше нуля')


account = BankAccount('Ivan', 500)
account.deposit(1000)
print(account.get_balance())