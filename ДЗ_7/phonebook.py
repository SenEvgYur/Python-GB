contacts = {
    "Александров Александр": {'Телефон': '+7111111111', 'Дата рождения': '01.01.1998'},
    "Борисов Борис Борисович": {'Телефон': '+7222222222', 'Дата рождения': '02.02.2000'},
    "Владимиров Владимир Владимирович": {'Телефон': '+7333333333', 'Дата рождения': '03.03.1980'},
    "Денисов Денис Денисович": {'Телефон': '+7444444444', 'Дата рождения': '04.04.1993'},
    "Галкин Алексей Алексеевич": {'Телефон': '+7555555555', 'Дата рождения': '05.05.1990'},
    "Егоров Егор Егорович": {'Телефон': '+7666666666', 'Дата рождения': '06.06.2003'},
    "Жамнова Жанна Егоровна": {'Телефон': '+7777777777', 'Дата рождения': '07.07.2001'},
    "Зумин Евгений Федорович": {'Телефон': '+7888888888', 'Дата рождения': '08.08.1995'},
}


def user_id():    # печать ФИО всего справочника
    global contacts
    for i in contacts:
        print('\nФИО: ', i)


def user_id_if(text):   # печать ФИО по указанным буквам
    for i in contacts:
        if text in i:
            print('\nФИО: ', i)


def correction_id(text):
    for i in contacts:
        if text in i:
            print('\nНапишите новое ФИО:\n')
            i = input()


def phone_all():       # печать ФИО и телефонов всего справочника
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])


def phone_if(text):       # печать ФИО и телефона по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])


def correction_phone(text):
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
            print('\nНапишите новый телефон:\n')
            i = input()
    for person in persons:
        contacts[person]['Телефон'] = i


def birthday_all():         # печать ФИО и Даты рождения всего справочника
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])


def birthday_if(text):         # печать ФИО и Даты рождения по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])


# def add_to_fail():    # запись в файл
#     global contacts
#     persons = []
#     for i in contacts:
#             persons.append(i)        
#     for person in persons:
#         dozapis(person)
#         for data in contacts[person]:
#             dozapis(contacts[person][data])


# def dozapis(x):
#     my_path_a = r'ДЗ_7\my_phonebook.txt'
#     with open(my_path_a, 'a') as f:
#         my_notebook_a = f.write(x)


def main_screen():    # запуск программы с выбором 
    print(
        '\nВыберите интересующий пункт меню: \n'
        '1. Проcмотр информации\n'
        '2. Исправление информации\n'
        '3. Запись новой информации'
    )
    x = int(input())
    while x < 1 or x > 3:
        x = int(input())
    if x == 1:
        print(
        '\nВыберите интересующий пункт меню: \n'
        '1. Проcмотр всеx контактов \n'
        '2. Поиск контакта'
        )
        x = int(input())
        while x < 1 or x > 2:
            x = int(input())
        if x == 1:
            user_id()
            print(
                '\nЕсли хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
                )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                phone_all()
            else:
                birthday_all()
        if x == 2:
            print('\nВведите буквы контакта, который ищите: ')
            my_text = input()
            user_id_if(my_text)
            print(
                '\nЕсли хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
            )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                phone_if(my_text)
            else: 
                birthday_if(my_text)
    if x == 2:
        print('\nВведите буквы контакта, который ищите: ')
        my_text = input()
        user_id_if(my_text)
        print(
            '\nВыберите, что хотите исправить:\n'
            '1. ФИО\n'
            '2. телефон\n'
            '3. день рождения\n'
            '4. всю информацию'
            )
        x = int(input())
        while x < 1 or x > 4:
            x = int(input())
        if x == 1:
            correction_id()
        if x == 2:

    print()



# my_path_a = r'ДЗ_7\my_phonebook.txt'
# with open(my_path_a, 'a') as f:
#     my_notebook_a = f.write()


# my_path_w = r'ДЗ_7\my_phonebook.txt'
# with open(my_path_w, 'w') as f:
#     my_notebook_w = f.write()

# my_path_r = r'ДЗ_7\my_phonebook.txt'
# with open(my_path_r, 'r') as f:
#     my_notebook_r = f.read()