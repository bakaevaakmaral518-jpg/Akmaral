class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__is_available = True


    def borrow_book(self):
       if self.__is_available:
           self.__is_available = False
           print("Книга успешно выдана!")
       else:
           print("Книга уже выдана!")


    def return_book(self):
        if self.__is_available:
            print("Книга доступна! Возварщать не нужно!")
        else:
            self.__is_available = True
            print("Книга успешно возвращена!")

    def show_info(self):
        print(self.title)
        print(self.author)
        print(self.year)
        if self.__is_available:
            print("Статус: доступна")
        else:
            print("Статус: выдана ")




book = Book("Гарри Поттер", "Джоан Роулинг", 1997)

book.borrow_book()
book.borrow_book()
book.return_book()
book.show_info()




# expenses = []
# while True:
#     user = int(input("Введите свои расходы: "))
#     if user == 0:
#         break
#
#     expenses.append(user)
#
# print("Ваши расходы: ", expenses)
#
# def calculate_expenses():
#     total = sum(expenses)
#     print("Общая сумма: ", total)
#
# calculate_expenses()
#
# print("Самый большой расход: ", max(expenses))
# print("Самый маленький расход: ", min(expenses))

# c = float(input("Введите температуру в градусах Цельсия: "))
# # переводим в градусы Фаренгейта
# f = (9/5)*c + 32
# print(c, " градусов Цельсия равны ", f,  " градусам Фаренгейта")

# p = float(input("Начальная сумма вклада: "))
# r = float(input("Процент по вкладу: "))
# t = float(input("Количество лет: "))
#
# bank = (p*r*t) / 100
# print("Начисленные проценты: ", bank)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = list(filter(lambda elem: elem in b, a ))
# print(result)



# for i in range(5):
#     user = int(input("Введите цифру: "))
#     if user %2 == 0:
#         print("число четное")
#     else:
#         print("Число нечетное")



# a = 0
# for i in range(5):
#     user = int(input("Введите число: "))
#     a += user
# print(a)


# numbers = [12, 5, 28, 9, 17, 3]
# max_number = 12
# min_number = 12
# for number in numbers:
#     if number >= max_number:
#         max_number = number
#     if number <= min_number:
#         min_number = number
# print(f"Максимальное число: {max_number}")
# print(f"Минимальное число: {min_number}")


# class Student:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Меня зовут {self.name} мне {self.age} лет")
#
# student1 = Student("Anna", 18)
# student2 = Student("Bob", 22)
#
# student1.introduce()
# student2.introduce()