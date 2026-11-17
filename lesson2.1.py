class Car:
    def __init__(self, marka, color):
        self.marka = marka
        self.color = color

    def drive_to(self, destination):
        print(f"Машина марки {self.marka} едет в{destination}")

car_1 = Car("BMW", "black")
car_2 = Car("Mercedes", "blue")
print(car_1, car_2)
print(f"Car 1: {car_1.marka} {car_2.color}")
print(f"Car 2: {car_1.marka} {car_2.color}")
car_2.drive_to("Каракол")
print(type(car_1))


class Player:
    def __init__(self, name, character, health):
        self.name = name
        self.character = character
        self.health = health

player_1 = Player("Joy", "funny", "90")
player_2 = Player("Dav", "nervos", "100")
player_3 = Player("Ban", "okay", "100")
print(player_1, player_2, player_3)
print(f"Player 1: {player_1.name} {player_1.character} {player_1.health}")
print(f"Player 2: {player_2.name} {player_2.character} {player_2.health}")
print(f"Player 3: {player_3.name} {player_3.character} {player_3.health}")