# class Animal:
#     has_tail=True
#     number_of_legs=4
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
#
# dog=Dog()
# cat=Cat()
# print(f"Тварина хвіст{Cat.has_tail},  кількість лап{Cat.number_of_legs}")
# print(f"Собака хвіст{Cat.has_tail},  кількість лап{Cat.number_of_legs}")
# print(f"Кіт хвіст{Cat.has_tail},  кількість лап{Cat.number_of_legs}")
# 2
# class Person:
#     name="Саша"
#     age=87
#     def __init__(self,age=87):
#         self.age=age
# class Driver(Person):
#     drivers_license_number=123456
#
# osoba = Person()
# vodiy = Driver()
# print(f"Особа: {osoba.name}, {osoba.age}")
# print(f"Водій: {vodiy.name}, {vodiy.age}, номер водійського посвідчення: {vodiy.drivers_license_number}")
# 3
# class Vehicle:
#     speed=40
#     def __init__(self, moving=3):
#         self.moving=moving
# class Bus(Vehicle):
#     def __init__(self):
#         super().__init__()
# class Motorcycle(Vehicle):
#     def __init__(self):
#         super().__init__()
#
# c=Bus()
# v=Vehicle()
# m=Motorcycle()
# print(f"Транспортний засіб  швидкість {c.speed}, переміщення {c.moving}")
# print(f"Автобус  швидкість {v.speed}, переміщення{v.moving}")
# print(f"Мотоцикл  швидкість {m.speed}, переміщення{m.moving}")
# 4
# class Device:
#     def __init__(self):
#         self.on = False
#         self.off = True
# class Tablet(Device):
#     def __init__(self):
#         super().__init__()
#
# class Phone(Device):
#     def __init__(self):
#         super().__init__()
# class Decktop(Device):
#     def __init__(self):
#         super().__init__()
# d=Device()
# t=Tablet()
# p=Phone()
# dec=Decktop()
# print(f"Девайс Ввімкнуте {d.on}, вимкнуте {d.off}")
# print(f" Планшет Ввімкнуте {t.on}, вимкнуте {t.off}")
# print(f" Телефон Ввімкнуте {p.on}, вимкнуте{ p.off}")
# print(f" Ноутбук Ввімкнуте{ dec.on}, вимкнуте {dec.off}")
#  5
class Programminglanguage:
    name="Python"
    def __init__(self, display_greetings="Hello World"):
        self.display_greetings=display_greetings
class JavaScript(Programminglanguage):
    def __init__(self):
        super().__init__()
class Java (Programminglanguage):
    def __init__(self):
        super().__init__()
class HTMLCSS (Programminglanguage):
    def __init__(self):
        super().__init__()

p=Programminglanguage()
j=Java()
js=JavaScript()
h=HTMLCSS()
print(f"Мова програмування {p.name}, привітання {p.display_greetings} ")
print(f" Java- мова програмування назва {j.name}, привітання {j.display_greetings} ")
print(f" JavaScript- мова програмування назва {js.name}, привітання {js.display_greetings} ")
print(f"HTML/CSS- мова програмування назва {h.name}, привітання {h.display_greetings} ")