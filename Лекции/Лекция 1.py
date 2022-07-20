# print('hello world') 
# a = 123
# b = 1.23
# value = None
# print(type(a))
# print(type(b))
# print(type(value))
# print(type(s)) 

# s = 'hello world'
# print(s) # вывод строки
# print(a, '-',b, '-',s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1,2,3]
# print(list)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, "=", a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметическкие операции
# +, -, *, /, %(остаток от деления), //(в ответе целое число), **
# **(возведение в степень), 
# (), Сокращённые операции
# a = 2
# b = 8
# c = a ** b
# print(c)
# round - для окруления чисел
# a = 3
# a *= 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=(не равно)
# not, and, or - не путать с &, |, ^
# Кое что ещё: is, is not, in, not in
# по умолчанию 0 - это ложь, а 1 - это истина
# f = [1,2,3,4]
# # is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции if, if - else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# list = range(7)
# for i in list:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwerty':
#     print(i)

# help(название команды) - справочная информация о команде

# Работа со строками
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))          # 39
# print('еще' in text)      # True
# print(text.isdigit())     # False
# print(text.islower())     # True
# print(text.replace('ещё','ЕЩЁ'))    #
# print(text[0])            # с
# print(text[1])            # ъ
# # print(text[len(text)])    # IndexError
# print(text[len(text)-1])  # к
# print(text[-5])           # б
# print(text[:])            # print(text)
# print(text[:2])           # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9])          # ешь ещё
# print(text[6:-18])        # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6])           # сеикакл
# #

# Списки. Введение
# numbers = [1,2,3,4,5]
# print(numbers)    # [1, 2, 3, 4, 5]