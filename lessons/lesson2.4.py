# ООП - Магические, статичные методы. Гит - слияние веток
# from abc import ABC, abstractmethod
#
#
# # Абстракция
# class Notification:
#     @abstractmethod
#     def send(self, message):
#         pass
#
#
#
# class Email(Notification):
#     # реализация абстрактного метода
#     def send(self, message):
#         print(f"уведомление по почте: {message}")
#
# class SMSNotification(Notification):
#     pass
#
# email_not = EmailNotification()
# email_not.send("привет мир")
# try:
#     sms_not = SMSNotification()
# except TypeError as e:
#     print(e)


class Visitor:
    organization = "Курсы"
    created_count = 0
    self.visitors 

    def __init__(self, name):
        self.name = name
        print(Visitor.created_count)

    def introduce(self):
        print(f"Меня зовут {self.name}")

    @classmethod
    def get_organization(cls):
        return Visitor.organization

    @classmethod
    def create_vip_visitors(cls, name):
        # альтернативный конструктор
        new_visitor = Visitor(name)
        new_visitor.visitor_type = "vip"
        return new_visitor




visitor = Visitor("Igor")
print(Visitor.created_count)
Visitor.organization = "Курсы Geeks"
visitor1 = Visitor("Igor")
print(visitor1.visitor_type)
print(Visitor.created_count)
print(Visitor.get_organization())
vip_visitor = Visitor.create_vip_visitors("Ali")
print(vip_visitor.visitor_type)