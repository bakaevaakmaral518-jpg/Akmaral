# принципы ООП -  Наследование, Полиморфизм. Гит - коммиты, создание репозитория, git push
# Наслдеование
# родительский класс, предок, суперкласс
class Car:
    def __init__(self, marka, color):
        self.marka = marka
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def drive_to(self, destination):
        print(f"Машина марки {self.marka} едет в{destination}")

class ElectroCar(Car):
    def __init__(self, marka, color):
        super().__init__(marka, color)    # super - отсылка к род.классу
        self.battery = 0

    def drive_to(self, destination):
        if self.battery > 5:
            super().drive_to(destination)
            print(f"Электро-машина марки {self.marka} с зарядом {self.battery} едет в {destination}")
        else:
            print(f"Мало заряда, не могу поехать в {destination}")

    def charge_battery(self):
        print("Идет заряд...")
        self.battery += 10
        if self.battery >= 100:
            self.battery = 100

class SportCar(Car):
    pass

tesla = ElectroCar("Tesla", "red")
print(f"Electro car {tesla.marka}, {tesla.color}")
tesla.drive_to("Кара-Балта")
tesla.charge_battery()
tesla.drive_to("Кара-Балта")

# Полиморфизм
car_1 = Car("Mercedes", "blue")
car_2 = SportCar("Ferrary", "red")

tesla.drive_to(destination="Бишкек")
car_1.drive_to(destination="Бишкек")
car_2.drive_to(destination="Бишкек")

vehicles = [tesla, car_1, car_2]
