# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# def searchNumber(a, b):
#     list = [1]
#     i = 1
#     while len(list) < a:
#         list.append(list[i-1]*b)
#         i += 1
#     print(list)
# searchNumber(6,-3)

# n = int(input('Введите число: '))
# result = 1
# for i in range(n):
#     print(result)
#     result *= -3

def returnSequence(num):
    prod = 1
    print(prod, end = ' ')
    for _ in range(num - 1):
        prod *= -3
        print(f"{prod} ", end = '')

num = int(input("Please, input number "))
returnSequence(num)
print()

# def print_numbers(x):
#     vivod = 1
#     for i in range(x):
#         print(vivod)
#         vivod = vivod * -3
# n = int(input())
# print_numbers(n)
