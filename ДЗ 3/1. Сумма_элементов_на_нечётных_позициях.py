# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

arr = input('Введите числа списка через пробел: ')
arr = arr.split()
my_list = []

for i in arr:
    i = int(i)
    my_list.append(i)

print(my_list)

sum = 0

for i in range(len(my_list)):
    if (i % 2 != 0):
        print(f'Индекс {i} значение {my_list[i]}')
        sum += my_list[i]

print('Сумма элементов на нечётных индексах:', sum)
