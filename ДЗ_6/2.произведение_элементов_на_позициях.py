# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

import random

n = int(input('Введите количество элементов в списке: '))
my_list = []

for i in range(n):
    my_list.append(random.randint(-n, n))

print(my_list)

# a = int(input('Введите индекс первого числа: '))
# while (a < 0) or (a > n-1):
#     a = int(input('Введите индекс первого числа: '))
    
# b = int(input('Введите индекс второго числа: '))
# while (b < 0) or (b > n-1):
#     b = int(input('Введите индекс второго числа: '))

a,b = map(int, input('Введите индекс числа: ').split())

print(f'{my_list[a]} x {my_list[b]} = {(my_list[a])*my_list[b]}')
