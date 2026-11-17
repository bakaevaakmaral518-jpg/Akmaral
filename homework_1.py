class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education = "есть"
        else:
            education = "нет"

        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation},"
              f" высшее(го) образование(я) {education}")

person1 = Person("Бек", "22.09.2002", "Экономист", True)
person2 = Person("Нурбол", "07.07.2009", "Энергетик", False)
person3 = Person("Бурул", "21.03.2006", "Компьютерная Лингвистика", False)
person4 = Person("Танзиля", "08.10.2005", "Программист", False)

print(f"Person 1: {person1.name} {person1.birth_date} {person1.occupation} {person1.higher_education}")
print(f"Person 2: {person2.name} {person2.birth_date} {person2.occupation} {person2.higher_education}")

person1.introduce()
person2.introduce()
person3.introduce()
person4.introduce()







