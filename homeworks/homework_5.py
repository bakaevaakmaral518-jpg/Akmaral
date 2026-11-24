class Distance:
    conversion_dict = {
        "centimeters": 0.01,
        "meters": 1,
        "kilometers": 1000,
        "millimeters": 0.001
    }

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __init__(self, value, unit):
        if unit not in Distance.conversion_dict:
            raise ValueError("Invalid unit")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"


    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total = self.convert() + other.convert()
        result = total / self.conversion_dict[self.unit]

        return Distance(result, self.unit)


    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total = self.convert() - other.convert()
        result = total / self.conversion_dict[self.unit]

        return Distance(result, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert() == other.convert()

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert() < other.convert()

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert() > other.convert()

    def __le__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert() <= other.convert()

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert() >= other.convert()


distance1 = Distance(10, "meters")
distance2 = Distance(2, "kilometers")
distance3 = Distance(500, "centimeters")
distance4 = Distance(3, "meters")

print("Первое расстояние:", distance1)
print("Второе расстояние:", distance2)
print("Третье расстояние:", distance3)

print("Сложение:", distance1 + distance2)

print("Вычитание:", distance2 - distance1)

print("Равны ли расстояния?", distance1 == distance2)
print("Первое меньше второго?", distance1 < distance2)
print("Первое больше второго?", distance1 > distance2)

print("100 метров == 10000 сантиметров:",
      Distance(100, "meters") == Distance(10000, "centimeters"))
