# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

x = int(input('Введите положительное число x больше или равное 2: '))
while x <= 1:
    x = int(input('Введите число x: '))

my_list = []
my_list.append(0)
my_list.append(1)

for i in range(2, x+1):
    my_list.append(my_list[i-2] - my_list[i-1])

my_list.reverse()    

my_list1 = []
my_list1.append(0)
my_list1.append(1)

for i in range(2, x+1):
    my_list1.append(my_list1[i-2] + my_list1[i-1])
del(my_list1[0])

my_list2 = my_list + my_list1
print(my_list2)
