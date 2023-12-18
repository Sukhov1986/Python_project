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

dictionary_1 = {"name": "kelly", "age": 25, "salary": 8000, "city": "New York"}
print(dictionary_1)
dictionary_2 = {key: dictionary_1[key] for key in dictionary_1 if key in ["name", "salary"]}
for i in dictionary_2:
    dictionary_1.pop(i)


print(dictionary_1)
print(dictionary_2)

