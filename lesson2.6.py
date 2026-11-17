# Множественное наследование
class Flying:
    def fly(self):
        print("умею летать")

class Swimming:
    def swim(self):
        print("умею плавать")

class Duck(Flying, Swimming):
    pass

class InfoMixin:
    def show_info(self):
        print(self.get_info())

class NamedObject:
    def __init__(self, name):
        self.name = name

class Product(InfoMixin, NamedObject):
    def get_info(self):
        return f"Товар: {self.name}"

class Room(InfoMixin, NamedObject):
    def get_info(self):
        return f"Помещение: {self.name}"


#SOLID  = SRP(SingleResponsibilityPrinciple) + ...
Product("кроссы").show_info()
Room("аудитрория 2-4").show_info()
donald = Duck()
donald.fly()
donald.swim()

# MRO - Method Resolution order - порядок поиска метода
class Animal:
    def move(self):
        print("Животное двигается")

class Flying(Animal):
    def move(self):
        print("умею летать")

class Swimming(Animal):
    def move(self):
        print("умею плавать")
        # super().move()

class Duck(Swimming, Flying):
    def move(self):
        print("Утка плавает и летает")
        super().move()

donald = Duck()
donald.move()
print(Duck.mro())
print(Duck.__mro__)