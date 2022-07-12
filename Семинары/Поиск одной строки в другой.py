#Напишите программу, в которой пользователь будет задавать две строки, 
# а программа ищет сколько раз вторая строка содержится в первой

# str1 = "абракбадабра"
# str2 = "а"
# result = 0
# for i in range(len(str1) - len(str2) + 1):
#     if str1[i:i+len(str2)] == str2:
#         result += 1
# print(result)

# st1 = 'привет, мир, т, привет!'
# st2 = ','
# def str(st1, st2):
#     t = 0
#     for i in range(len(st1) - len(st2)):
#         if (st1[i : i + len(st2)] == st2):
#             t += 1
#     return t
# print(str(st1, st2))

def find_line(string:str, under_strind:str):
    print(string.count(under_strind))

user_string = input('Введите текст: ')
user_understring = input('Введите текст: ')
find_line(user_string, user_understring)