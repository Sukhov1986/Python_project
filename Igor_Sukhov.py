# try:
#     number = int(input("Введите число -> "))
# except ValueError:
#     print("Должно быть число ")
#     exit()
# tpl = tuple(str(i) for i in str(number))
# print(tpl)
# lst = []
# for i in tpl:
#     if i not in lst:
#         lst.append(i)
# print(lst)
# for i in lst:
#     print(f"{i} = {tpl.count(i)}")

# string = input('Введите строку -> ').lower()
# vowels_1 = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
# vowels_2 = [x for x in string if x in vowels_1]
# print(f'Количество гласных равно : {len(vowels_2)}')

# dictionary_1 = {"name": "kelly", "age": 25, "salary": 8000, "city": "New York"}
# print(dictionary_1)
# dictionary_2 = {key: dictionary_1[key] for key in dictionary_1 if key in ["name", "salary"]}
# for i in dictionary_2:
#     dictionary_1.pop(i)
#
#
# print(dictionary_1)
# print(dictionary_2)
#

# # print(dictionary_1)
# dictionary_2 = {key: dictionary_1[key] for key in dictionary_1 if key in ["name", "salary"]}
# for i in dictionary_2:
#     dictionary_1.pop(i)
#
#
# print(dictionary_1)
# print(dictionary_2)


# from prettytable import PrettyTable
#
# Total_Sales = {'January': 52000, 'February': 51000, "March": 48000}
# Production_Cost = {'January': 46800, 'February': 45900, "March": 43200}
# profit = dict(zip(Total_Sales.keys(),
#                   [sales - cost for sales, cost in zip(list(Total_Sales.values()), list(Production_Cost.values()))]))

# # print(profit)

# print(profit)

# table = PrettyTable(['Element/Month', 'January', 'February', "March"])
# table.align = 'r'
# table.align['Element/Month'] = "l"
# table.add_row(['Total Sales', Total_Sales['January'], Total_Sales['February'], Total_Sales["March"]])
# table.add_row(['Production Cost', Production_Cost['January'], Production_Cost['February'], Production_Cost["March"]])
# table.add_row(['Profit', profit['January'], profit['February'], profit["March"]])
# print(table)


# def main():
#     quantity = int(input("Введите количество учеников :"))
#     return quantity
#
#
# def data(**kwargs):
#     return kwargs
#
#
# def data_input():
#     s_surname = input("Введите фамилию :")
#     s_name = input("Введите имя :")
#     s_point = int(input("Введите балл :"))
#     return s_surname, s_name, s_point
#
#
# students = main()
# lst = []
# res = 0
# for i in range(students):
#     a, b, c = data_input()
#     res += c
#     x = data(surname=a, name=b, point=c)
#     lst.append(x)
# average_mark = res / students
# average_result = round(average_mark)
# print(f"Средний балл {average_result}. Студенты с баллом выше среднего :")
# for i in lst:
#     if i["point"] > average_result:
#         print(i["name"])

from math import pi

figures = {
    "circle": lambda x: x ** 2 * pi,
    "rectangle": lambda x, y: x * y,
    "trapezoid": lambda a, b, h: 0.5 * (a + b) * h
}


def circle():
    x = int(input("Введите радиус : "))
    return x


def rectangle():
    x, y = [int(input(f"Введите сторону прямоугольника {i} : ")) for i in ["1", "2"]]
    return x, y


def trapezoid():
    x, y, z = [int(input(f"Введите {i} : ")) for i in ["длину основания 1", "длину основания 2", "высоту"]]
    return x, y, z


circle_ = circle()
side_1, side_2 = rectangle()
base_1, base_2, height = trapezoid()

print(f"Площадь окружности радиуса {circle_} : {figures['circle'](circle_)}")
print(f"Площадь прямоугольника размером {side_1}*{side_2} : {figures['rectangle'](side_1, side_2)}")
print(f"Площадь трапеции для a={base_1}, b={base_2}, h={height} : {figures['trapezoid'](base_1, base_2, height)}")


def decorator(fn):
    def wrapper(*args):
        return fn(*args) / len(args)

    return wrapper


@decorator
def summ(*args):
    return sum(args)


print(summ(2, 3, 3, 4))


def function(x, y):
    if x > y:
        x, y = y, x
    return list(map(chr, [i for i in range(x, y + 1)]))


a, b = 122, 97

print(*function(a, b))

str1 = "I am learning Python. hello, WORLD!"
letter = "h"
str1 = str1[:str1.find(letter) + 1] + str1[str1.find(letter) + 1:str1.rfind(letter)][::-1] + str1[str1.rfind(letter):]
print(str1)

import re

text_ = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
pattern = r"[\w.-]+@[\w.]*\.ru\b"
print(re.findall(pattern, text_))

import re

tel = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78 "
req = r"\+*7(?:[\s(]*\d{3}[\s)]*){2}[-\s]*\d{2}[\s-]*\d{2}"
print(re.findall(req, tel))


