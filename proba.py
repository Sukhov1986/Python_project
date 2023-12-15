# a, b, c = [int(input(f"Введите значение для {var}: ")) for var in ['a', 'b', 'c']]
# a = [1, 2, 3]
# b = a.copy()
# print(a)
# print(b)
# a.append(20)
# print(a)
# print(b)
# b.append(40)
# print(a)
# print(b)
# a = [5, 1, 2, 7, 3]
# # print(a)
# # a.reverse()
# # print(a)
# # a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# b = ["Ivan", "Vitalii", "Sergei"]
# b.sort(key=len, reverse=True)
# print(b)
# a = [5, 1, 2, 7, 3]
# print(a)
#
# sort = sorted(a, reverse=True)
# print(sort)
import random

# # print(random.random())
# # print(random.randint(0, 9))
# # print(random.randrange(3, 9, 2))
# # print(round(random.uniform(10.5, 10.9), 2))
#

# # print(random.choice(city))
# # print(random.choices(city, k=3))
# s = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(random.choices(s, k=5))
# random.shuffle(city)
# print(city)
# lst = [1, 3, 5, 3, 7, 8]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# import random
# lst = [random.randint(0,100) for i in range(10)]
# print(lst)
# min_ = min(lst)
# print(min(lst))
# ind_min_ = lst.index(min_)
# print(ind_min_)
# del lst[0: ind_min_]
# print(lst)
# print(lst[ind_min_:])

# print(x)
# print("1" in x)
# print("e" not in x)
# lst = [9]
# if not lst:
#     print("Пуст")
# else:
#     print("Есть")
# n = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# print(n)
# print()
# # for row in range(len(n)):
# #     print(n[row])
# #     for col in range(len(n[row])):
# #         print(n[row][col], end="\t")
# for row in n:
#     for col in row:
#         print(col, end="\t")

# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)] for i in range(h)]
# # matrix = []
# # for i in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
#
# print(matrix)
# for i in matrix:
#     for j in i:
#         print(i, end="\t")
# matrix = [[random.randint(-20, 10) for x in range(3)] for i in range(4)]
# print(matrix)
# count = 0
# for i in matrix:
#     for j in i:
#         if j < 0:
#             count += 1
# print(count)
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
# matrix = [[random.randint(-20, 10) for x in range(3)] for i in range(4)]
# import math
# num = math.sqrt(4)
# num1 = math.ceil(3.1)
# print(num)
# print(num1)
# print(math.pi)
# import time
# import locale
# locale.setlocale(locale.LC_ALL, "")
#
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
#
# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "x", "y")
# def function(x, y):
#     if x > y:
#         return x - y
#     else:
#         return sum(x, y)
#
#
# a, b = [int(input(f"Введите значение для {var}: ")) for var in ['a', 'b']]
#
# function(10, 11)
#

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе равно = ", cube(i))
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#
#     return lst
#
#
# x = [1, 2, 3]
# y = [9, 12, 53, 45, 134]
#
# result = change(y)
# print(result)
# def function(x, y):
#     if x > y:
#         return True
#     else:
#         return False
# a = 10
# b = 5
#
# print(function(a, b))
# print(function(5, 10))


# def check_password(password):
#     has = False
#     h_l = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has = True
#
#     if len(password) >= 8 and has:
#         return True
#     elif "a" <= ch <= "z":
#         h_l = True
#
#
#
#
# p = input("Введите пароль :")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("ненадежный")
# x = 123456789
# s = str(x)
# d = [int(x) for x in s if int(x) % 2 == 0]
# print(d)
# print(int(y))
# def get_summ(a, b, c, d = 4):
#     return a + b + c + d
#
#
# print(get_summ(1, 2, 3,))

# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="&")
# def number(n):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if current % 2 == 0:
#             s += current
#         print(current)
#         print(n)
#         n //= 10
#     return s
#
#
# print(number(9873532))
# print(number(5675434444))
# print(number(6753))
# def display(name, age):
#     print("Name", name, "\nAge", age)
#
#
# display("Ira", 23)
# display(23, "Ira")
# display(age=23, name="Igor")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt2 == lt1)
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# n = 5
# m = 5
# print(n == m)
# print(id(n), id(m))
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (5,)
# print(a)
# print(type(a))
# a = [1, 2, 3]
# b = tuple("Hello")
# print(b)
# def slicer(tp1, el):
#     if el in tp1:
#         if tp1.count(el) > 1:
#             a = tp1.index(el)
#             b = tp1.index(el, a + 1)
#             return tp1[a:b + 1]
#         else:
#             return tp1[tp1.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 3, 8, 3, 9, 4, 1), 8))
# t = (10, 11, [2, 3, 4], ["Hello, Word"])
# print(t)
# print(id(t))
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def function():
#     name = "Tom"
#     age = 23
#     hair = False
#     return name, age, hair
#
#
# user = function()
# first, name, wrong = user
# print(user)
# print(first, name, wrong)
# tpl = (1, 2, 3 )
# print(tpl)
# lst = list(tpl)
# print(lst)
# tpl_1 = tuple(lst)
# print(tpl_1)
# del tpl_1
# print(tpl_1)
# country = (
#     ("Германия", 89.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 89.2, (("Париж", 3.326), ("Марсель", 1.718))),
# )
#
# print(country, end="\n")
#
# for co in country:
#     country_name, country_population, cities_info = co
#     print("\nСтрана", country_name, "население =", country_population, "млн.")
#
#     for city_info in cities_info:
#         city_name, city_population = city_info
#         print(f"{city_name}: {city_population} млн.")
a = [1, 1, 2, 3, 4, 5, 6, 6]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
x = 10