# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

x = float(input('Введите вещественное число: '))
x = abs(x)

while ((x % 1 > 0) and (x % 1 < 1)):
    x *= 10

summa_cifr = x % 10
while (x % 100 > 10):
    x = int(x / 10)
    summa_cifr += x % 10

summa_cifr = int(summa_cifr)
print(f'Сумма цифр в числе = {summa_cifr}')    