# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите положительное число N: '))
while(n <= 0):
    n = int(input('Введите положительное число N: '))

x = 1
for i in range(1, n+1):
    print(f'{x} x {i} = ', end=' ')
    x *= i
    print(x)
