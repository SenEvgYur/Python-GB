# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.  
#     Примеры:   
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# my_list = []
# for i in [0, 1, 2, 3, 4]:
#     x = int(input('--> '))
#     my_list.append(x)
# print(f'Максимальное число: {max(my_list)}')

# my_list = []
# for i in range(5):
#     x = int(input('--> '))
#     my_list.append(x) # добавляем в список
# print(f'Максимальное число: {max(my_list)}')

maxx = 0
for i in range(5):
    x = int(input('--> '))
    if i == 0:
        maxx = x
    elif x > maxx:
        maxx = x

print(maxx)

# my_list = [5, 2, 9, 1, 3]
# i = 1
# maxx = my_list[0]
# while i < len(my_list):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#     i += 1

# print(maxx)
