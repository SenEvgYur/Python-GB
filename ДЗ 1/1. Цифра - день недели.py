# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

x = int(input('Введите число от 1 до 7: '))
while (x > 7) or (x < 1):
    x = int(input('Введите число от 1 до 7: '))

if (x == 6) or (x == 7):
    print('Выходной день')
else:
    print('Будний день')