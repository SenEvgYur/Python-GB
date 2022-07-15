# Ищем число после запятой

a = '124,41'

for i in range(len(a)):
    if a[i] == ',':
        print(a[i + 1])
        break
