# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

# лучше последовательность считать с файла

# Пример

# [1, 1, 2] -> [2]

arr = input('Введите числа списка через запятую: ')
file_path = r'ДЗ_4\файл_к_3_задаче.txt'
f = open(file_path, 'w')
f.write(arr)
f.close()

with open(file_path, 'r') as f:
    my_str = f.read()
my_str = my_str.split(',')
my_str2 = []

for i in my_str:
    i = int(i)
    my_str2.append(i)

print(f"Исходный список: {my_str2}")

new_str = my_str2
new_str1 = []

# пыталась сделать сравнение через 2 цикла
# ничего не вышло ((
for i in my_str2:
    for j in new_str:
        if i != j:
            new_str1.append(j)

print(f"Список из неповторяющихся элементов: {new_str1}")