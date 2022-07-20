# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = input('Введите числа списка через пробел: ')
arr = arr.split()
my_list = []

for i in arr:
    i = int(i)
    my_list.append(i)

print(my_list)

if len(my_list) % 2 != 0:
    for i in range(round(len(my_list)/2)+1):
        print(f'{my_list[i]} * {(len(my_list)-i)} = {my_list[i] * (len(my_list)-i)}')
else:
    for i in range(round(len(my_list)/2)):
        print(f'{my_list[i]} * {(len(my_list)-i)} = {my_list[i] * (len(my_list)-i)}')           