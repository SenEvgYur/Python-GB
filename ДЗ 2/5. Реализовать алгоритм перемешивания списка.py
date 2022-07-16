# Реализовать алгоритм перемешивания списка

import random

n = int(input('Введите количество чисел в списке: '))
my_list = []

for i in range(n):
    my_list.append(random.randint(-n, n))

print(my_list)

random.shuffle(my_list)

print(my_list)