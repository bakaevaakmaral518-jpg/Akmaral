class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Гав гав гав"


class Cat(Animal):
    def make_sound(self):
        return "Мяу мяу"

kitty = Cat("Барбариска", 2)
kitty.set_age(3)
kitty.set_name("Мурка")

dog = Dog("Тайга", 4)
dog.set_age(2)
dog.set_name("Лев")

print(kitty.get_age())
print(kitty.get_name())
print(kitty.make_sound())
print(dog.get_age())
print(dog.get_name())
print(dog.make_sound())