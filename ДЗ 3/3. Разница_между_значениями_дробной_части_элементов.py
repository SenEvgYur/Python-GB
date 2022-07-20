# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from math import trunc
import math

arr = input('Введите вещественные числа списка через пробел: ')
arr = arr.split()
my_list = []

for i in arr:
    i = float(i)
    my_list.append(i)

print(my_list)

my_list1 = []
for i in range(len(my_list)):
    if (my_list[i] % trunc(my_list[i]) != 0):
        my_list1.append(my_list[i] % trunc(my_list[i]))

print(my_list1)
print('Разница между максимальным и минимальным значением дробной части элементов = ', end="")
print(max(my_list1) - min(my_list1))
