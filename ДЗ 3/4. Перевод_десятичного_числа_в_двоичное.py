# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = int(input('Введите положительное число x: '))
while x <= 0:
    x = int(input('Введите число x: '))

print(f'Число {x} в двоичной системе исчисления = ', end='')
my_list = []
while x >= 1:
    my_list.append(x % 2)
    x = x // 2

my_list.reverse()

for i in range(len(my_list)):
    print(my_list[i], end='')

# второй вариант переворачивания
# my_list1 = my_list[::-1]

# for i in range(len(my_list1)):
#     print(my_list1[i], end='')
