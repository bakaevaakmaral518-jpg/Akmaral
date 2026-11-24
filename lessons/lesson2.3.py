# принципы ООП: Инкапсуляция, Абстракция. Гит - ветки

class BankAccount:
    def __init__(self, owner, balance, code):
        self._owner = owner
        self.__balance = balance
        self.__code = code

    @property
    def code(self):
        #геттер
        return self.__code

    @code.setter
    def code(self, new_code):
        #сеттер
        self.__code = new_code

    # геттер
    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Сумма больше вашего баланса")
            return
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

igor_account = BankAccount(
    "Igor",
    100_000,
    "qwerty",
)

# igor_account.code = "12345"
# igor_account.owner = "Akmaral"
igor_account._owner = "Akmaral"
print(igor_account._owner)
# print(igor_account.__balance)
igor_account.__balance = 0
print(igor_account.__balance)
print(igor_account.get_balance())
igor_account.withdraw(100_000_000)
igor_account.withdraw(1_000)
print(igor_account.get_balance())
print(igor_account.code)
igor_account.code = "1234"
print(igor_account.code)
print(igor_account._BankAccount__balance) # так писать не стоит