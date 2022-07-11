# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# def searchNumber(a, b):
#     list = [1]
#     i = 1
#     while len(list) < a:
#         list.append(list[i-1]*b)
#         i += 1
#     print(list)
# searchNumber(6,-3)

# n = int(input('Введите число: '))
# result = 1
# for i in range(n):
#     print(result)
#     result *= -3

# def returnSequence(num):
#     prod = 1
#     print(prod, end = ' ')
#     for _ in range(num - 1):
#         prod *= -3
#         print(f"{prod} ", end = '')
# returnSequence(int(input("Please, input number "))

# def print_numbers(x):
#     vivod = 1
#     for i in range(x):
#         print(vivod)
#         vivod = vivod * -3
# n = int(input())
# print_numbers(n)

# Книги для изучения. Рекомедую читать именно в таком порядке:
# Byte of Python, Swaroop C. H.
# Грокаем алгоритмы, Адитья Бхаргава
# Изучаем Python (1, 2 том), Марк Лутц

# IDE, которую использовал на семинаре: https://www.onlinegdb.com/online_python_compiler
# PyCharm: https://www.jetbrains.com/ru-ru/pycharm/
# Дзен Python: https://tyapk.ru/blog/post/the-zen-of-python

#Напишите программу, в которой пользователь будет задавать две строки, 

# str1 = "абракбадабра"
# str2 = "а"
# result = 0
# for i in range(len(str1) - len(str2) + 1):
#     if str1[i:i+len(str2)] == str2:
#         result += 1
# print(result)

# st1 = 'привет, мир, т, привет!'
# st2 = ','
# def str(st1, st2):
#     t = 0
#     for i in range(len(st1) - len(st2)):
#         if (st1[i : i + len(st2)] == st2):
#             t += 1
#     return t
# print(str(st1, st2))

# def find_line(string:str, under_strind:str):
#     print(string.count(under_strind))

# user_string = input('Введите текст: ')
# user_understring = input('Введите текст: ')
# find_line(user_string, user_understring)




# для ДЗ
# (1 + 1/n)^n
