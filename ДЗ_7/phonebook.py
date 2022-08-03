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
        print('ФИО: ', i)


def user_id_if(text):   # печать ФИО по указанным буквам
    for i in contacts:
        if text in i:
            print('ФИО: ', i)


def phone_all():       # печать ФИО и телефонов всего справочника
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('ФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])


def phone_if(text):       # печать ФИО и телефона по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('ФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])


def birthday_all():         # печать ФИО и Даты рождения всего справочника
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('ФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])


def birthday_if(text):         # печать ФИО и Даты рождения по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('ФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])


def main_screen():    # запуск программы с выбором 
    print()
    print(
        'Выберите интересующий пункт меню: \n'
        '3. Проcмотр информации'
    )
    x = int(input())
    while x < 1 or x > 3:
        x = int(input())
    if x == 3:
        print()
        print(
        'Выберите интересующий пункт меню: \n'
        '1. Проcмотр всеx контактов \n'
        '2. Поиск контакта'
        )
        x = int(input())
        while x < 1 or x > 2:
            x = int(input())
        if x == 1:
            print()
            user_id()
            print()
            print(
                'Если хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
                )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                print()
                phone_all()
            else:
                print() 
                birthday_all()
        if x == 2:
            print()
            print('Введите буквы контакта, который ищите: ')
            my_text = input()
            print()
            user_id_if(my_text)
            print()
            print(
                'Если хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
            )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                print()
                phone_if(my_text)
            else:
                print() 
                birthday_if(my_text)
    print()

main_screen()
