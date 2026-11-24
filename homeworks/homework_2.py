class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}", end="")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print(f", я одногруппник Марсэля, моя группа {self.group_name}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f", я друг Марсэля, мое хобби {self.hobby}")


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f", наше общее воспоминание это {self.shared_memory}")


classmate1 = Classmate("Бек", "22.09.2002", "Экономистом", "КЛ-1-23")
classmate2 = Classmate("Нурбол", "07.07.2009", "Энергетиком", "БИС-2-23")

friend1 = Friend("Искен", "16.12.2005", "Инженером", "Шахматы")
friend2 = Friend("Султан", "25.05.2005", "Переводчиком", "Дзюдо")

bestfriend1 = BestFriend("Акылай", "23.01.2006", "Учителем", "Судоку", "игра на песочнице")
bestfriend2 = BestFriend("Танзиля", "10.10.2006", "СММ специалистом", "Чтение книг", "прогулка под дождем")


class_list = [classmate1, classmate2, friend1, friend2, bestfriend1, bestfriend2]
for i in class_list:
    i.introduce()