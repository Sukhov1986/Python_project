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

string = input('Введите строку -> ').lower()
vowels_1 = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
vowels_2 = [x for x in string if x in vowels_1]
print(f'Количество гласных равно : {len(vowels_2)}')
