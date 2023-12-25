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
# print(profit)
# table = PrettyTable(['Element/Month', 'January', 'February', "March"])
# table.align = 'r'
# table.align['Element/Month'] = "l"
# table.add_row(['Total Sales', Total_Sales['January'], Total_Sales['February'], Total_Sales["March"]])
# table.add_row(['Production Cost', Production_Cost['January'], Production_Cost['February'], Production_Cost["March"]])
# table.add_row(['Profit', profit['January'], profit['February'], profit["March"]])
# print(table)


def main():
    quantity = int(input("Введите количество учеников :"))
    return quantity


def data(**kwargs):
    return kwargs


def data_input():
    s_surname = input("Введите фамилию :")
    s_name = input("Введите имя :")
    s_point = int(input("Введите балл :"))
    return s_surname, s_name, s_point


students = main()
lst = []
res = 0
for i in range(students):
    a, b, c = data_input()
    res += c
    x = data(surname=a, name=b, point=c)
    lst.append(x)
average_mark = res / students
average_result = round(average_mark)
print(f"Средний балл {average_result}. Студенты с баллом выше среднего :")
for i in lst:
    if i["point"] > average_result:
        print(i["name"])