def negative_number(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative_number(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative_number(lst))

txt = ("Замена строки в текстовом файле;\n"
       "Записать список в файл;\n"
       "Изменить строку в списке;\n")


def file_creation(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def replacement(file):
    with open(file, "r") as f:
        lines = f.readlines()
    while True:
        pos1, pos2 = [int(input(f"Заменить {val}")) for val in ["строку: ", "на строку: "]]
        if 0 < pos1 <= len(lines) and 0 < pos2 <= len(lines):
            lines[pos1 - 1], lines[pos2 - 1] = lines[pos2 - 1], lines[pos1 - 1]
            break
        else:
            print(f"Неверный диапазон строк.Допустимое значение от 1 до {len(lines)}")

    with open(file, "w") as f:
        f.writelines(lines)


file_creation("filename.txt", txt)
replacement("filename.txt")

import os

dirs = "Homework"
nested = ["test", "test1"]
file_name = ["project.txt", "test.txt"]
for d in nested:
    os.makedirs(os.path.join(dirs, d), exist_ok=True)
    for file in file_name:
        file_path = os.path.join(dirs, file)
        with open(file_path, "w") as f:
            f.write(f"Это файл {file}")


def scanning(directory):
    if os.path.exists(directory):
        contents = os.listdir(directory)
        for i in contents:
            full_path = os.path.join(directory, i)
            print(f"{i} - file - {os.path.getsize(full_path)} bytes" if os.path.isfile(full_path) else f"{i} - dir")
    else:
        print("Такого пути не существует")


scanning(dirs)


class Automobile:
    def __init__(self):
        self.model = ""
        self.year = ""
        self.manufacturer = ""
        self.engine_power = ""
        self.color = ""
        self.price = ""

    def input_data(self):
        self.model = input("Модель автомобиля :")
        self.year = input("Год выпуска :")
        self.manufacturer = input("Производитель :")
        self.engine_power = input("Мощность двигателя :")
        self.color = input("Цвет машины :")
        self.price = input("Цена :")

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель : {self.manufacturer}")
        print(f"Мощность двигателя : {self.engine_power} л.с.")
        print(f"Цвет машины : {self.color}")
        print(f"Цена : {self.price}")
        print("=" * 40)

    def update_model(self):
        new_model = input("Введите новую модель автомобиля: ")
        self.model = new_model

    def update_year(self):
        new_year = input("Введите новый год выпуска: ")
        self.year = new_year

    def update_manufacturer(self):
        new_manufacturer = input("Введите нового производителя: ")
        self.manufacturer = new_manufacturer

    def update_engine_power(self):
        new_engine_power = input("Введите новую мощность двигателя: ")
        self.engine_power = new_engine_power

    def update_color(self):
        new_color = input("Введите новый цвет машины: ")
        self.color = new_color

    def update_price(self):
        new_price = input("Введите новую цену: ")
        self.price = new_price


car1 = Automobile()
car1.input_data()
car1.print_info()
car1.update_color()
car1.print_info()

import turtle  # нужно импортировать модуль


class Rectangle:
    def __init__(self):
        self.length = int(input("Введите длину прямоугольника : "))
        self.width = int(input("Введите ширину прямоугольника : "))

    def methods(self):
        while True:
            print("Выберите интересующий вас метод: ".center(40, "*"))
            print("1 Площадь прямоугольника\n"
                  "2 Периметр прямоугольника\n"
                  "3 Гипотенуза прямоугольника\n"
                  "4 Нарисовать прямоугольник")
            choice = int(input("Введите номер метода : "))
            if choice == 1:
                self.square()
            elif choice == 2:
                self.perimeter()
            elif choice == 3:
                self.hypotenuse()
            elif choice == 4:
                self.draw()
            else:
                print("Введите правильный номер метода".center(40, "*"))
            if 0 < choice < 5:
                break

    def square(self):
        print(f"Площадь прямоугольника: {self.length * self.width}")

    def perimeter(self):
        print(f"Периметр прямоугольника: {2 * (self.length + self.width)}")

    def hypotenuse(self):
        print(f"Гипотенуза прямоугольника: {0.5 * (self.length ** 2 + self.width ** 2)}")

    def draw(self):
        t = turtle.Turtle()
        for _ in range(2):
            t.forward(self.length)
            t.left(90)
            t.forward(self.width)
            t.left(90)
        turtle.done()


rectangle1 = Rectangle()
rectangle1.methods()


class Person:

    def __init__(self, name, old):
        if Person.__check_value_old(old) and Person.__check_value_name(name):
            self.__name = name
            self.__old = old
        else:
            raise ValueError("Неправильный ввод данных")

    @staticmethod
    def __check_value_name(n):
        if isinstance(n, str):
            return True
        return False

    @staticmethod
    def __check_value_old(o):
        if isinstance(o, int):
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if Person.__check_value_name(new_name):
            self.__name = new_name
        else:
            print("Имя должно быть строкой")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if Person.__check_value_old(new_old):
            self.__old = new_old
        else:
            print("Возраст должен быть числом")

    @old.deleter
    def old(self):
        del self.__old


person1 = Person("Irina", 26)
print(person1.name)
print(person1.old)
person1.name = "Igor"
person1.old = 31
print(person1.name)
print(person1.old)
del person1.name
print(person1.__dict__)
