# список - изменяемый, индексируемый                   []

# кортеж (tuple()) - не изменяемый, индексируемый      ( , )
# кортеж определяется запятой

# множество (set()) - изменяемый, не индексируемый     { не пустой }
# выводит уникальные элементы

# словарь (dictionary{}) - изменяемый, не индексируемый


# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# '12' -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'

# list = ['asd12', '12', 'asd', '87']
# n = input('Введите число: ')

# for i in list:
#     if n in i:
#         print(i)

    
# 2. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# count = 0
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцу", "йцу"]
# for i in range(len(my_list)):
#     if my_list[i] == 'йцу':
#         count += 1

#         if count > 1:
#             print(i)
#             break


# 3. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# my_set = set()
# for i in range(10):
#     my_set.add(str(i))

# for e in my_set:
#     print(int(e))

# def find_num(x):
#     a = str(time.time())
#     b = ''
#     count = 1
#     while count <= x:
#         b += a[-count]
#         count += 1
#     return int(b)

# print(find_num(3))

import time

l = int(input('Введите длинну числа: '))
a = time.time()
print(a)
ms = int(((a % 1) * (10 ** (l + 1))) % (10 ** (l)))
#ms = time.time()
#ms = int(time.time() % 10)

print(ms)
