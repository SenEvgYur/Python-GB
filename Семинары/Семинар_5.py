# my_str = '1, 22, 54, 76, 2'.split(',')
# #что сделать с элементом, с каким элементом, условие
# my_list = [int(item) for item in my_str]
# print(my_list)

# f = lambda x: True if x > 10 else False
# my_list = [12, 54, 3, 65]
# res = list(filter(f, my_list))
# print(res)

# my_list_1 = ['A', 'B', 'C', 'D']
# my_list_2 = [15, 76, 1, 98]
# my_list_3 = [65, 68]
# res = list(zip(my_list_1, my_list_2, my_list_3))
# print(res)

# data = list(map(int, input().split())) 


# 1. Удалить из исходной строки все слова с "абв"
# 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# str_list = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# # str_list = str_list.split()
# print(str)

# def strs(str):
#     for item in str_list:
#         if 'абв' in item:
#             str_list.remove(item)
#     print(str_list)
# # strs(str_list)

# res = list(filter(lambda item: 'абв' not in item, str_list.split()))
# print(res)

# 1. Удалить из исходной строки все слова с "абв"
# my_str = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# res = [word for word in my_str.split() if 'абв' not in word]
# print(' '.join(res))
