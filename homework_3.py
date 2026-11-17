TRIP_COST = 20

class TransportCard:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError(f"Ошибка: Нельзя пополнить карту на сумму {amount}. Сумма должна быть больше 0.")

        self.__balance += amount
        print(f"Успешно пополнено на {amount} сомов. Текущий баланс: {self.__balance}")

    def pay_for_trip(self):
        if self.__balance >= TRIP_COST:
            self.__balance -= TRIP_COST
            print(f"Поездка оплачена! Списано {TRIP_COST}. Текущий баланс: {self.__balance}")
        else:
            raise ValueError(f"Ошибка: Недостаточно средств на карте владельца {self.__owner}. Баланс: {self.__balance}")


card1 = TransportCard("Иван")
card2 = TransportCard("Айсулуу")

card1.add_money(100)

print(card1.get_owner())
print(card1.get_balance())

card1.pay_for_trip()
print(card1.get_balance())

try:
    card2.pay_for_trip()
except ValueError as error:
    print(error)

try:
    card1.add_money(-50)
except ValueError as error:
    print(error)
