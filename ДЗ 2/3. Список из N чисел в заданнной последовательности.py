# Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

n = int(input('Введите число: ')) 
my_list = []
for i in range(1, n + 1):
    my_list.append(round((1 + 1 / i)**i, 5))
print(f'Список из указанного числа: {my_list}')

summa_chisel = round(sum(my_list), 5)
print(f'Сумма всех членов в списке = {summa_chisel}')
