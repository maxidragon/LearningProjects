# balance, funkcja do wplacenia, do wyplaty (sprawdzanie stanu), owner, przeliczanie walut, waluta konta, funkcja przewalutowania
from forex_python.converter import CurrencyRates

c = CurrencyRates()


class BankAccount:

    def __init__(self, balance: float, owner: str, currency: str):
        """
        The __init__ function is a special function that Python runs automatically whenever we create a new instance based on the Account class.
        The __init__ function allows us to perform any tasks that are necessary every time we use the new instance of this class.

        :param self: Refer to the object itself
        :param balance:float: Set the initial balance of the account
        :param owner:str: Store the name of the account owner
        :param currency:str: Set the currency of the account
        :return: The object that is created
        :doc-author: Trelent
        """

        self.balance = balance
        self.owner = owner
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "You don't have enough money"
        else:
            self.balance -= amount

    @staticmethod
    def convert_currencies(amount, currency):
        return amount * c.get_rate('PLN', currency)

    def change_currency(self, currency):
        self.balance = self.balance * c.get_rate(self.currency, currency)
        self.currency = currency
    def __str__(self):
        return f'{self.balance} {self.currency}'

ba1 = BankAccount(10, 'Jan Kowalski', 'PLN')
ba1.change_currency('EUR')
print(ba1.balance)
# print(BankAccount.convert_currencies(10, 'EUR'))
print(ba1)