# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Введите число N = '))
# a = -n
# while a != n+1:
#     print(a, end=' ')  # end=' ' - это оператор, чтобы печатать в одну строку
#     a += 1

# n = int(input(('Введите N = ')))
# for i in range(-n, n+1):
#     print(i)


# 2. Напишите программу, которая будет принимать на вход дробь и показывать
# первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# x = float(input('-> '))
# x *= 10
# x = int(x)
# print(x % 10


# 3. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно (5 и 10) или (15, но не 30).

# x = int(input('--> '))
# if ((x % 5 == 0 and x % 10 == 0) or (x % 15 == 0 and x % 30 != 0)):
#     print('yes')
# else:
#     print('no')


# Ищем число после запятой

# a = '124,31'

# for i in range(len(a)):
#     if a[i] == ',':
#         print(a[i + 1])
#         break



# ¬ - not
# ⋁ - or
# ⋀ - and

# ДЗ на истинность
# rezult = True
# for X in True, False:
#     for Y in True, False:
#         for Z in True, False:
#             rezult = rezult and (not(X or Y or Z) == (not X and not Y and not Z))
# print(rezult)
